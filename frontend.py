# frontend.py
import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

st.title("Pokémon Stats Explorer")

option = st.sidebar.selectbox("Choose Action", ["Search Pokémon", "Top Pokémon by Stat"])

if option == "Search Pokémon":
    name = st.text_input("Enter Pokémon Name")
    if st.button("Search"):
        res = requests.get(f"{API_URL}/pokemon/{name}").json()
        st.json(res)

elif option == "Top Pokémon by Stat":
    stat = st.selectbox("Select Stat", ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"])
    n = st.slider("Number of Pokémon", 5, 20, 10)
    if st.button("Get Top Pokémon"):
        res = requests.get(f"{API_URL}/top/{stat}/{n}").json()
        df = pd.DataFrame(res)
        st.dataframe(df)
        st.bar_chart(df.set_index("Name"))
