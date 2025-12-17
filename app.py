import streamlit as st
import pandas as pd
import requests
from datetime import datetime, timedelta
import io

st.set_page_config(page_title="Wheel Strategy Pro Scanner", layout="wide")

# --- 0. CONFIGURAZIONE API ---
# Inserisci la tua chiave nella barra laterale (quella che abbiamo visto nello screenshot)
API_KEY = st.sidebar.text_input("Inserisci FMP API Key", type="password")

def get_fmp_data(endpoint, params=""):
    url = f"https://financialmodelingprep.com/api/v3/{endpoint}?apikey={API_KEY}{params}"
    try:
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None
    except:
        return None

st.title("🎯 Wheel Strategy Pro Scanner")
st.markdown("Analisi tecnica e fondamentale basata sui 7 criteri Finviz selezionati.")

if not API_KEY:
    st.warning("⚠️ Inserisci la tua API Key nella sidebar per iniziare.")
else:
    if st.button('🚀 AVVIA SCANSIONE COMPLETA'):
        # --- FILTRI 1, 2, 3 (SCREENER) ---
        # 1. Market Cap > 10B | 2. Optionable (implicito in Large Cap) | 3. Avg Volume > 1M
        st.info("Fase 1: Filtraggio Market Cap e Liquidità...")
        screener_params = "&marketCapMoreThan=10000000000&volumeMoreThan=1000000&isEtf=false&isActivelyTrading=true"
        stocks = get_fmp_data("stock-screener", screener_params)
        
        if stocks:
            results = []
            progress_bar = st.progress(0)
            today = datetime.now()
            next_week = today + timedelta(days=7)

            # Analizziamo un campione per ottimizzare le chiamate API
            for i, s in enumerate(stocks[:40]): 
                symbol = s['symbol']
                
                # Recupero Dati Storici (per Supporto, Volatilità e Rel. Volume)
                hist = get_fmp_data(f"historical-price-full/{symbol}", "&timeseries=30")
                if not hist or 'historical' not in hist: continue
                
                df = pd.DataFrame(hist['historical'])
                curr_price = df['close'].iloc[0]
                curr_vol = df['volume'].iloc[0]
                
                # --- FILTRO 7: Relative Volume > 1 ---
                avg_vol_10d = df['volume'].head(10).mean()
                rel_vol = curr_vol / avg_vol_10d
                
                # --- FILTRO 5: Volatilità Mensile > 2% ---
                vol_mensile = ((df['high'] - df['low']) / df['low']).mean() * 100
                
                # --- FILTRO 4: Dividend Yield > 0% ---
                div_yield = s.get('lastDiv', 0)
                
                # --- FILTRO 6: Controllo Earnings (Escludi se < 7gg) ---
                earn_data = get_fmp_data(f"historical/earnings-calendar/{symbol}")
                is_safe_earn = True
                if earn_data:
                    next_earn_str = earn_data[0].get('date')
                    if next_earn_str:
                        next_earn_dt = datetime.strptime(next_earn_str, '%Y-%m-%d')
                        if today <= next_earn_dt <= next_week:
                            is_safe_earn = False

                # APPLICAZIONE LOGICA FINALE (TUTTI I FILTRI DEVONO ESSERE VERI)
                if vol_mensile >= 2.0 and div_yield > 0 and rel_vol > 1.0 and is_safe_earn:
                    supp = df['low'].min()
                    # Strike suggerito al 90% del prezzo attuale (Delta conservativo)
                    strike = round((curr_price * 0.90) * 2) / 2
                    
                    results.append({
                        "Ticker": symbol,
                        "Prezzo ($)": round(curr_price, 2),
                        "Strike CSP": strike,
                        "Supporto (30g)": round(supp, 2),
                        "Div. Yield (%)": round(div_yield, 2),
                        "Volat. Mensile (%)": round(vol_mensile, 2),
                        "Rel. Volume": round(rel_vol, 2),
                        "Market Cap": f"{s['marketCap']/1e9:.1f}B"
                    })
                progress_bar.progress((i + 1) / 40)

            if results:
                df_final = pd.DataFrame(results)
                st.write("### 📊 Titoli che superano i 7 filtri")
                st.dataframe(df_final, use_container_width=True)

                # --- FUNZIONE ESPORTAZIONE EXCEL ---
                buffer = io.BytesIO()
                with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                    df_final.to_excel(writer, index=False, sheet_name='Analisi_Wheel')
                
                st.download_button(
                    label="📥 Scarica Report Excel",
                    data=buffer.getvalue(),
                    file_name=f"Wheel_Scan_{today.strftime('%Y%m%d')}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
            else:
                st.warning("Nessun titolo trovato con i parametri attuali. Prova a ridurre leggermente la Volatilità.")
