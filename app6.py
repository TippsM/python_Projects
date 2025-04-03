import streamlit as st
import requests

st.title("Currency Monitoring")
st.subheader("Find the latest crypto price update")

crypto = st.selectbox("Choose a cryptocurrency",
                      options=["", "Bitcoin", "Ethereum", "Litecoin"])

if crypto == "Bitcoin":
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms"