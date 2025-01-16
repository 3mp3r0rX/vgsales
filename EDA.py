import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno

file_path = "curated_video_game_sales.csv"
data = pd.read_csv(file_path)


print (data.head())


print (f"Dataset Shape: {data.shape}")

print(data.describe())

print(data['Genre'].value_counts())
print(data['Platform'].value_counts())

msno.matrix(data)
plt.show()

plt.figure(figsize = (8, 5))
sns.histplot(data['GlobalSales'], kde = False, bins = 30, color = 'blue')
plt.title('Global Sales Distribution')
plt.xlabel('Global Sales')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize = (10, 6))
sns.countplot(y=data['Genre'], order=data['Genre'].value_counts().index,hue=data['Genre'], palette='viridis', legend=False)
plt.title('Genre Distribution')
plt.xlabel('Count')
plt.ylabel('Genre')
plt.show()

numeric_data = data.select_dtypes(include = ['float64', 'int64'])

correlation_matrix = numeric_data.corr()

plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(x='Platform', y='GlobalSales', data=data, hue=data['Platform'], palette='cool', legend=False)
plt.title('Global Sales by Platform')
plt.xlabel('Platform')
plt.ylabel('Global Sales')
plt.xticks(rotation=45)
plt.show()

sns.pairplot(data, hue='Genre', palette='husl', diag_kind='kde')
plt.show()


top_platforms =  data.groupby('Platform')['GlobalSales'].sum().sort_values(ascending=False).head(10)
print(top_platforms)

sales_by_year = data.groupby('Year')['GlobalSales'].sum()
print(sales_by_year.idxmax(), sales_by_year.max())