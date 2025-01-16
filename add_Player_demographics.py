import pandas as pd

file_path = 'curated_video_game_sales.csv'
data = pd.read_csv(file_path)

def assign_demographic(row):
    if row['Genre'] in ['Action', 'Shooter']:
        return 'Hardcore'
    elif row['Genre'] in ['Puzzle', 'Adventure']:
        return 'Casual'
    elif row['Genre'] in ['Sport', 'Racing']:
        return 'All Ages'
    else:
        return 'General'

data['player_demographic'] = data.apply(assign_demographic, axis=1)

data.to_csv("updated_video_game_sales.csv", index=False)