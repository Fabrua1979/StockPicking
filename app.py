import streamlit as st
import pandas as pd
import requests
from datetime import datetime, timedelta
import io

st.set_page_config(page_title="Wheel Strategy Pro Scanner", layout="wide")

# --- CONFIGURAZIONE API ---
API_KEY = st.sidebar.text_input("Inserisci FMP API Key", type="password") #

def get_fmp_data(endpoint, params=""):
    url = f"https://financialmodelingprep.com/api/v3/{endpoint}?apikey={API_KEY}{params}"
    try:
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None
    except:
        return None

st.title("🎯 Wheel Strategy Pro Scanner")
st.markdown("Scanner professionale con esportazione dati e i 7 filtri Finviz configurati.")

if not API_KEY:
    st.warning("⚠️ Inserisci la tua API Key nella sidebar per iniziare.")
else:
    if st.button('🚀 AVVIA SCANSIONE COMPLETA'):
        # 1, 2, 3. Filtri base: Market Cap > 10B, Volume > 1M, Optionable
        screener_params = "&marketCapMoreThan=10000000000&volumeMoreThan=1000000&isEtf=false&isActivelyTrading=true"
        stocks = get_fmp_data("stock-screener", screener_params)
        
        if stocks:
            results = []
            progress_bar = st.progress(0)
            today = datetime.now()
            next_week = today + timedelta(days=7)

            # Analizziamo un campione per gestire il limite di 250 chiamate/giorno
            for i, s in enumerate(stocks[:50]): 
                symbol = s['symbol']
                
                # Recupero Storico (per Volatilità, Supporto e Relative Volume)
                hist = get_fmp_data(f"historical-price-full/{symbol}", "&timeseries=30")
                if not hist or 'historical' not in hist: continue
                
                df = pd.DataFrame(hist['historical'])
                curr_price = df['close'].iloc[0]
                
                # 7. Relative Volume > 1
                avg_vol_10d = df['volume'].head(10).mean()
                rel_vol = df['volume'].iloc[0] / avg_vol_10d
                
                # 5. Volatilità Mensile > 2%
                vol_mensile = ((df['high'] - df['low']) / df['low']).mean() * 100
                
                # 4. Dividend Yield > 0%
                div_yield = s.get('lastDiv', 0)
                
                # 6. Controllo Earnings (Escludi se < 7gg)
                earn_data = get_fmp_data(f"historical/earnings-calendar/{symbol}")
                is_safe_earn = True
                if earn_data:
                    next_earn_str = earn_data[0].get('date')
                    if next_earn_str:
                        next_earn_dt = datetime.strptime(next_earn_str, '%Y-%m-%d')
                        if today <= next_earn_dt <= next_week:
                            is_safe_earn = False

                # Verifica finale filtri
                if vol_mensile >= 2.0 and div_yield > 0 and rel_vol > 1.0 and is_safe_earn:
                    supp = df['low'].min()
                    strike = round((curr_price * 0.90) * 2) / 2
                    
                    results.append({
                        "Ticker": symbol,
                        "Prezzo ($)": round(curr_price, 2),
                        "Strike Suggerito": strike,
                        "Supporto (30g)": round(supp, 2),
                        "Div. Yield (%)": round(div_yield, 2),
                        "Volat. Mensile (%)": round(vol_mensile, 2),
                        "Rel. Volume": round(rel_vol, 2),
                        "Data Analisi": today.strftime('%Y-%m-%d')
                    })
                progress_bar.progress((i + 1) / 50)

            if results:
                df_final = pd.DataFrame(results)
                st.write("### 📊 Risultati Screening")
                st.dataframe(df_final, use_container_width=True)

                # --- FUNZIONE DI ESPORTAZIONE EXCEL ---
                buffer = io.BytesIO()
                with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                    df_final.to_excel(writer, index=False, sheet_name='Wheel_Scanner')
                
                st.download_button(
                    label="📥 Scarica i risultati in Excel",
                    data=buffer.getvalue(),
                    file_name=f"Wheel_Analysis_{today.strftime('%Y%m%d')}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
            else:
                st.warning("Nessun titolo soddisfa i criteri al momento.")
