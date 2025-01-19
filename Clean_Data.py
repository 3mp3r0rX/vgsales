import pandas as pd


df = pd.read_csv('vgsales.csv')

# Data Profiling
print(df.info())
print(df.isnull().sum())
print(df.describe())

# Data Cleaning
df = df.dropna(subset=['Year', 'Publisher'])
df['Year'] = df['Year'].fillna(df['Year'].median()).astype(int)
df = df.drop_duplicates()
df = df[df['Global_Sales'] <= 50]

# Data Wrangling
df['Decade'] = (df['Year'] // 10) * 10
df = df[df['Year'] > 2000]
platform_sales = df.groupby('Platform')['Global_Sales'].sum().reset_index()
platform_sales = platform_sales.sort_values(by='Global_Sales', ascending=False)

# Save the cleaned dataset
df.to_csv('vgsales_cleaned.csv', index=False)

# Data Validation
print(df.isnull().sum())
print(df.dtypes)
df['Calculated_Global_Sales'] = df['NA_Sales'] + df['EU_Sales'] + df['JP_Sales'] + df['Other_Sales']
print(df[['Global_Sales', 'Calculated_Global_Sales']].head())