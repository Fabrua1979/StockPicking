import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime
import time
import plotly.express as px

st.set_page_config(page_title="Wheel Strategy - Full Scanner", layout="wide")

# --- 1. DATABASE INTEGRALE (Tutti gli indici combinati) ---
@st.cache_data
def get_ultimate_list():
    # Lista espansa per coprire S&P 500, Nasdaq 100, Dow e Aristocrats
    stocks = [
        'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'TSLA', 'NVDA', 'BRK-B', 'JPM', 'V', 'MA', 'AVGO', 'HD', 'PG', 'COST', 'JNJ', 'LLY', 'MRK', 'ABBV', 'CVX', 'XOM', 'PEP', 'KO', 'WMT', 'TMO', 'ADBE', 'CRM', 'ORCL', 'NFLX', 'AMD', 'INTC', 'CSCO', 'TXN', 'QCOM', 'AMAT', 'MU', 'DIS', 'NKE', 'PFE', 'T', 'VZ', 'BA', 'GE', 'HON', 'UPS', 'CAT', 'DE', 'PLTR', 'BABA', 'PYPL', 'ABNB', 'UBER', 'SNOW', 'SHOP', 'SQ', 'COIN', 'MSTR', 'MARA', 'RIOT', 'HOOD', 'LCID', 'RIVN', 'NIO', 'XPEV', 'LI', 'PINS', 'SNAP', 'ROKU', 'U', 'DKNG', 'PENN', 'ZM', 'DOCU', 'ETSY', 'SE', 'MELI', 'JD', 'PDD', 'BIDU', 'TME', 'FCX', 'AA', 'CLF', 'NUE', 'X', 'VALE', 'GOLD', 'NEM', 'F', 'GM', 'DAL', 'AAL', 'UAL', 'LUV', 'CCL', 'RCL', 'NCLH', 'BX', 'KKR', 'APO', 'WFC', 'BAC', 'GS', 'MS', 'C', 'AXP', 'BLK', 'SCHW', 'PGR', 'CB', 'MMC', 'AON', 'TRV', 'MET', 'PRU', 'AIG', 'LMT', 'RTX', 'GD', 'NOC', 'AMT', 'PLD', 'CCI', 'EQIX', 'DLR', 'PSA', 'O', 'VICI', 'WY', 'SBAC', 'LOW', 'TGT', 'TJX', 'ORLY', 'AZO', 'TSCO', 'MAR', 'HLT', 'YUM', 'DRI', 'CMG', 'SBUX', 'BKNG', 'EXPE', 'STLA', 'TM', 'HMC', 'EBAY', 'STT', 'BK', 'IBKR', 'RJF', 'LPLA', 'ALL', 'AFL', 'AJG', 'WTW', 'WELL', 'AVB', 'EQR', 'ARE', 'VRE', 'CPT', 'MAA', 'UDR', 'ESS', 'INVH', 'AMH', 'SUI', 'ELS', 'FRT', 'REG', 'KIM', 'BRX', 'SPG', 'TCO', 'MAC', 'PEAK', 'DOC', 'HR', 'OHI', 'VTR', 'HST', 'PK', 'BXP', 'SLG', 'FDX', 'WM', 'RSG', 'NSC', 'UNP', 'CSX', 'ETN', 'PH', 'ITW', 'EMR', 'ROP', 'AME', 'DOV', 'XYL', 'JCI', 'TT', 'CARR', 'OTIS', 'PAYX', 'FAST', 'URI', 'GWW', 'FERG', 'INTU', 'NOW', 'TEAM', 'WDAY', 'PANW', 'FTNT', 'CRWD', 'DDOG', 'ZS', 'OKTA', 'NET', 'MDB', 'LRCX', 'KLAC', 'ASML', 'TSM', 'SNPS', 'CDNS', 'ANSS', 'MSI', 'APH', 'TEL', 'KEYS', 'TER', 'QRVO', 'SWKS', 'ADI', 'NXPI', 'ON', 'MCHP', 'STX', 'WDC', 'HPQ', 'DELL', 'NTAP', 'PSTG', 'VRSN', 'AKAM', 'FSLR', 'ENPH', 'SEDG', 'LIN', 'TMUS', 'AMGN', 'GILD', 'VRTX', 'REGN', 'DXCM', 'ADSK', 'IDXX', 'CTAS', 'PCAR', 'LULU', 'CPRT', 'ROST', 'ODFL', 'AEP', 'BKR', 'KDP', 'MNST', 'KHC', 'CTSH', 'CSGP', 'ZSC', 'PDD', 'SGEN', 'MCD', 'DIS', 'VZ', 'WBA', 'IBM', 'DOW', 'CSX', 'NSC', 'UNP', 'KMI', 'WMB', 'OKE', 'HAL', 'SLB', 'BKR', 'PSX', 'MPC', 'VLO', 'COP', 'EOG', 'PXD', 'DVN', 'CLR', 'HES', 'APA', 'MRO', 'FANG', 'CTRA', 'EQT', 'RRC', 'SWN'
    ]
    return sorted(list(set(stocks)))

# --- 2. CALCOLI FINANZIARI ---
def analyze_stock(ticker_obj, price):
    hist = ticker_obj.history(period="3mo")
    if hist.empty: return None
    
    # Supporto e Volatilità
    support = hist['Low'].tail(20).min()
    dist_supp = ((price - support) / support) * 100
    std_dev = hist['Close'].pct_change().dropna().std()
    vol_monthly = (std_dev * (21**0.5)) * 100
    
    # Strike Suggerito (1 Deviazione Standard)
    strike = round((price * (1 - std_dev)) * 2) / 2
    
    # PROFIT RATIO (Rendimento stimato sul capitale impegnato per 30 giorni)
    # Stima del premio: Price * Vol_Mensile * 0.2 (costante approssimativa per Delta 0.20)
    est_premium = (price * (vol_monthly / 100)) * 0.25
    profit_ratio = (est_premium / (strike * 100)) * 100 
    
    return {
        "supp": round(support, 2), "dist_supp": round(dist_supp, 2),
        "strike": strike, "vol": round(vol_monthly, 2),
        "profit": round(profit_ratio * 10, 2) # Mensilizzato
    }

# --- 3. SIDEBAR ---
st.sidebar.header("⚙️ Parametri Strategia")
price_range = st.sidebar.slider("Prezzo ($)", 0, 1000, (10, 400))
min_profit = st.sidebar.number_input("Profit Ratio Min (Mese %)", value=1.5)
max_dist_supp = st.sidebar.slider("Vicinanza Supporto Max (%)", 0.0, 15.0, 5.0)
limit = st.sidebar.number_input("Numero titoli da scansionare", value=150)

st.title("🎯 Wheel Strategy PRO Scanner")
st.caption("Analisi integrata: S&P 500, Nasdaq, Dow Jones e Aristocrats.")

# --- 4. SCANSIONE ---
if st.button('🚀 AVVIA ANALISI TOTALE'):
    all_tickers = get_ultimate_list()
    tickers_to_scan = all_tickers[:int(limit)]
    results = []
    progress_bar = st.progress(0)
    
    for i, symbol in enumerate(tickers_to_scan):
        try:
            t = yf.Ticker(symbol.replace('.', '-'))
            info = t.info
            p = info.get('currentPrice')
            
            if p and price_range[0] <= p <= price_range[1]:
                data = analyze_stock(t, p)
                if data and data['profit'] >= min_profit and data['dist_supp'] <= max_dist_supp:
                    
                    # Controllo Earnings
                    cal = t.calendar
                    risk = "OK"
                    if cal is not None and not cal.empty:
                        if (cal.iloc[0,0] - datetime.now().date()).days <= 7: risk = "⚠️"

                    results.append({
                        "Ticker": symbol, "Prezzo": p, "Volat. %": data['vol'],
                        "Profit/Mese %": data['profit'], "Strike (1-SD)": data['strike'],
                        "Supporto": data['supp'], "Dist. Supp %": data['dist_supp'],
                        "Rischio": risk, "P/E": info.get('trailingPE', 0)
                    })
            time.sleep(0.05)
        except: continue
        progress_bar.progress((i + 1) / len(tickers_to_scan))

    if results:
        df = pd.DataFrame(results)
        st.success(f"Trovate {len(results)} opportunità ideali!")
        
        # Tabella con Stile
        st.dataframe(df.style.background_gradient(subset=['Profit/Mese %'], cmap='Greens')
                              .background_gradient(subset=['Dist. Supp %'], cmap='RdYlGn_r')
                              .format({'Prezzo': '{:.2f}$', 'Profit/Mese %': '{:.2f}%'}),
                     use_container_width=True)
        
        # --- 5. GRAFICO RISCHIO/RENDIMENTO ---
        st.write("### 📈 Mappa Opportunità (Rendimento vs Vicinanza Supporto)")
        fig = px.scatter(df, x="Dist. Supp %", y="Profit/Mese %", text="Ticker", 
                         size="Volat. %", color="Profit/Mese %",
                         labels={"Dist. Supp %": "Distanza dal Supporto (Più basso = meno rischio)",
                                 "Profit/Mese %": "Rendimento Stimato %"},
                         title="I titoli in alto a sinistra sono i migliori (Alto rendimento, vicino al supporto)")
        st.plotly_chart(fig, use_container_width=True)
        
    else:
        st.warning("Nessun titolo trovato. Prova ad aumentare la 'Vicinanza Supporto' nella sidebar.")
