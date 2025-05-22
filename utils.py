# utils.py
from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playergamelog
import pandas as pd

# Global player/team data
all_players = players.get_players()
all_teams = teams.get_teams()

player_names = sorted([p['full_name'] for p in all_players])
team_names = sorted([t['full_name'] for t in all_teams])
team_abbr_map = {t['full_name']: t['abbreviation'] for t in all_teams}

def get_player_id(name):
    return next((p['id'] for p in all_players if p['full_name'] == name), None)

def get_player_stats(player_id):
    try:
        gamelog = playergamelog.PlayerGameLog(player_id=player_id)
        return gamelog.get_data_frames()[0]
    except Exception:
        return pd.DataFrame()
