import requests
from bs4 import BeautifulSoup
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 1. Scraping and Data Preparation
url = "https://en.wikipedia.org/wiki/Cinema_of_India"
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

tables = soup.find_all('table', {'class': 'wikitable'})
data = []

for row in tables[0].find_all('tr')[1:]:
    cols = row.find_all('td')
    if len(cols) >= 2:
        industry = cols[0].text.strip()
        # Cleaning: Comma aur references [1] hatana
        films_text = cols[1].text.strip().replace(',', '').split('[')[0]
        if films_text.isdigit():
            data.append([industry, int(films_text)])

df = pd.DataFrame(data, columns=['Industry', 'FilmsCount'])

# 2. K-Means Clustering
X = df[['FilmsCount']].values
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

# 3. Plotting the Graph
plt.figure(figsize=(12, 6))
colors = ['red', 'blue', 'green']
for i in range(3):
    cluster_data = df[df['Cluster'] == i]
    plt.scatter(cluster_data['Industry'], cluster_data['FilmsCount'], 
                label=f'Cluster {i}', s=100, edgecolors='black')

plt.xticks(rotation=45, ha='right') 
plt.title('K-Means Clustering: Indian Film Industries by Film Count')
plt.xlabel('Film Industry')
plt.ylabel('Number of Films')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout() 
plt.show()