import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import requests
import time

st.set_page_config(page_title="Wheel Strategy Ultimate", layout="wide")

# --- 1. FUNZIONI DI RECUPERO TITOLI (Dinamiche + Backup) ---
@st.cache_data
def get_tickers(index_name):
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        if index_name == "S&P 500":
            url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
            res = requests.get(url, headers=headers)
            df = pd.read_html(res.text)[0]
            return [t.replace('.', '-') for t in df['Symbol'].tolist()]
        
        elif index_name == "Nasdaq-100":
            url = "https://en.wikipedia.org/wiki/Nasdaq-100"
            res = requests.get(url, headers=headers)
            # Spesso è la tabella 4 o 5 su Wikipedia
            df = pd.read_html(res.text)[4] 
            return [t.replace('.', '-') for t in df['Ticker'].tolist()]
        
        elif index_name == "Dow Jones":
            url = "https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average"
            res = requests.get(url, headers=headers)
            df = pd.read_html(res.text)[1]
            return [t.replace('.', '-') for t in df['Symbol'].tolist()]
    except:
        # Liste di emergenza se Wikipedia blocca la richiesta (Errore 403)
        st.warning(f"Utilizzo lista di emergenza per {index_name}")
        backups = {
            "S&P 500": ['AAPL', 'MSFT', 'AMZN', 'NVDA', 'GOOGL', 'META', 'TSLA', 'BRK-B', 'JPM', 'UNH'],
            "Nasdaq-100": ['AAPL', 'MSFT', 'AMZN', 'NVDA', 'GOOGL', 'META', 'TSLA', 'AVGO', 'COST', 'ADBE'],
            "Dow Jones": ['BA', 'UNH', 'GS', 'HD', 'MSFT', 'V', 'MCD', 'CAT', 'CRM', 'HON']
        }
        return backups.get(index_name, ['AAPL'])

# --- 2. LOGICA TECNICA: SUPPORTO E STRIKE STATISTICO ---
def get_analysis(ticker_obj, current_price):
    hist = ticker_obj.history(period="3mo")
    if hist.empty: return None
    
    # Supporto: Minimo delle ultime 20 sessioni
    support = hist['Low'].tail(20).min()
    
    # Volatilità Statistica (Deviazione Standard logaritmica)
    log_returns = pd.Series(hist['Close']).pct_change().dropna()
    std_dev = log_returns.std()
    
    # Strike Suggerito (1 Deviazione Standard sotto)
    # Formula: Prezzo * (1 - std_dev)
    suggested_strike = current_price * (1 - std_dev)
    
    # Volatilità mensile (%)
    vol_monthly = (std_dev * (21**0.5)) * 100
    
    return {
        "support": round(support, 2),
        "strike": round(suggested_strike * 2) / 2, # Arrotonda allo 0.50 più vicino
        "vol": round(vol_monthly, 2)
    }

# --- 3. INTERFACCIA SIDEBAR ---
st.sidebar.header("⚙️ Parametri Scanner")
target_index = st.sidebar.selectbox("Seleziona Indice", ["S&P 500", "Nasdaq-100", "Dow Jones", "Dividend Aristocrats"])
price_filter = st.sidebar.slider("Range Prezzo ($)", 0, 1000, (10, 500))
pe_filter = st.sidebar.number_input("P/E Ratio Massimo (0 = disattiva)", value=0.0)
vol_filter = st.sidebar.slider("Volatilità Minima (%)", 0.0, 10.0, 1.0)
limit_scan = st.sidebar.number_input("Limite titoli da scansionare", value=50)

st.title("🎯 Wheel Strategy Professional Scanner")
st.caption(f"Analisi avanzata su {target_index}. Filtri attivi: Prezzo {price_filter}$, Volatilità > {vol_filter}%")

# --- 4. ESECUZIONE SCANSIONE ---
if st.button('🚀 AVVIA SCANSIONE SETTORIALE'):
    tickers = get_tickers(target_index)[:int(limit_scan)]
    results = []
    progress_bar = st.progress(0)
    
    for i, symbol in enumerate(tickers):
        try:
            t = yf.Ticker(symbol)
            info = t.info
            price = info.get('currentPrice')
            
            # Filtro Prezzo e P/E
            if price and price_filter[0] <= price <= price_filter[1]:
                pe = info.get('trailingPE', 0)
                if pe_filter == 0 or (0 < pe <= pe_filter):
                    
                    analysis = get_analysis(t, price)
                    if analysis and analysis['vol'] >= vol_filter:
                        
                        # Controllo Earnings (Prossimi 7 giorni)
                        earnings_date = "N/A"
                        is_risky = "OK"
                        # Nota: yfinance a volte non fornisce 'nextEarningsDate', usiamo il calendario
                        cal = t.calendar
                        if cal is not None and not cal.empty:
                            next_e = cal.iloc[0, 0]
                            earnings_date = next_e.strftime('%Y-%m-%d')
                            if (next_e - datetime.now().date()).days <= 7:
                                is_risky = "⚠️ RISCHIO"

                        results.append({
                            "Ticker": symbol,
                            "Prezzo": price,
                            "P/E Ratio": round(pe, 1) if pe > 0 else "N/A",
                            "Volatilità %": analysis['vol'],
                            "Strike Suggerito (1-SD)": analysis['strike'],
                            "Supporto (20d)": analysis['support'],
                            "Prossimi Earnings": earnings_date,
                            "Alert": is_risky,
                            "Div. %": round(info.get('dividendYield', 0) * 100, 2)
                        })
            # Pausa per evitare blocchi Yahoo (molto importante online)
            time.sleep(0.1)
        except: continue
        progress_bar.progress((i + 1) / len(tickers))

    if results:
        df_res = pd.DataFrame(results)
        st.success(f"Analisi completata! Trovate {len(results)} opportunità.")
        
        # Formattazione condizionale per i colori
        def color_alert(val):
            color = 'red' if val == "⚠️ RISCHIO" else 'green'
            return f'color: {color}'

        st.dataframe(df_res.style.applymap(color_alert, subset=['Alert'])
                              .background_gradient(subset=['Volatilità %'], cmap='Oranges')
                              .background_gradient(subset=['Div. %'], cmap='Greens')
                              .format({'Prezzo': '{:.2f}$', 'Strike Suggerito (1-SD)': '{:.2f}$', 'Supporto (20d)': '{:.2f}$'}),
                     use_container_width=True)
    else:
        st.warning("Nessun titolo trovato. Prova ad allentare i filtri nella sidebar.")
