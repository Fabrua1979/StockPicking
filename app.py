import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Scanner Wheel Gratuito", layout="wide")

st.title("🎯 Scanner Mercato USA (Motore Yahoo Finance)")
st.write("Questa versione non usa chiavi API e non può essere bloccata.")

# Lista di titoli famosi e liquidi
TICKERS = ['AAPL', 'TSLA', 'NVDA', 'AMD', 'MSFT', 'AMZN', 'META', 'GOOGL', 'NFLX', 'PLTR', 'BABA', 'DIS']

if st.button('🚀 AVVIA SCANSIONE ORA'):
    results = []
    prog = st.progress(0)
    status = st.empty()
    
    for i, t in enumerate(TICKERS):
        status.text(f"Scaricando dati per {t}...")
        try:
            ticker_data = yf.Ticker(t)
            info = ticker_data.info
            
            price = info.get('currentPrice')
            if price:
                # Calcoliamo lo strike per la Put (-10%)
                strike = round(price * 0.90, 1)
                results.append({
                    "Ticker": t,
                    "Prezzo Attuale": f"{price:.2f}$",
                    "Strike Consigliato (-10%)": f"{strike:.2f}$",
                    "Settore": info.get('sector', 'N/A'),
                    "Market Cap (B)": f"{info.get('marketCap', 0) / 1e9:.1f}"
                })
        except:
            continue
        prog.progress((i + 1) / len(TICKERS))
    
    status.empty()
    if results:
        st.write("### 📊 Risultati Analisi")
        st.table(pd.DataFrame(results))
    else:
        st.error("Errore nel recupero dati da Yahoo Finance. Riprova tra un istante.")
