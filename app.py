import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Scanner Wheel 2025", layout="wide")

# La tua chiave confermata
API_KEY = "sQJgPn10EvTF6U4HzkVRukBF0Y0ijMrL"

def get_data(symbol):
    # Usiamo il profilo (per settore e mkt cap) e la quote (per il prezzo real-time)
    # Questi NON sono endpoint legacy e dovrebbero funzionare
    url_profile = f"https://financialmodelingprep.com/api/v3/profile/{symbol}?apikey={API_KEY}"
    url_quote = f"https://financialmodelingprep.com/api/v3/quote/{symbol}?apikey={API_KEY}"
    
    try:
        p_res = requests.get(url_profile).json()
        q_res = requests.get(url_quote).json()
        
        if p_res and q_res:
            p = p_res[0]
            q = q_res[0]
            return {
                "Ticker": symbol,
                "Prezzo": q.get('price'),
                "Variazione %": q.get('changesPercentage'),
                "Market Cap (B)": round(p.get('mktCap', 0) / 1e9, 2),
                "Settore": p.get('sector')
            }
        return None
    except:
        return None

st.title("🎯 Scanner Mercato USA - Versione 2025")
st.info("Questa versione evita gli endpoint 'Legacy' bloccati da FMP.")

if st.button('🚀 AVVIA ANALISI TITOLI SELEZIONATI'):
    # Lista di titoli attivi e liquidi (ottimi per le opzioni)
    tickers = ['AAPL', 'TSLA', 'NVDA', 'AMD', 'MSFT', 'AMZN', 'META', 'GOOGL', 'NFLX', 'PYPL', 'PLTR', 'BABA']
    
    results = []
    prog = st.progress(0)
    
    for i, t in enumerate(tickers):
        data = get_data(t)
        if data:
            # Calcoliamo uno Strike conservativo (-10% dal prezzo attuale)
            data["Strike Put Cons."] = round(data["Prezzo"] * 0.90, 1)
            results.append(data)
        prog.progress((i + 1) / len(tickers))
    
    if results:
        df = pd.DataFrame(results)
        st.write("### 📊 Opportunità Rilevate")
        st.dataframe(df.style.format({"Prezzo": "{:.2f}$", "Strike Put Cons.": "{:.2f}$", "Variazione %": "{:+.2f}%"}))
    else:
        st.error("Errore di autorizzazione. Assicurati che l'email di FMP sia stata confermata.")
