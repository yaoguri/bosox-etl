import statsapi
import pandas as pd
import requests
from sqlalchemy import create_engine

schedule = statsapi.schedule(
    start_date = "03/27/2025", 
    end_date = "09/28/2025", 
    team = 111,
    sportId = 1
    )

games = []

for game in schedule:
    if game['status'] == 'Final':
        redsox_home = 'Red Sox' in game['home_name']
    
    game_data = {
        'date' : game['game_date'],
        'opponent' : game['away_name'] if redsox_home else game['home_name'],
        'home_away': 'Home' if redsox_home else 'Away',
        'redsox_score': game['home_score'] if redsox_home else game['away_score'],
        'opponent_score' : game['away_score'] if redsox_home else game['home_score']
        }
    
    redsox_runs = int(game_data['redsox_score'])
    opponent_runs = int(game_data['opponent_score'])

    if redsox_runs > opponent_runs:
        game_data['outcome'] = 'Win'
    elif redsox_runs < opponent_runs:
        game_data['outcome'] = 'Loss'
    else:
        game_data['outcome'] = 'Tie'

    
    game_data['run_diff'] = redsox_runs - opponent_runs

    games.append(game_data)

conn_str = "postgresql://postgres:ilovepaupau@localhost:5432/redsox_data"

engine = create_engine(conn_str)

df = pd.DataFrame(games)
df['date'] = pd.to_datetime(df['date'])

df.to_sql("redsox_games_2024", con = engine, if_exists = "replace", index = False)
print(df.head())