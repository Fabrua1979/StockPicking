import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Wheel Scanner Lite", layout="wide")

API_KEY = "sQJgPn10EvTF6U4HzkVRukBF0Y0ijMrL"

def get_profile(symbol):
    url = f"https://financialmodelingprep.com/api/v3/profile/{symbol}?apikey={API_KEY}"
    try:
        r = requests.get(url)
        return r.json()[0] if r.status_code == 200 and r.json() else None
    except:
        return None

st.title("🎯 Scanner Wheel Strategy (Versione Compatibile)")
st.write("Questa versione utilizza una lista titoli predefinita per evitare i blocchi del piano API.")

if st.button('🚀 AVVIA SCANSIONE'):
    # Lista di 40 titoli molto scambiati e famosi (evita la Stock Directory bloccata)
    tickers = [
        'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'TSLA', 'NVDA', 'JPM', 'V', 'MA',
        'JNJ', 'PG', 'HD', 'DIS', 'KO', 'PEP', 'CVX', 'XOM', 'ABBV', 'MRK',
        'PFE', 'WMT', 'T', 'VZ', 'INTC', 'CSCO', 'BA', 'MCD', 'NKE', 'IBM',
        'AMD', 'NFLX', 'PYPL', 'ADBE', 'CRM', 'QCOM', 'TXN', 'COST', 'SBUX', 'AMAT'
    ]
    
    results = []
    progress_bar = st.progress(0)
    
    for i, ticker in enumerate(tickers):
        data = get_profile(ticker)
        if data:
            mcap = data.get('mktCap', 0) / 1e9
            div = data.get('lastDiv', 0)
            # Filtro: Capitalizzazione > 10B e ha un dividendo
            if mcap > 10 and div > 0:
                price = data.get('price', 0)
                strike = round((price * 0.90) * 2) / 2
                results.append({
                    "Ticker": ticker,
                    "Prezzo": f"{price:.2f}$",
                    "Strike Put (-10%)": f"{strike:.2f}$",
                    "Dividendo": f"{div:.2f}%",
                    "Cap. (B)": f"{mcap:.1f}"
                })
        progress_bar.progress((i + 1) / len(tickers))

    if results:
        st.success(f"Analisi completata! Trovati {len(results)} titoli.")
        st.table(pd.DataFrame(results))
    else:
        st.error("Nessun dato recuperato. Verifica di aver confermato l'email di FMP.")
