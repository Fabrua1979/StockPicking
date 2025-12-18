import streamlit as st
import pandas as pd
import yfinance as yf
import io
import time
import requests # Necessario per superare il blocco 403

st.set_page_config(page_title="Wheel Strategy PRO - 500 Titoli", layout="wide")

# --- 1. RECUPERO LISTA S&P 500 CON AGENT (RISOLVE ERRORE 403) ---
@st.cache_data
def get_sp500_tickers():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        # Usiamo requests per simulare un browser ed evitare il "Forbidden"
        response = requests.get(url, headers=headers)
        tables = pd.read_html(response.text)
        df = tables[0]
        tickers = df['Symbol'].tolist()
        # Pulizia simboli per Yahoo Finance (es: BRK.B -> BRK-B)
        return [t.replace('.', '-') for t in tickers]
    except Exception as e:
        st.error(f"⚠️ Impossibile caricare i 500 titoli: {e}. Uso lista ridotta.")
        return ['AAPL', 'MSFT', 'NVDA', 'TSLA', 'AMZN', 'META', 'AMD', 'GOOGL', 'NFLX']

# --- 2. SIDEBAR PARAMETRI ---
st.sidebar.header("⚙️ Filtri di Scansione")
mcap_min = st.sidebar.slider("Market Cap Minima (Miliardi $)", 0, 500, 0)
div_min = st.sidebar.number_input("Dividend Yield Min (%)", value=0.0)
vol_min = st.sidebar.slider("Volatilità Mensile Min (%)", 0.0, 10.0, 0.0)
limit_scan = st.sidebar.number_input("Titoli da scansionare (max 503)", value=500)

st.title("🎯 Wheel Strategy Global Scanner")
st.caption("Accesso completo all'indice S&P 500 tramite bypass Wikipedia.")

# --- 3. MOTORE DI SCANSIONE ---
if st.button('🚀 AVVIA SCANSIONE COMPLETA'):
    all_tickers = get_sp500_tickers()
    tickers_to_scan = all_tickers[:int(limit_scan)]
    
    st.info(f"Avvio analisi su {len(tickers_to_scan)} titoli. Il processo richiederà qualche minuto.")
    
    results = []
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i, symbol in enumerate(tickers_to_scan):
        status_text.text(f"🔎 Analisi: {symbol} ({i+1}/{len(tickers_to_scan)})")
        
        try:
            t = yf.Ticker(symbol)
            info = t.info
            
            if info and 'currentPrice' in info:
                price = info.get('currentPrice')
                mcap = info.get('marketCap', 0) / 1e9
                dy = info.get('dividendYield', 0) * 100
                
                if mcap >= mcap_min and dy >= div_min:
                    hist = t.history(period="1mo")
                    if not hist.empty:
                        # Volatilità media High-Low mensile
                        vol = ((hist['High'] - hist['Low']) / hist['Low']).mean() * 100
                        
                        if vol >= vol_min:
                            results.append({
                                "Ticker": symbol,
                                "Prezzo": price,
                                "Strike (-10%)": round((price * 0.90) * 2) / 2,
                                "Div. %": round(dy, 2),
                                "Volatilità %": round(vol, 2),
                                "Cap. (Mld $)": round(mcap, 1),
                                "Settore": info.get('sector', 'N/A')
                            })
            
            # Pausa breve per evitare di essere bloccati da Yahoo Finance
            time.sleep(0.05)
            
        except:
            continue
            
        progress_bar.progress((i + 1) / len(tickers_to_scan))

    status_text.empty()
    
    if results:
        df_res = pd.DataFrame(results)
        st.success(f"✅ Scansione terminata! Trovate {len(results)} opportunità.")
        
        # Tabella con colori (ora funzionerà grazie a matplotlib installato)
        st.dataframe(df_res.style.background_gradient(subset=['Div. %'], cmap='Greens')
                                  .background_gradient(subset=['Volatilità %'], cmap='Oranges')
                                  .format({'Prezzo': '{:.2f}$', 'Strike (-10%)': '{:.2f}$'}), 
                     use_container_width=True)
        
        # Export CSV
        csv = df_res.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Scarica Report CSV", csv, "wheel_scan_full.csv", "text/csv")
    else:
        st.warning("Nessun titolo trovato. Prova ad allentare i filtri nella sidebar.")
