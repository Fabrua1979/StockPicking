import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime

# CONFIGURAZIONE DELLA PAGINA
st.set_page_config(page_title="Wheel Strategy Pro Scanner", layout="wide", initial_sidebar_state="expanded")

# --- LOGICA DI CALCOLO E FILTRI ---

@st.cache_data(ttl=604800) # La lista dei ticker viene aggiornata una volta a settimana
def get_market_tickers():
    try:
        # S&P 500
        sp500 = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]['Symbol'].tolist()
        # Nasdaq 100
        nasdaq100 = pd.read_html('https://en.wikipedia.org/wiki/Nasdaq-100')[4]['Ticker'].tolist()
        tickers = list(set(sp500 + nasdaq100))
        return [t.replace('.', '-') for t in tickers] # Correzione ticker per Yahoo Finance
    except:
        return ["AAPL", "MSFT", "KO", "PEP", "JNJ", "PG", "WMT", "CVX"]

def get_technical_data(ticker_obj):
    """Calcola il supporto (minimo a 6 mesi) e lo strike suggerito"""
    hist_6m = ticker_obj.history(period="6mo")
    hist_1m = ticker_obj.history(period="1mo")
    
    if len(hist_6m) < 20 or len(hist_1m) < 15:
        return 0, 0, 0
    
    # Supporto Tecnico (Punto di rimbalzo storico)
    supporto = min(hist_6m['Low'].tail(20).min(), hist_6m['Low'].tail(60).min())
    
    # Volatilità Mensile (Filtro Finviz punto 5)
    vol_mensile = ((hist_1m['High'] - hist_1m['Low']) / hist_1m['Low']).mean() * 100
    
    # Strike Statistico (Delta ~0.20 / 1 Deviazione Standard)
    daily_std = hist_1m['Close'].pct_change().std()
    margin = daily_std * np.sqrt(20) * 1.2 # Proiezione a 30gg
    strike = round((hist_1m['Close'].iloc[-1] * (1 - margin)) * 2) / 2
    
    return round(supporto, 2), round(strike, 2), round(vol_mensile, 2)

# --- INTERFACCIA UTENTE (STREAMLIT) ---

st.title("🎯 Wheel Strategy Pro Scanner")
st.markdown("Scanner avanzato basato sui parametri di **Finviz** e **Barchart**.")

# SIDEBAR PER I FILTRI
st.sidebar.header("⚙️ Parametri Screening")
min_mcap = st.sidebar.slider("Market Cap Minima (Biliardi $)", 10, 500, 20)
min_div = st.sidebar.number_input("Dividend Yield Min (%)", value=1.5, step=0.5)
min_vol_filter = st.sidebar.slider("Volatilità Mensile Min (%)", 1.0, 10.0, 2.0)

st.sidebar.header("🚨 Gestione Rischio")
exclude_earn = st.sidebar.checkbox("Nascondi Earnings imminenti (< 7gg)", value=True)

if st.button('🚀 AVVIA SCANSIONE MERCATO'):
    all_tickers = get_market_tickers()
    results = []
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Scansione di un campione significativo (es. primi 120 per stabilità)
    limit = 120 
    for i, t in enumerate(all_tickers[:limit]):
        status_text.text(f"Analisi in corso: {t}...")
        try:
            stock = yf.Ticker(t)
            info = stock.info
            
            # Recupero dati fondamentali
            mcap = info.get('marketCap', 0) / 1e9
            div = info.get('dividendYield', 0) * 100
            price = info.get('currentPrice', 0)
            avg_vol = info.get('averageVolume', 0)
            
            # Supporto, Strike e Volatilità calcolata
            supp, strike, vol_m = get_technical_data(stock)

            # Controllo Earnings
            calendar = stock.calendar
            days_to_earn = 999
            if calendar is not None and 'Earnings Date' in calendar:
                earn_date = calendar['Earnings Date'][0].replace(tzinfo=None)
                days_to_earn = (earn_date - datetime.now()).days

            # APPLICAZIONE FILTRI (SCREENSHOT FINVIZ)
            if (mcap >= min_mcap and div >= min_div and 
                avg_vol > 1000000 and vol_m >= min_vol_filter):
                
                if exclude_earn and 0 <= days_to_earn < 7:
                    continue
                
                results.append({
                    "Ticker": t,
                    "Prezzo": f"{price:.2f}$",
                    "Supporto Tecnico": f"{supp:.2f}$",
                    "Strike Suggerito": f"{strike:.2f}$",
                    "Div. Yield": f"{div:.2f}%",
                    "Vol. Mensile": f"{vol_m:.1f}%",
                    "Giorni a Earnings": days_to_earn if days_to_earn != 999 else "N/D",
                    "Status": "⚠️ EARNINGS" if 0 <= days_to_earn < 7 else "✅ OK"
                })
        except:
            continue
        progress_bar.progress((i + 1) / limit)

    status_text.empty()

    if results:
        df = pd.DataFrame(results)
        st.success(f"Trovati {len(results)} titoli validi per la Wheel!")
        
        # Formattazione ed evidenziazione rischi
        st.dataframe(df.style.applymap(
            lambda x: 'background-color: #ff4b4b; color: white' if x == '⚠️ EARNINGS' else '', 
            subset=['Status']
        ), use_container_width=True)
    else:
        st.warning("Nessun titolo soddisfa i criteri impostati. Prova ad abbassare la Market Cap o il Dividendo.")

st.divider()
st.caption("Dati forniti da Yahoo Finance. Lo Strike Suggerito è puramente indicativo e basato sulla volatilità storica a 30 giorni.")
