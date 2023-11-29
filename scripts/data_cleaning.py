import pandas as pd

df = pd.read_csv('data/perfumes.csv')

# Remove rows where the country and release year is 'Unknown'
df = df[(df['Country'] != 'Unknown') & (df['Release Year'] != 'Unknown')]

df.to_csv('data/perfumes_cleaned.csv', index = False)