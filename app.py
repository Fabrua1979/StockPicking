import streamlit as st
import pandas as pd
import requests
from datetime import datetime, timedelta
import io

st.set_page_config(page_title="Wheel Strategy Pro Scanner", layout="wide")

# --- 1. CONFIGURAZIONE API & SECRETS ---
if "FMP_API_KEY" in st.secrets:
    API_KEY = st.secrets["FMP_API_KEY"]
else:
    API_KEY = st.sidebar.text_input("Inserisci FMP API Key", type="password")

def get_fmp_data(endpoint, params=""):
    url = f"https://financialmodelingprep.com/api/v3/{endpoint}?apikey={API_KEY}{params}"
    try:
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None
    except:
        return None

# --- 2. SIDEBAR PARAMETRI ---
st.sidebar.header("⚙️ Parametri Screening")
mcap_min = st.sidebar.slider("Market Cap Minima (Biliardi $)", 1, 200, 10)
div_min = st.sidebar.number_input("Dividend Yield Min (%)", value=1.5)
vol_min = st.sidebar.slider("Volatilità Mensile Min (%)", 0.0, 10.0, 2.0)
avoid_earn = st.sidebar.checkbox("Nascondi Earnings imminenti (< 7gg)", value=True)

st.title("🎯 Wheel Strategy Pro Scanner")

if not API_KEY:
    st.warning("⚠️ Inserisci la tua API Key nella sidebar o nei Secrets per iniziare.")
else:
    if st.button('🚀 AVVIA SCANSIONE MERCATO'):
        st.info(f"Analisi in corso sui titoli con Market Cap > {mcap_min}B...")
        
        mcap_api = mcap_min * 1000000000
        stocks = get_fmp_data("stock-screener", f"&marketCapMoreThan={mcap_api}&volumeMoreThan=1000000&isEtf=false&isActivelyTrading=true")
        
        if stocks:
            results = []
            progress_bar = st.progress(0)
            today = datetime.now()
            next_week = today + timedelta(days=7)

            for i, s in enumerate(stocks[:40]): 
                symbol = s['symbol']
                hist = get_fmp_data(f"historical-price-full/{symbol}", "&timeseries=30")
                if not hist or 'historical' not in hist: continue
                
                df = pd.DataFrame(hist['historical'])
                curr_price = df['close'].iloc[0]
                vol_mensile = ((df['high'] - df['low']) / df['low']).mean() * 100
                div_yield = s.get('lastDiv', 0)
                
                avg_vol_10d = df['volume'].head(10).mean()
                rel_vol = df['volume'].iloc[0] / avg_vol_10d

                is_safe_earn = True
                if avoid_earn:
                    earn_data = get_fmp_data(f"historical/earnings-calendar/{symbol}")
                    if earn_data and len(earn_data) > 0:
                        next_earn = datetime.strptime(earn_data[0].get('date'), '%Y-%m-%d')
                        if today <= next_earn <= next_week: is_safe_earn = False

                if vol_mensile >= vol_min and div_yield >= div_min and rel_vol > 1.0 and is_safe_earn:
                    results.append({
                        "Ticker": symbol,
                        "Prezzo": round(curr_price, 2),
                        "Strike CSP": round((curr_price * 0.90) * 2) / 2,
                        "Div. %": round(div_yield, 2),
                        "Volat. %": round(vol_mensile, 2),
                        "Rel. Vol": round(rel_vol, 2)
                    })
                progress_bar.progress((i + 1) / 40)

            if results:
                df_res = pd.DataFrame(results)
                st.session_state['scan_results'] = df_res # Salviamo per il calcolatore
                
                def style_table(styler):
                    styler.background_gradient(subset=['Div. %'], cmap='Greens')
                    styler.background_gradient(subset=['Volat. %'], cmap='Oranges')
                    styler.format({'Prezzo': '{:.2f}$', 'Strike CSP': '{:.2f}$'})
                    return styler

                st.write("### 📊 Risultati Screening")
                st.dataframe(style_table(df_res.style), use_container_width=True)

                buffer = io.BytesIO()
                with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                    df_res.to_excel(writer, index=False)
                st.download_button("📥 Scarica Report Excel", buffer.getvalue(), "wheel_scan.xlsx")
            else:
                st.warning("Nessun titolo trovato con i filtri attuali.")

    # --- 3. CALCOLATORE ROI (Visualizzato solo se ci sono risultati) ---
    if 'scan_results' in st.session_state:
        st.divider()
        st.subheader("🧮 Calcolatore Profitto Opzioni (CSP)")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            ticker_sel = st.selectbox("Seleziona Ticker", st.session_state['scan_results']['Ticker'])
            selected_row = st.session_state['scan_results'][st.session_state['scan_results']['Ticker'] == ticker_sel].iloc[0]
        
        with col2:
            premio = st.number_input("Premio incassato ($)", value=50.0, step=5.0)
            days = st.number_input("Giorni alla scadenza", value=30, step=1)
            
        with col3:
            capitale_richiesto = selected_row['Strike CSP'] * 100
            roi_periodo = (premio / capitale_richiesto) * 100
            roi_annuale = roi_periodo * (365 / days)
            
            st.metric("ROI Periodo", f"{roi_periodo:.2f}%")
            st.metric("ROI Annualizzato", f"{roi_annuale:.2f}%", delta="Obiettivo Wheel: >15%")
