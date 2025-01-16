# # import matplotlib
# # import numpy as np
# # import pandas as pd
# #
# # file_path = "vgsales.csv"
# # data = pd.read_csv(file_path)
# #
# #
# # print("Data Overview:")
# # print(data.info)
# # print("Data Description:")
# # print(data.describe())
# # print("Data Columns:")
# # print(data.columns)
# # print("head")
# # print(data.head())
# #
# #
# # missing_values = data.isnull().sum()
# # print(missing_values)
# #
# # categorical_columns = ['Platform', 'Publisher']
# # for column in categorical_columns:
# #     print("Unique values in {col}")
# #     print(data[column].nunique())
# #
# # columns_to_drop = ['rank']
# # data = data.drop(columns=columns_to_drop, errors='ignore')
# #
# # data['Year'] = data['Year'].fillna(data['Year'].median())
# #
# # data['Year'] = data['Year'].astype(int)
# #
# #
# # data.columns = [col.lower().replace(' ', '_') for col in data.columns]
# #
# # print('\nCleaned Dataset Overview:')
# # print(data.info())
# #
# # cleaned_file_path = "cleaned_video_game_sales.csv"
# # data.to_csv(cleaned_file_path, index=False)
# # print(f"\nCleaned dataset saved to {cleaned_file_path}")
# #
# # # import pandas as pd
# # # import sqlite3
# # # import matplotlib.pyplot as plt
# # # import seaborn as sns
# # #
# # # df = pd.read_csv('cleaned_video_game_sales.csv')
# # #
# # # conn = sqlite3.connect('video_game_sales.db')
# # #
# # # query = """
# # # SELECT Platform AS platform, SUM(Global_Sales) AS total_sales
# # # FROM video_game_sales
# # # GROUP BY Platform
# # # ORDER BY total_sales DESC;
# # #
# # # """
# # # df_platform_sales = pd.read_sql_query(query, conn)
# # #
# # # conn.close()
# # #
# # # print(df_platform_sales)
# # #
# # # plt.figure(figsize=(12, 6))
# # # sns.barplot(
# # #     x='total_sales',
# # #     y='platform',
# # #     data=df_platform_sales,
# # #     hue='platform',
# # #     palette='Blues_d',
# # #     dodge=False,
# # #     legend=False
# # # )
# # # plt.title("Total Global Sales by Platform")
# # # plt.xlabel("Total Sales (Millions)")
# # # plt.ylabel("Platform")
# # # plt.show()
#
#
#
# import sqlite3
# import pandas as pd
#
#
# sales_file = "cleaned_video_game_sales.csv"
# demographics_file = "player_demographics.csv"
#
# sales_data = pd.read_csv(sales_file)
# demographics_data = pd.read_csv(demographics_file)
#
# conn = sqlite3.connect('gaming_analytics.db')
#
# # sales_data.to_sql('video_game_sales', conn, if_exists='replace', index=False)
# # demographics_data.to_sql("player_demographics", conn, if_exists="replace", index=False)
# #
# # print("Data Successfully loaded into SQLite!")
#
#
# with conn:
#     cursor = conn.cursor()
#     cursor.execute("SELECT gender FROM player_demographics")
#     print("Tables in database:", cursor.fetchall())
#
#     # Check structure of the video game sales table
#     cursor.execute("PRAGMA table_info(video_game_sales);")
#     print("Video Game Sales Table Structure:", cursor.fetchall())
#
#     # Check structure of the demographics table
#     cursor.execute("PRAGMA table_info(player_demographics);")
#     print("Player Demographics Table Structure:", cursor.fetchall())
#
#

