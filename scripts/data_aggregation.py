import pandas as pd
import pycountry

df = pd.read_json('data/perfumes.json')

# Group by 'Country' and count the number of perfumes
perfume_counts = df.groupby('Country').size().reset_index(name = 'Perfume Count')

# Convert country names to ISO 3166-1 alpha-3 country codes
perfume_counts['Country'] = perfume_counts['Country'].apply(lambda x: pycountry.countries.get(name = x).alpha_3 if pycountry.countries.get(name=  x) is not None else x)

# Convert the DataFrame to JSON
json_data = perfume_counts.to_json(orient = 'records')

with open('data/perfumes_aggregated.json', 'w') as json_file:
    json_file.write(json_data)