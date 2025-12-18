import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime
import time
import io

st.set_page_config(page_title="Wheel Strategy Ultimate", layout="wide")

# --- 1. DATABASE TITOLI HARDCODED (Indistruttibile) ---
@st.cache_data
def get_static_tickers():
    return {
        "S&P 500 (Tutti)": [
            'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'TSLA', 'NVDA', 'BRK-B', 'JPM', 'V', 'MA', 'AVGO', 'HD', 'PG', 'COST', 'JNJ', 'LLY', 'MRK', 'ABBV', 'CVX', 'XOM', 'PEP', 'KO', 'WMT', 'TMO', 'ADBE', 'CRM', 'ORCL', 'NFLX', 'AMD', 'INTC', 'CSCO', 'TXN', 'QCOM', 'AMAT', 'MU', 'DIS', 'NKE', 'PFE', 'T', 'VZ', 'BA', 'GE', 'HON', 'UPS', 'CAT', 'DE', 'PLTR', 'BABA', 'PYPL', 'ABNB', 'UBER', 'SNOW', 'SHOP', 'SQ', 'COIN', 'MSTR', 'MARA', 'RIOT', 'HOOD', 'LCID', 'RIVN', 'NIO', 'XPEV', 'LI', 'PINS', 'SNAP', 'ROKU', 'U', 'DKNG', 'PENN', 'ZM', 'DOCU', 'ETSY', 'SE', 'MELI', 'JD', 'PDD', 'BIDU', 'TME', 'FCX', 'AA', 'CLF', 'NUE', 'X', 'VALE', 'GOLD', 'NEM', 'F', 'GM', 'DAL', 'AAL', 'UAL', 'LUV', 'CCL', 'RCL', 'NCLH', 'BX', 'KKR', 'APO', 'WFC', 'BAC', 'GS', 'MS', 'C', 'AXP', 'BLK', 'SCHW', 'PGR', 'CB', 'MMC', 'AON', 'TRV', 'MET', 'PRU', 'AIG', 'LMT', 'RTX', 'GD', 'NOC', 'AMT', 'PLD', 'CCI', 'EQIX', 'DLR', 'PSA', 'O', 'VICI', 'WY', 'SBAC', 'LOW', 'TGT', 'COST', 'WMT', 'HD', 'TJX', 'ORLY', 'AZO', 'TSCO', 'MAR', 'HLT', 'YUM', 'DRI', 'CMG', 'SBUX', 'NKE', 'F', 'GM', 'HMC', 'TM', 'STLA', 'TSLA', 'AMZN', 'EBAY', 'ETSY', 'BKNG', 'EXPE', 'ABNB', 'V', 'MA', 'AXP', 'PYPL', 'SQ', 'COIN', 'HOOD', 'JPM', 'BAC', 'WFC', 'C', 'GS', 'MS', 'BLK', 'STT', 'BK', 'SCHW', 'IBKR', 'RJF', 'LPLA', 'PGR', 'CB', 'TRV', 'ALL', 'MET', 'PRU', 'AFL', 'AIG', 'MMC', 'AON', 'AJG', 'WTW', 'PLD', 'AMT', 'CCI', 'EQIX', 'DLR', 'PSA', 'O', 'VICI', 'WY', 'SBAC', 'WELL', 'DRE', 'AVB', 'EQR', 'ARE', 'VRE', 'CPT', 'MAA', 'UDR', 'ESS', 'INVH', 'AMH', 'SUI', 'ELS', 'FRT', 'REG', 'KIM', 'BRX', 'SPG', 'TCO', 'MAC', 'PEAK', 'DOC', 'HR', 'OHI', 'VTR', 'HST', 'PK', 'BXP', 'SLG', 'DE', 'CAT', 'LMT', 'RTX', 'GD', 'NOC', 'BA', 'GE', 'HON', 'UPS', 'FDX', 'WM', 'RSG', 'NSC', 'UNP', 'CSX', 'ETN', 'PH', 'ITW', 'EMR', 'ROP', 'AME', 'DOV', 'XYL', 'JCI', 'TT', 'CARR', 'OTIS', 'PAYX', 'FAST', 'URI', 'GWW', 'FERG', 'ADBE', 'ORCL', 'CRM', 'INTU', 'NOW', 'SNOW', 'TEAM', 'WDAY', 'PANW', 'FTNT', 'CRWD', 'DDOG', 'ZS', 'OKTA', 'NET', 'MDB', 'SHOP', 'SQ', 'PYPL', 'V', 'MA', 'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'NVDA', 'AVGO', 'CSCO', 'ADBE', 'CRM', 'TXN', 'QCOM', 'INTC', 'AMD', 'AMAT', 'MU', 'LRCX', 'KLAC', 'ASML', 'TSM', 'SNPS', 'CDNS', 'ANSS', 'MSI', 'APH', 'TEL', 'KEYS', 'TER', 'QRVO', 'SWKS', 'ADI', 'NXPI', 'ON', 'MCHP', 'STX', 'WDC', 'HPQ', 'DELL', 'NTAP', 'PSTG', 'VRSN', 'AKAM', 'FSLR', 'ENPH', 'SEDG', 'SPWR'
        ],
        "Nasdaq-100 (Tech Focus)": ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'TSLA', 'NVDA', 'AVGO', 'COST', 'ADBE', 'AZO', 'CSCO', 'PEP', 'LIN', 'AMD', 'TMUS', 'INTC', 'TXN', 'AMAT', 'QCOM', 'ISRG', 'HON', 'INTU', 'BKNG', 'AMGN', 'SBUX', 'MDLZ', 'ADP', 'GILD', 'ADI', 'LRCX', 'VRTX', 'REGN', 'PANW', 'SNPS', 'KLAC', 'MELI', 'CDNS', 'PYPL', 'CSX', 'ASML', 'MAR', 'ORLY', 'MNST', 'KDP', 'MNST', 'KHC', 'DXCM', 'ADSK', 'IDXX', 'CTAS', 'PCAR', 'LULU', 'CPRT', 'MCHP', 'PAYX', 'ROST', 'ODFL', 'AEP', 'TEAM', 'FAST', 'BKR', 'KDP', 'EBAY', 'JD', 'WDAY', 'ALGN', 'ZM', 'MRVL', 'DDOG', 'ANSS', 'VRSN', 'EXC', 'CTSH', 'CSGP', 'OKTA', 'SPLK', 'DOCU', 'ZSC', 'FTNT', 'PDD', 'SGEN', 'IDXX', 'LCID', 'RIVN'],
        "Dow Jones 30": ['BA', 'UNH', 'GS', 'HD', 'MSFT', 'V', 'MCD', 'CAT', 'CRM', 'HON', 'AAPL', 'AXP', 'TRV', 'CVX', 'JNJ', 'JPM', 'NKE', 'PG', 'MMM', 'IBM', 'DIS', 'AMGN', 'VZ', 'WBA', 'WMT', 'KO', 'DOW', 'CSCO', 'INTC', 'MRK'],
        "Dividend Aristocrats": ['KO', 'PEP', 'PG', 'JNJ', 'MMM', 'T', 'LOW', 'TGT', 'CVX', 'XOM', 'ABBV', 'ABT', 'BEN', 'ED', 'GPC', 'ITW', 'KMB', 'LEG', 'NOA', 'SHW', 'SYY', 'TROW', 'VFC', 'WMT']
    }

# --- 2. LOGICA TECNICA ---
def get_technical_data(ticker_obj, price):
    hist = ticker_obj.history(period="3mo")
    if hist.empty: return None
    
    # Supporto (Minimo 20gg)
    support = hist['Low'].tail(20).min()
    dist_supp = ((price - support) / support) * 100
    
    # Volatilità Statistica
    log_returns = hist['Close'].pct_change().dropna()
    std_dev = log_returns.std()
    
    # Strike 1 Deviazione Standard (circa Delta 0.16)
    strike_sd = price * (1 - std_dev)
    
    return {
        "support": round(support, 2),
        "dist_supp": round(dist_supp, 2),
        "strike": round(strike_sd * 2) / 2,
        "vol": round((std_dev * (21**0.5)) * 100, 2)
    }

# --- 3. SIDEBAR ---
st.sidebar.header("⚙️ Configurazione")
indices = get_static_tickers()
selected_index = st.sidebar.selectbox("Indice di riferimento", list(indices.keys()))
price_min = st.sidebar.number_input("Prezzo Min ($)", value=10)
price_max = st.sidebar.number_input("Prezzo Max ($)", value=1000)
pe_max = st.sidebar.number_input("P/E Massimo (0 = OFF)", value=0)
vol_min = st.sidebar.slider("Volatilità Min (%)", 0.0, 15.0, 1.0)
supp_prox = st.sidebar.slider("Vicinanza Supporto Max (%)", 0.0, 10.0, 5.0)

st.title("🎯 Wheel Strategy Pro: Scanner Integrale")
st.caption(f"Database statico attivo: {len(indices[selected_index])} titoli caricati.")

# --- 4. SCANSIONE ---
if st.button('🚀 AVVIA SCANSIONE ORA'):
    tickers = indices[selected_index]
    results = []
    progress_bar = st.progress(0)
    
    for i, symbol in enumerate(tickers):
        try:
            t = yf.Ticker(symbol)
            info = t.info
            p = info.get('currentPrice')
            
            if p and price_min <= p <= price_max:
                pe = info.get('trailingPE', 0)
                if pe_max == 0 or (0 < pe <= pe_max):
                    
                    data = get_technical_data(t, p)
                    if data and data['vol'] >= vol_min:
                        # Filtro Prossimità Supporto
                        if data['dist_supp'] <= supp_prox:
                            
                            # Controllo Earnings
                            earnings = "N/A"
                            is_earning_risk = False
                            cal = t.calendar
                            if cal is not None and not cal.empty:
                                next_e = cal.iloc[0, 0]
                                earnings = next_e.strftime('%Y-%m-%d')
                                if (next_e - datetime.now().date()).days <= 7:
                                    is_earning_risk = True

                            results.append({
                                "Ticker": symbol,
                                "Prezzo": p,
                                "P/E": round(pe, 1) if pe > 0 else "N/A",
                                "Volat. %": data['vol'],
                                "Strike Stat. (1-SD)": data['strike'],
                                "Supporto (20d)": data['support'],
                                "Dist. Supp. %": data['dist_supp'],
                                "Earnings": earnings,
                                "Risk": "⚠️" if is_earning_risk else "OK",
                                "Div. %": round(info.get('dividendYield', 0) * 100, 2)
                            })
            time.sleep(0.05)
        except: continue
        progress_bar.progress((i + 1) / len(tickers))

    if results:
        df = pd.DataFrame(results)
        st.success(f"Trovate {len(results)} opportunità su {len(tickers)} titoli.")
        
        # Colorazione Earnings e Dist. Supporto
        st.dataframe(df.style.applymap(lambda x: 'color: red' if x == "⚠️" else 'color: green', subset=['Risk'])
                              .background_gradient(subset=['Dist. Supp. %'], cmap='YlGn_r')
                              .background_gradient(subset=['Volat. %'], cmap='Oranges')
                              .format({'Prezzo': '{:.2f}$', 'Strike Stat. (1-SD)': '{:.2f}$', 'Supporto (20d)': '{:.2f}$'}),
                     use_container_width=True)
    else:
        st.warning("Nessun titolo trovato. Prova ad aumentare il 'Range Prezzo' o la 'Vicinanza Supporto'.")
