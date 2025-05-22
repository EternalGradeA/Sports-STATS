# prediction_tab.py
import streamlit as st
from utils import get_player_id, get_player_stats, player_names, team_names, team_abbr_map
import pandas as pd

def show_predictions():
    st.header("🔮 Stat Predictor & Game Log Viewer")

    # Player & team selection
    player = st.selectbox("Select Player", player_names, key="predict_player")
    team = st.selectbox("Select Opponent Team", team_names, key="predict_team")

    # Game log view filter
    view_option = st.selectbox("Select Game Log Type", [
        "Last 5 Games", 
        "Last 10 Games", 
        "Last 20 Games", 
        "Head-to-Head vs Team", 
        "Regular Season Only", 
        "Playoffs Only"
    ])

    if player:
        pid = get_player_id(player)
        df = get_player_stats(pid)

        if df.empty:
            st.warning("No recent games available for this player.")
            return

        abbr = team_abbr_map.get(team, "")

        # Apply game log filters
        if view_option == "Last 5 Games":
            filtered_df = df.head(5)
        elif view_option == "Last 10 Games":
            filtered_df = df.head(10)
        elif view_option == "Last 20 Games":
            filtered_df = df.head(20)
        elif view_option == "Head-to-Head vs Team" and abbr:
            filtered_df = df[df['MATCHUP'].str.contains(abbr)]
        elif view_option == "Playoffs Only":
            filtered_df = df[df['SEASON_TYPE'] == 'Playoffs']
        elif view_option == "Regular Season Only":
            filtered_df = df[df['SEASON_TYPE'] == 'Regular Season']
        else:
            filtered_df = df

        # Display filtered stats
        if not filtered_df.empty:
            st.subheader(f"{view_option} for {player}")
            st.dataframe(filtered_df[['GAME_DATE', 'MATCHUP', 'PTS', 'AST', 'REB']].reset_index(drop=True))

            # Prediction
            avg_pts = filtered_df['PTS'].mean()
            st.markdown(f"**Predicted Points (Average): `{avg_pts:.1f}`**")

            # Over/Under interactive check
            line = st.slider("Set a points line for over/under prediction:", 0, 50, 20)
            if avg_pts > line:
                st.success(f"🟢 Over! Predicted {avg_pts:.1f} > {line}")
            else:
                st.warning(f"🔴 Under. Predicted {avg_pts:.1f} < {line}")
        else:
            st.warning(f"No data available for '{view_option}'. Try another filter.")
