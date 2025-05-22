# app.py
import streamlit as st
from player_compare import show_player_comparison
from prediction_tab import show_predictions

st.set_page_config(page_title="NBA Intelligence Suite", layout="wide")
st.title("🏀 NBA Player Intelligence Suite")

# Tabs
tab1, tab2 = st.tabs(["📊 Compare Players", "🔮 Predict Stats"])

with tab1:
    show_player_comparison()

with tab2:
    show_predictions()
