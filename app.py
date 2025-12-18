import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Scanner Professionale", layout="wide")

# --- CHIAVE API ---
# Uso la tua nuova chiave sQJgPn... come valore predefinito
api_key = st.sidebar.text_input("FMP API Key", type="password", value="sQJgPn10EvTF6U4HzkVRukBF0Y0ijMrL")

def fetch_fmp(url):
    # Questo Header serve a "ingannare" il server e fargli credere che siamo un browser
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    try:
        response = requests.get(f"{url}&apikey={api_key}", headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None

st.title("🎯 Scanner Mercato USA")

if st.button('🚀 AVVIA ANALISI PROFONDA'):
    status = st.empty()
    status.info("Connessione al database in corso...")
    
    # 1. Recuperiamo la lista dei titoli (Endpoint alternativo più stabile)
    stocks_list = fetch_fmp("https://financialmodelingprep.com/api/v3/stock/list?")
    
    if stocks_list:
        # Filtriamo i primi 50 titoli NASDAQ/NYSE per il test
        subset = [s for s in stocks_list if s.get('exchangeShortName') in ['NASDAQ', 'NYSE']][:50]
        results = []
        prog = st.progress(0)
        
        for i, s in enumerate(subset):
            ticker = s['symbol']
            status.text(f"Analizzando {ticker}...")
            
            # Chiamata singola per profilo
            p_data = fetch_fmp(f"https://financialmodelingprep.com/api/v3/profile/{ticker}?")
            if p_data:
                p = p_data[0]
                mcap = p.get('mktCap', 0) / 1e9
                div = p.get('lastDiv', 0)
                
                # Applichiamo filtri base
                if mcap > 2 and div > 0:
                    results.append({
                        "Ticker": ticker,
                        "Prezzo": p.get('price'),
                        "Dividendo %": div,
                        "Market Cap (B)": round(mcap, 2)
                    })
            prog.progress((i + 1) / len(subset))
            
        status.empty()
        if results:
            st.write("### Risultati Scansione")
            st.dataframe(pd.DataFrame(results))
        else:
            st.warning("Nessun titolo trovato. Prova ad abbassare i filtri nella sidebar.")
    else:
        st.error("Errore critico: Il server FMP ha rifiutato la connessione. Prova a ricaricare la pagina.")
