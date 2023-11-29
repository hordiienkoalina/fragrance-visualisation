import pandas as pd

df = pd.read_csv('data/perfumes_cleaned.csv')

# Convert the DataFrame to JSON
json_data = df.to_json(orient = 'records')

with open('data/perfumes.json', 'w') as json_file:
    json_file.write(json_data)