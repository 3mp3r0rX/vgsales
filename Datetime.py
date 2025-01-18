import pandas as pd

file_path = 'last_updated_video_game_sales.csv'
Majed=pd.read_csv(file_path)

print(Majed.dtypes)
#
# Majed['Year'] = pd.to_datetime(Majed['Year'], format='%Y', errors='coerce')
#
#
# updated_file_path = 'last_updated_video_game_sales.csv'
# Majed.to_csv(updated_file_path)
#
#
# print("Year colmun converted to datetime. Updated file saved at:", updated_file_path)