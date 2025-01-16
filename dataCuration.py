import pandas as pd

file_path = "vgsales.csv"
data = pd.read_csv(file_path)


print(data.head())
print(data.info())
print(data.isnull().sum())
print(f"Dublicate rows: {data.duplicated().sum()}")
print(data.dtypes)


data = data.dropna()
data = data.drop_duplicates()

print(data[data['Global_Sales'] < 0])

print(data['Genre'].unique())
print(data['Platform'].unique())

data.rename(columns={"Global_Sales": "GlobalSales"}, inplace=True)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
data[['Global_Sales']] = scaler.fit_transform(data[['GlobalSales']])

curated_file_path = "curated_video_game_sales.csv"
data.to_csv(curated_file_path, index=False)