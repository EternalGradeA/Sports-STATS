# player_compare.py
import streamlit as st
import pandas as pd
from utils import get_player_id, get_player_stats, player_names

def show_player_comparison():
    st.header("📊 Compare Two Players")
    col1, col2 = st.columns(2)

    with col1:
        p1 = st.selectbox("Select Player 1", player_names, key="p1")
    with col2:
        p2 = st.selectbox("Select Player 2", player_names, key="p2")

    if p1 and p2:
        id1 = get_player_id(p1)
        id2 = get_player_id(p2)

        df1 = get_player_stats(id1)[['GAME_DATE', 'MATCHUP', 'PTS', 'AST', 'REB']].head(5)
        df2 = get_player_stats(id2)[['GAME_DATE', 'MATCHUP', 'PTS', 'AST', 'REB']].head(5)

        st.write(f"**{p1} - Last 5 Games**")
        st.dataframe(df1)

        st.write(f"**{p2} - Last 5 Games**")
        st.dataframe(df2)

        avg1 = df1[['PTS', 'AST', 'REB']].mean()
        avg2 = df2[['PTS', 'AST', 'REB']].mean()

        st.subheader("Average Comparison")
        st.dataframe(pd.DataFrame({p1: avg1, p2: avg2}))
