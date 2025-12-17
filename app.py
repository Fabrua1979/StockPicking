import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime
import requests

st.set_page_config(page_title="Wheel Pro Scanner - Ultimate", layout="wide")

# --- LISTA TICKER CORE ---
def get_reliable_tickers():
    return [
        "AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "META", "TSLA", "AVGO", "COST", "NFLX",
        "KO", "PEP", "JNJ", "PG", "WMT", "CVX", "XOM", "ABBV", "JPM", "V", "MA", "UNH", 
        "HD", "CSCO", "CRM", "BAC", "DIS", "ADBE", "ACN", "TMO"
    ]

st.title("🎯 Wheel Strategy Pro Scanner")
st.info("Questa versione utilizza un sistema di camuffamento per evitare i blocchi dei dati.")

# SIDEBAR
st.sidebar.header("⚙️ Parametri")
mcap_min = st.sidebar.number_input("Market Cap Min (B$)", value=5)
div_min = st.sidebar.number_input("Div. Yield Min (%)", value=0.0)
vol_min = st.sidebar.number_input("Volatilità Min (%)", value=0.5)

if st.button('🚀 AVVIA SCANSIONE'):
    tickers = get_reliable_tickers()
    results = []
    log_area = st.expander("📝 Log di Analisi", expanded=True)
    progress_bar = st.progress(0)
    
    # Setup sessione per evitare blocchi
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    })

    for i, t in enumerate(tickers):
        try:
            log_area.write(f"Scansione di {t}...")
            stock = yf.Ticker(t, session=session)
            
            # Scarichiamo la cronologia (metodo più affidabile per i prezzi)
            hist = stock.history(period="5d")
            if hist.empty:
                log_area.warning(f"⚠️ {t}: Nessuno storico trovato")
                continue
            
            price = hist['Close'].iloc[-1]
            
            # Dati fondamentali
            info = stock.info
            mcap = info.get('marketCap', 0) / 1e9
            div = info.get('dividendYield', 0) * 100
            
            # Calcoli tecnici su base mensile
            hist_m = stock.history(period="1mo")
            vol_calc = ((hist_m['High'] - hist_m['Low']) / hist_m['Low']).mean() * 100
            supp = hist_m['Low'].min()
            
            # Calcolo Strike CSP (Deviazione Standard semplificata)
            std = hist_m['Close'].pct_change().std()
            strike = round((price * (1 - (std * 4.47))) * 2) / 2 # 4.47 è radice di 20gg

            if mcap >= mcap_min and div >= div_min and vol_calc >= vol_min:
                results.append({
                    "Ticker": t,
                    "Prezzo": f"{price:.2f}$",
                    "Supporto": f"{supp:.2f}$",
                    "Strike Suggerito": f"{strike:.2f}$",
                    "Dividendo": f"{div:.2f}%",
                    "Volatilità": f"{vol_calc:.1f}%"
                })
                log_area.success(f"✅ {t} caricato correttamente.")
            else:
                log_area.info(f"❌ {t} filtrato (non rispetta i parametri).")

        except Exception as e:
            log_area.error(f"❗ Errore critico su {t}: {str(e)[:100]}")
            
        progress_bar.progress((i + 1) / len(tickers))

    if results:
        st.write("### 📊 Selezione Titoli per Wheel Strategy")
        st.dataframe(pd.DataFrame(results), use_container_width=True)
    else:
        st.error("Ancora nessun dato. Prova a riavviare l'app tra pochi minuti, Yahoo potrebbe aver temporaneamente limitato l'IP.")
