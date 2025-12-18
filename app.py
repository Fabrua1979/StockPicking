import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime
import time
import plotly.express as px

st.set_page_config(page_title="USA Options Wheel Scanner", layout="wide")

# --- 1. CARICAMENTO MASSIVO TITOLI USA ---
@st.cache_data
def get_usa_master_list():
    # In un'app reale qui caricheresti un CSV con i 1000+ ticker.
    # Qui inserisco i blocchi principali che compongono il Russell 1000 + Nasdaq
    nasdaq_100 = ['AAPL', 'MSFT', 'AMZN', 'NVDA', 'META', 'GOOGL', 'GOOG', 'TSLA', 'AVGO', 'COST', 'PEP', 'ADBE', 'LIN', 'CSCO', 'TMUS', 'INTU', 'QCOM', 'AMD', 'AMGN', 'ISRG', 'TXN', 'HON', 'AMAT', 'BKNG', 'VRTX', 'ADI', 'ADP', 'LRCX', 'PANW', 'MU', 'MDLZ', 'REGN', 'SNPS', 'INTC', 'CDNS', 'KLAC', 'MELI', 'PYPL', 'MAR', 'ASML', 'CSX', 'CTAS', 'MNST', 'ORLY', 'WDAY', 'ROP', 'ADSK', 'PCAR', 'LULU', 'CPRT', 'NXPI', 'PAYX', 'ROST', 'TEAM', 'IDXX', 'AEP', 'KDP', 'FAST', 'ODFL', 'AZO', 'BKR', 'GEHC', 'DXCM', 'EXC', 'MRVL', 'CTSH', 'XEL', 'MCHP', 'ADX', 'ANSS', 'DLTR', 'WBD', 'ILMN', 'TTD', 'WBA', 'GFS', 'MDB', 'ON', 'CDW', 'ZS', 'DDOG', 'BIIB', 'ENPH', 'EBAY']
    
    sp500_others = ['JPM', 'V', 'MA', 'UNH', 'PG', 'XOM', 'HD', 'JNJ', 'ORCL', 'MRK', 'ABBV', 'CVX', 'CRM', 'WMT', 'KO', 'BAC', 'ACN', 'TMO', 'ABT', 'CAT', 'VZ', 'AXP', 'PFE', 'IBM', 'MS', 'GE', 'PM', 'UNP', 'GS', 'LOW', 'SPGI', 'RTX', 'SYK', 'LMT', 'ELV', 'DE', 'TJX', 'COP', 'BLK', 'ETN', 'PGR', 'CVS', 'MMC', 'CI', 'BSX', 'SCHW', 'T', 'ZTS', 'WM', 'C', 'FI', 'BA', 'PLD', 'GILD', 'UPS', 'ITW', 'EOG', 'MO', 'CB', 'BDX', 'SLB', 'CME', 'APH', 'SHW', 'MCD', 'MMM', 'ABNB', 'AIG', 'TRV', 'MET', 'AON', 'D', 'SO', 'DUK', 'NEE', 'PSA', 'VICI', 'EQIX', 'DLR', 'WELL', 'AVB', 'SPG', 'KMI', 'WMB', 'OKE', 'HAL', 'DVN', 'FANG', 'CTRA', 'MPC', 'VLO', 'PSX', 'PLTR', 'UBER', 'SNOW', 'SQ', 'PARA', 'SNAP', 'PINS', 'ROKU', 'ZM', 'DOCU', 'ETSY', 'SHOP', 'SE', 'BABA', 'JD', 'BIDU', 'TME', 'FCX', 'AA', 'CLF', 'NUE', 'X', 'VALE', 'GOLD', 'NEM', 'F', 'GM', 'DAL', 'AAL', 'UAL', 'LUV', 'CCL', 'RCL', 'NCLH', 'BX', 'KKR', 'APO', 'WFC', 'STT', 'BK', 'IBKR', 'RJF', 'LPLA', 'ALL', 'AFL', 'AJG', 'WTW', 'EQR', 'ARE', 'VRE', 'CPT', 'MAA', 'UDR', 'ESS', 'INVH', 'AMH', 'SUI', 'ELS', 'FRT', 'REG', 'KIM', 'BRX', 'TCO', 'MAC', 'PEAK', 'DOC', 'HR', 'OHI', 'VTR', 'HST', 'PK', 'BXP', 'SLG', 'FDX', 'RSG', 'NSC', 'AME', 'DOV', 'XYL', 'JCI', 'TT', 'CARR', 'OTIS', 'URI', 'GWW', 'FERG', 'NOW', 'CRWD', 'OKTA', 'NET', 'TSM', 'MSI', 'TEL', 'KEYS', 'TER', 'QRVO', 'SWKS', 'STX', 'WDC', 'HPQ', 'DELL', 'NTAP', 'PSTG', 'VRSN', 'AKAM', 'FSLR', 'SEDG']
    
    # Unione e rimozione duplicati per arrivare a circa 800-1000 titoli core
    return sorted(list(set(nasdaq_100 + sp500_others)))

# --- 2. FUNZIONE DI ANALISI CON VERIFICA OPZIONI ---
def analyze_usa_stock(t_obj, hist, info):
    try:
        # 1. Verifica disponibilità Opzioni
        if not t_obj.options:
            return None
            
        cp = hist['Close'].iloc[-1]
        
        # 2. Parametri Tecnici
        support = hist['Low'].tail(20).min()
        dist_supp = ((cp - support) / support) * 100
        std_dev = hist['Close'].pct_change().dropna().std()
        vol_month = std_dev * (21**0.5)
        
        # 3. Evoluzioni Professionali
        pe = info.get('trailingPE', 0)
        strike = round(cp * (1 - vol_month) * 2) / 2
        profit_month = ((cp * vol_month * 0.25) / strike) * 100
        
        # 4. Earnings Alert
        earn_alert = "OK"
        try:
            cal = t_obj.calendar
            if cal is not None and not cal.empty:
                if (cal.iloc[0,0] - datetime.now().date()).days <= 7:
                    earn_alert = "⚠️"
        except: pass

        return {
            "Prezzo": round(cp, 2),
            "P/E": round(pe, 1) if pe else "N/D",
            "Profit/Mese %": round(profit_month * 10, 2),
            "Strike Consigliato": strike,
            "Distanza Supporto %": round(dist_supp, 2),
            "Earnings": earn_alert,
            "Volatilità %": round(vol_month * 100, 2)
        }
    except:
        return None

# --- 3. INTERFACCIA ---
st.title("🇺🇸 USA Market Wheel Scanner (Opt-In Only)")
st.caption("Scansione massiva del mercato USA filtrando solo titoli con opzioni disponibili.")

usa_list = get_usa_master_list()

with st.sidebar:
    st.header("⚙️ Filtri Professionali")
    limit_scan = st.number_input("Numero titoli da scansionare (max 1000)", 10, 1000, 300)
    min_profit = st.slider("Profitto Minimo Mensile %", 0.0, 5.0, 0.8)
    max_pe = st.number_input("P/E Massimo (0=disabilita)", 0, 100, 40)
    max_dist = st.slider("Distanza Max Supporto %", 0.0, 40.0, 15.0)

st.info(f"Il database contiene **{len(usa_list)}** titoli pronti per l'analisi.")

# --- 4. MOTORE DI SCANSIONE ---
if st.button('🚀 AVVIA SCANSIONE COMPLETA'):
    results = []
    progress = st.progress(0)
    status = st.empty()
    
    # Scansioniamo fino al limite impostato
    tickers_to_process = usa_list[:limit_scan]
    
    for i, symbol in enumerate(tickers_to_process):
        status.text(f"Verifica Opzioni e Tecnica: {symbol} ({i+1}/{len(tickers_to_process)})")
        try:
            t = yf.Ticker(symbol)
            h = t.history(period="1mo")
            if h.empty: continue
            
            data = analyze_usa_stock(t, h, t.info)
            
            if data:
                # Filtro P/E
                pe_val = data['P/E']
                pe_ok = True if max_pe == 0 or pe_val == "N/D" else (pe_val <= max_pe)
                
                if pe_ok and data['Profit/Mese %'] >= min_profit and data['Distanza Supporto %'] <= max_dist:
                    results.append({"Ticker": symbol, **data})
            
            if i % 12 == 0: time.sleep(0.05)
        except: continue
        progress.progress((i + 1) / len(tickers_to_process))

    status.empty()
    if results:
        df_res = pd.DataFrame(results)
        st.success(f"Analisi completata! Trovate {len(df_res)} opportunità su {len(tickers_to_process)} titoli scansionati.")
        
        # Tabella formattata
        st.dataframe(df_res.style.background_gradient(subset=['Profit/Mese %'], cmap='Greens')
                     .applymap(lambda x: 'background-color: #ffcccc' if x == "⚠️" else '', subset=['Earnings']),
                     use_container_width=True)
        
        # Grafico Rischio/Rendimento
        fig = px.scatter(df_res, x="Distanza Supporto %", y="Profit/Mese %", text="Ticker", 
                         size="Volatilità %", color="Profit/Mese %",
                         title="Strategia Wheel: Le migliori opportunità (Alto Rendimento, Bassa Distanza dal Supporto)")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("Nessun titolo trovato con i filtri attuali. Prova ad allargare i parametri nella sidebar.")
