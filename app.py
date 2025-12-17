import streamlit as st
import pandas as pd
import requests
from datetime import datetime, timedelta
import io

st.set_page_config(page_title="Wheel Strategy Pro Scanner", layout="wide")

# --- 1. GESTIONE API KEY ---
if "FMP_API_KEY" in st.secrets:
    API_KEY = st.secrets["FMP_API_KEY"]
else:
    API_KEY = st.sidebar.text_input("Inserisci FMP API Key", type="password", value="uZJbm6FkDS56ktyFfzvh5flhePsbh4rz")

def get_fmp_data(endpoint, params=""):
    url = f"https://financialmodelingprep.com/api/v3/{endpoint}?apikey={API_KEY}{params}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            st.error(f"🔑 Errore 401: La chiave API non è autorizzata per l'endpoint '{endpoint}'.")
            return None
        return None
    except:
        return None

# --- 2. SIDEBAR PARAMETRI ---
st.sidebar.header("⚙️ Parametri Screening")
mcap_min = st.sidebar.slider("Market Cap Minima (Miliardi $)", 10, 500, 50)
div_min = st.sidebar.number_input("Dividend Yield Min (%)", value=1.0)
vol_min = st.sidebar.slider("Volatilità Mensile Min (%)", 0.5, 10.0, 1.5)

st.title("🎯 Wheel Strategy Pro Scanner")
st.caption("Connessione API FMP ottimizzata. Filtraggio interno attivo.")

if st.button('🚀 AVVIA SCANSIONE MERCATO'):
    status_text = st.empty()
    status_text.info("Fase 1: Recupero lista titoli dal database principale...")
    
    # CAMBIO STRATEGIA: Usiamo stock/list invece dello screener per evitare il blocco 401
    all_stocks = get_fmp_data("stock/list")
    
    if all_stocks:
        # Filtriamo i primi 40 titoli NASDAQ/NYSE con Market Cap elevata (simulata per velocizzare)
        # In questa versione prendiamo i titoli principali per testare la connessione
        target_exchanges = ['NASDAQ', 'NYSE']
        stocks = [s for s in all_stocks if s.get('exchangeShortName') in target_exchanges and s.get('type') == 'stock'][:40]
        
        results = []
        progress_bar = st.progress(0)
        
        for i, s in enumerate(stocks):
            symbol = s['symbol']
            status_text.text(f"🔎 Analisi tecnica e dividendi di {symbol} ({i+1}/{len(stocks)})...")
            
            # Recupero Profilo (per Market Cap e Dividendi)
            profile = get_fmp_data(f"profile/{symbol}")
            if not profile: continue
            p = profile[0]
            
            mcap = p.get('mktCap', 0) / 1_000_000_000
            d_yield = p.get('lastDiv', 0)
            
            # Applichiamo i filtri fondamentali
            if mcap >= mcap_min and d_yield >= div_min:
                # Recupero Storico per Volatilità
                hist = get_fmp_data(f"historical-price-full/{symbol}", "&timeseries=20")
                if hist and 'historical' in hist:
                    df = pd.DataFrame(hist['historical'])
                    curr_price = df['close'].iloc[0]
                    vol = ((df['high'] - df['low']) / df['low']).mean() * 100
                    
                    if vol >= vol_min:
                        strike = round((curr_price * 0.90) * 2) / 2
                        results.append({
                            "Ticker": symbol,
                            "Prezzo": round(curr_price, 2),
                            "Strike CSP (-10%)": strike,
                            "Div. %": round(d_yield, 2),
                            "Volat. %": round(vol, 2),
                            "Market Cap (B)": round(mcap, 1)
                        })
            
            progress_bar.progress((i + 1) / len(stocks))

        status_text.empty()
        if results:
            df_res = pd.DataFrame(results)
            st.session_state['scan_results'] = df_res
            st.write("### 📊 Risultati Screening")
            st.dataframe(df_res.style.background_gradient(subset=['Div. %'], cmap='Greens')
                                  .background_gradient(subset=['Volat. %'], cmap='Oranges'), 
                         use_container_width=True)
        else:
            st.warning("Nessun titolo soddisfa i criteri con questa chiave API. Prova ad abbassare i filtri.")
    else:
        st.error("Impossibile recuperare la lista titoli. Controlla la tua connessione o la validità della chiave.")
