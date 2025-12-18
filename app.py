import streamlit as st
import requests

st.title("🧪 Test Connessione API")

# La tua chiave
key = "sQJgPn10EvTF6U4HzkVRukBF0Y0ijMrL"

if st.button('VERIFICA CHIAVE ORA'):
    # Proviamo a scaricare solo il profilo di Apple
    url = f"https://financialmodelingprep.com/api/v3/profile/AAPL?apikey={key}"
    
    st.info(f"Tentativo di connessione con chiave: {key[:5]}...")
    
    try:
        r = requests.get(url)
        data = r.json()
        
        if r.status_code == 200 and data:
            st.success("✅ CONNESSIONE RIUSCITA!")
            st.write(f"Prezzo attuale Apple: {data[0].get('price')}$")
        else:
            st.error(f"❌ Errore Server: {r.status_code}")
            st.write("Il server ha risposto ma non ha dato dati. Verifica l'email di conferma.")
    except Exception as e:
        st.error(f"💥 Errore di Rete: {e}")
