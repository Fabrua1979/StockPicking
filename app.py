import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime
import time
import plotly.express as px

st.set_page_config(page_title="Wheel Strategy MEGA Scanner", layout="wide")

# --- 1. DATABASE MASSIVO (Liste estese) ---
@st.cache_data
def get_massive_stock_list():
    # Liste espanse (Puoi incollare qui centinaia di ticker)
    sp500 = [
        'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'META', 'BRK-B', 'LLY', 'AVGO', 'V', 'JPM', 'TSLA', 'MA', 'UNH', 'PG', 'XOM', 'HD', 'JNJ', 'COST', 'ORCL', 'MRK', 'ABBV', 'CVX', 'CRM', 'AMD', 'ADBE', 'PEP', 'WMT', 'KO', 'BAC', 'ACN', 'TMO', 'BAC', 'LIN', 'NFLX', 'DIS', 'CSCO', 'TMUS', 'DHR', 'INTU', 'QCOM', 'ABT', 'CAT', 'VZ', 'TXN', 'AMAT', 'AMGN', 'AXP', 'PFE', 'IBM', 'MS', 'GE', 'PM', 'UNP', 'HON', 'GS', 'LOW', 'SPGI', 'RTX', 'INTC', 'SYK', 'LMT', 'ELV', 'DE', 'BKNG', 'TJX', 'COP', 'BLK', 'ETN', 'MDLZ', 'REGN', 'ADP', 'PGR', 'CVS', 'VRTX', 'MMC', 'CI', 'ADI', 'BSX', 'LRCX', 'SCHW', 'MU', 'T', 'ZTS', 'PANW', 'WM', 'C', 'FI', 'BA', 'PLD', 'SNPS', 'GILD', 'UPS', 'ITW', 'CDNS', 'EOG', 'MO', 'CB', 'BDX', 'MAR', 'SLB', 'CME', 'APH', 'SHW', 'KLAC', 'MCD', 'MMM', 'ABNB', 'ORLY', 'AIG', 'TRV', 'MET', 'AON', 'D', 'SO', 'DUK', 'NEE', 'AEP', 'O', 'PSA', 'VICI', 'EQIX', 'DLR', 'WELL', 'AVB', 'SPG', 'KMI', 'WMB', 'OKE', 'HAL', 'BKR', 'DVN', 'FANG', 'CTRA', 'MPC', 'VLO', 'PSX'
    ]
    
    nasdaq100 = [
        'AAPL', 'MSFT', 'AMZN', 'NVDA', 'META', 'GOOGL', 'GOOG', 'TSLA', 'AVGO', 'COST', 'PEP', 'ADBE', 'LIN', 'CSCO', 'TMUS', 'INTU', 'QCOM', 'AMD', 'AMGN', 'ISRG', 'TXN', 'HON', 'AMAT', 'BKNG', 'VRTX', 'ADI', 'ADP', 'LRCX', 'PANW', 'MU', 'MDLZ', 'REGN', 'SNPS', 'INTC', 'CDNS', 'KLAC', 'MELI', 'PYPL', 'MAR', 'ASML', 'CSX', 'CTAS', 'MNST', 'ORLY', 'WDAY', 'ROP', 'ADSK', 'PCAR', 'LULU', 'CPRT', 'NXPI', 'PAYX', 'ROST', 'TEAM', 'IDXX', 'AEP', 'KDP', 'FAST', 'ODFL', 'AZO', 'BKR', 'GEHC', 'DXCM', 'EXC', 'MRVL', 'CTSH', 'XEL', 'MCHP', 'ADX', 'ANSS', 'DLTR', 'WBD', 'ILMN', 'TTD', 'WBA', 'GFS', 'MDB', 'ON', 'CDW', 'ZS', 'DDOG', 'BIIB', 'ENPH', 'EBAY'
    ]
    
    aristocrats = [
        'NOBL', 'GPC', 'DOV', 'EMR', 'PH', 'GWW', 'MMM', 'PG', 'KO', 'JNJ', 'LOW', 'TGT', 'ABBV', 'ABT', 'ADP', 'AFL', 'ALB', 'AOS', 'APD', 'ATO', 'BEN', 'BDX', 'CAH', 'CAT', 'CB', 'CHRW', 'CL', 'CLX', 'CINF', 'CTAS', 'CVX', 'ECL', 'ED', 'ESS', 'EXPD', 'FRT', 'GD', 'HRL', 'ITW', 'KMB', 'LEG', 'LIN', 'MCD', 'MDT', 'MKC', 'NEU', 'NUE', 'O', 'PEP', 'PNR', 'PPG', 'ROP', 'SHW', 'SJW', 'SPGI', 'SWK', 'SYY', 'T', 'TROW', 'VFC', 'WMT', 'XOM'
    ]

    # Unione e rimozione duplicati
    all_tickers = list(set(sp500 + nasdaq100 + aristocrats))
    
    # Creazione DataFrame etichettato
    df_list = []
    for t in all_tickers:
        tags = []
        if t in sp500: tags.append("S&P 500")
        if t in nasdaq100: tags.append("Nasdaq 100")
        if t in aristocrats: tags.append("Aristocrats")
        
        df_list.append({
            'Ticker': t,
            'Indici': ", ".join(tags)
        })
    
    return pd.DataFrame(df_list).sort_values('Ticker')

# --- 2. LOGICA DI ANALISI ---
def analyze_stock(hist, price):
    if len(hist) < 20: return None
    support = hist['Low'].tail(20).min()
    dist_supp = ((price - support) / support) * 100
    std_dev = hist['Close'].pct_change().dropna().std()
    vol_monthly = (std_dev * (21**0.5)) * 100
    strike = round((price * (1 - std_dev)) * 2) / 2
    est_premium = (price * (vol_monthly / 100)) * 0.25
    profit_ratio = (est_premium / (strike * 100)) * 100 
    return {
        "supp": round(support, 2), "dist_supp": round(dist_supp, 2),
        "strike": strike, "vol": round(vol_monthly, 2),
        "profit": round(profit_ratio * 10, 2)
    }

# --- 3. INTERFACCIA ---
st.title("🚀 Wheel Strategy MEGA Scanner")
db = get_massive_stock_list()

st.sidebar.header("⚙️ Filtri Scanner")
selected_indices = st.sidebar.multiselect(
    "Filtra per Indice", 
    ["S&P 500", "Nasdaq 100", "Aristocrats"], 
    default=["S&P 500", "Nasdaq 100", "Aristocrats"]
)

price_range = st.sidebar.slider("Prezzo ($)", 0, 1500, (10, 800))
min_profit = st.sidebar.number_input("Profitto Min % (Mese)", value=1.2)
max_dist = st.sidebar.slider("Distanza Max Supporto %", 0.0, 40.0, 12.0)

# Filtraggio lista basato sulla sidebar
mask = db['Indici'].apply(lambda x: any(idx in x for idx in selected_indices))
final_list = db[mask]

st.info(f"Pronto a scansionare **{len(final_list)}** titoli selezionati.")

# --- 4. MOTORE DI SCANSIONE ---
if st.button('🔥 AVVIA SCANSIONE MASSIVA'):
    results = []
    progress_bar = st.progress(0)
    status_bar = st.empty()
    
    # Processiamo i titoli a blocchi per evitare timeout
    for i, row in enumerate(final_list.itertuples()):
        symbol = row.Ticker
        status_bar.text(f"Analisi {i+1}/{len(final_list)}: {symbol}")
        
        try:
            t = yf.Ticker(symbol)
            # Chiediamo solo i dati strettamente necessari (1 mese) per velocità
            h = t.history(period="1mo")
            
            if not h.empty:
                cp = h['Close'].iloc[-1]
                
                if price_range[0] <= cp <= price_range[1]:
                    data = analyze_stock(h, cp)
                    
                    if data and data['profit'] >= min_profit and data['dist_supp'] <= max_dist:
                        results.append({
                            "Ticker": symbol,
                            "Indici": row.Indici,
                            "Prezzo": round(cp, 2),
                            "Profit/Mese %": data['profit'],
                            "Strike": data['strike'],
                            "Dist. Supp %": data['dist_supp'],
                            "Volatilità %": data['vol']
                        })
            
            # Delay minimo per non farsi bannare da Yahoo
            if i % 10 == 0: time.sleep(0.1)
            
        except:
            continue
            
        progress_bar.progress((i + 1) / len(final_list))

    status_bar.empty()

    if results:
        df_res = pd.DataFrame(results)
        st.success(f"Trovate {len(df_res)} opportunità su {len(final_list)} titoli!")
        st.dataframe(df_res.style.background_gradient(subset=['Profit/Mese %'], cmap='Greens'), use_container_width=True)
        
        fig = px.scatter(df_res, x="Dist. Supp %", y="Profit/Mese %", text="Ticker", 
                         size="Volatilità %", color="Profit/Mese %",
                         title="Mappa Opportunità: Alto Rendimento vs Vicinanza Minimi")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("Nessun titolo trovato. Prova ad aumentare la 'Distanza Max Supporto' o a ridurre il 'Profitto Min'.")
