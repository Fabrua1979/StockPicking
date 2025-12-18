import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime
import time
import io
import plotly.express as px

st.set_page_config(page_title="USA Options Wheel Scanner", layout="wide")

# --- 1. DATABASE COMPLETO USA ---
@st.cache_data
def get_massive_usa_list():
    # Database esteso (Puoi aggiungere altri 1000 ticker qui sotto)
    nasdaq_100 = ['AAPL', 'MSFT', 'AMZN', 'NVDA', 'META', 'GOOGL', 'TSLA', 'AVGO', 'COST', 'ADBE', 'LIN', 'CSCO', 'TMUS', 'INTU', 'QCOM', 'AMD', 'AMGN', 'ISRG', 'TXN', 'HON', 'AMAT', 'BKNG', 'VRTX', 'ADI', 'ADP', 'LRCX', 'PANW', 'MU', 'MDLZ', 'REGN', 'SNPS', 'INTC', 'CDNS', 'KLAC', 'MELI', 'PYPL', 'MAR', 'ASML', 'CSX', 'CTAS', 'MNST', 'ORLY', 'WDAY', 'ROP', 'ADSK', 'PCAR', 'LULU', 'CPRT', 'NXPI', 'PAYX', 'ROST', 'TEAM', 'IDXX', 'AEP', 'KDP', 'FAST', 'ODFL', 'AZO', 'BKR', 'GEHC', 'DXCM', 'EXC', 'MRVL', 'CTSH', 'XEL', 'MCHP', 'ANSS', 'DLTR', 'WBD', 'ILMN', 'TTD', 'WBA', 'GFS', 'MDB', 'ON', 'CDW', 'ZS', 'DDOG', 'BIIB', 'ENPH', 'EBAY']
    sp500_others = ['JPM', 'V', 'MA', 'UNH', 'PG', 'XOM', 'HD', 'JNJ', 'ORCL', 'MRK', 'ABBV', 'CVX', 'CRM', 'WMT', 'KO', 'BAC', 'ACN', 'TMO', 'ABT', 'CAT', 'VZ', 'AXP', 'PFE', 'IBM', 'MS', 'GE', 'PM', 'UNP', 'HON', 'GS', 'LOW', 'SPGI', 'RTX', 'SYK', 'LMT', 'ELV', 'DE', 'TJX', 'COP', 'BLK', 'ETN', 'PGR', 'CVS', 'MMC', 'CI', 'BSX', 'SCHW', 'T', 'ZTS', 'WM', 'C', 'FI', 'BA', 'PLD', 'GILD', 'UPS', 'ITW', 'EOG', 'MO', 'CB', 'BDX', 'SLB', 'CME', 'APH', 'SHW', 'MCD', 'MMM', 'ABNB', 'AIG', 'TRV', 'MET', 'AON', 'D', 'SO', 'DUK', 'NEE', 'PSA', 'VICI', 'EQIX', 'DLR', 'WELL', 'AVB', 'SPG', 'KMI', 'WMB', 'OKE', 'HAL', 'DVN', 'FANG', 'CTRA', 'MPC', 'VLO', 'PSX', 'PLTR', 'UBER', 'SNOW', 'SQ', 'PARA', 'SNAP', 'PINS', 'ROKU', 'ZM', 'DOCU', 'ETSY', 'SHOP', 'SE', 'BABA', 'JD', 'BIDU', 'TME', 'FCX', 'AA', 'CLF', 'NUE', 'X', 'VALE', 'GOLD', 'NEM', 'F', 'GM', 'DAL', 'AAL', 'UAL', 'LUV', 'CCL', 'RCL', 'NCLH', 'BX', 'KKR', 'APO', 'WFC', 'STT', 'BK', 'IBKR', 'RJF', 'LPLA', 'ALL', 'AFL', 'AJG', 'WTW', 'EQR', 'ARE', 'VRE', 'CPT', 'MAA', 'UDR', 'ESS', 'INVH', 'AMH', 'SUI', 'ELS', 'FRT', 'REG', 'KIM', 'BRX', 'TCO', 'MAC', 'PEAK', 'DOC', 'HR', 'OHI', 'VTR', 'HST', 'PK', 'BXP', 'SLG', 'FDX', 'RSG', 'NSC', 'AME', 'DOV', 'XYL', 'JCI', 'TT', 'CARR', 'OTIS', 'URI', 'GWW', 'FERG', 'NOW', 'CRWD', 'OKTA', 'NET', 'TSM', 'MSI', 'TEL', 'KEYS', 'TER', 'QRVO', 'SWKS', 'STX', 'WDC', 'HPQ', 'DELL', 'NTAP', 'PSTG', 'VRSN', 'AKAM', 'FSLR', 'SEDG']
    
    return sorted(list(set(nasdaq_100 + sp500_others)))

# --- 2. LOGICA ANALISI ---
def analyze_stock(t_obj, hist):
    try:
        if not t_obj.options: return None
        cp = hist['Close'].iloc[-1]
        info = t_obj.info
        std_dev = hist['Close'].pct_change().dropna().std()
        vol_month = std_dev * (21**0.5)
        strike = round(cp * (1 - vol_month) * 2) / 2
        profit_month = ((cp * vol_month * 0.25) / strike) * 100
        earn_alert = "OK"
        try:
            cal = t_obj.calendar
            if cal is not None and not cal.empty:
                if (cal.iloc[0,0] - datetime.now().date()).days <= 7: earn_alert = "⚠️"
        except: pass

        return {
            "Prezzo": round(cp, 2),
            "P/E": info.get('trailingPE', 0),
            "Settore": info.get('sector', 'N/D'),
            "Profit/Mese %": round(profit_month * 10, 2),
            "Strike Consigliato": strike,
            "Distanza Supp %": round(((cp - hist['Low'].tail(20).min()) / cp) * 100, 2),
            "Earnings": earn_alert,
            "Volatilità %": round(vol_month * 100, 2)
        }
    except: return None

# --- 3. INTERFACCIA ---
st.title("🛡️ USA Market Wheel Scanner")
usa_list = get_massive_usa_list()

if 'scan_results' not in st.session_state:
    st.session_state.scan_results = None

with st.sidebar:
    st.header("⚙️ Configurazione Scansione")
    scan_limit = st.number_input("Titoli da scansionare", 10, len(usa_list), 300)
    st.caption("Nota: Scansionare molti titoli può richiedere tempo.")

# --- 4. SCANSIONE ---
if st.button('🚀 AVVIA SCANSIONE TOTALE'):
    results = []
    progress = st.progress(0)
    status = st.empty()
    
    for i, sym in enumerate(usa_list[:scan_limit]):
        status.text(f"Analisi: {sym} ({i+1}/{scan_limit})")
        try:
            t = yf.Ticker(sym)
            h = t.history(period="1mo")
            if h.empty: continue
            data = analyze_stock(t, h)
            if data:
                data['Ticker'] = sym
                results.append(data)
            if i % 10 == 0: time.sleep(0.02)
        except: continue
        progress.progress((i + 1) / scan_limit)
    
    st.session_state.scan_results = pd.DataFrame(results)
    status.empty()

# --- 5. FILTRI DINAMICI SUI RISULTATI (Visualizzati solo se ci sono dati) ---
if st.session_state.scan_results is not None:
    df = st.session_state.scan_results.copy()
    
    st.divider()
    st.header("🎯 Filtra i Risultati della Tabella")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        f_price = st.slider("Filtra Prezzo", float(df['Prezzo'].min()), float(df['Prezzo'].max()), (float(df['Prezzo'].min()), float(df['Prezzo'].max())))
    with col2:
        f_profit = st.slider("Filtra Profit %", float(df['Profit/Mese %'].min()), float(df['Profit/Mese %'].max()), (0.5, float(df['Profit/Mese %'].max())))
    with col3:
        f_sector = st.multiselect("Filtra Settore", df['Settore'].unique(), default=df['Settore'].unique())
    with col4:
        f_earnings = st.checkbox("Nascondi ⚠️ (Earnings imminenti)")

    # Applicazione filtri
    df = df[(df['Prezzo'] >= f_price[0]) & (df['Prezzo'] <= f_price[1])]
    df = df[(df['Profit/Mese %'] >= f_profit[0]) & (df['Profit/Mese %'] <= f_profit[1])]
    df = df[df['Settore'].isin(f_sector)]
    if f_earnings:
        df = df[df['Earnings'] == "OK"]

    st.success(f"Visualizzati {len(df)} titoli filtrati.")

    # DOWNLOAD EXCEL
    output = io.BytesIO()
    try:
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Wheel_Report')
        st.download_button("📥 Scarica Report Excel", output.getvalue(), "wheel_report.xlsx")
    except:
        st.warning("Assicurati di aver aggiunto 'xlsxwriter' al file requirements.txt")

    # GRAFICO
    st.subheader("📈 Analisi Grafica Rischio/Rendimento")
    fig = px.scatter(df, x="Distanza Supporto %", y="Profit/Mese %", text="Ticker", 
                     size="Prezzo", color="Settore", hover_data=['Strike Consigliato', 'P/E'],
                     title="Ottimizzazione Wheel Strategy")
    st.plotly_chart(fig, use_container_width=True)

    # TABELLA FINALE
    st.dataframe(df.style.background_gradient(subset=['Profit/Mese %'], cmap='Greens')
                 .applymap(lambda x: 'background-color: #ff4b4b; color: white' if x == "⚠️" else '', subset=['Earnings'])
                 .format({'Prezzo': '{:.2f}$', 'Profit/Mese %': '{:.2f}%'}),
                 use_container_width=True)
