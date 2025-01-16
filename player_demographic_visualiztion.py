import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = "updated_video_game_sales.csv"
data = pd.read_csv(file_path)


plt.figure(figsize=(10,6))
sns.countplot(x='player_demographic', data=data, hue=data['player_demographic'], palette='viridis', legend=False)
plt.title('Distribution of player demographics')
plt.xlabel('Player Demographics')
plt.ylabel('Number of Games')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='player_demographic', y='GlobalSales', hue=data['player_demographic'], data=data, palette='coolwarm', legend=False)
plt.title('Global Sales by Player Demographic')
plt.xlabel('Player Demographic')
plt.ylabel('Global Sales (in millions)')
plt.show()


genre_demographic = pd.crosstab(data['Genre'], data['player_demographic'])
print(genre_demographic)
plt.figure(figsize=(12, 8))
sns.heatmap(genre_demographic, annot=True, cmap='Blues', fmt='.0f')
plt.title('Genre vs. Player Demographics')
plt.xlabel('Player Demographic')
plt.ylabel('Genre')
plt.show()