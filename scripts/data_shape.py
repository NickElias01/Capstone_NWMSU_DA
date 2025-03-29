import pandas as pd

# Load datasets
city_df = pd.read_csv('data/City_energy_profiles.csv')
county_df = pd.read_csv('data/County_energy_profiles.csv')

# Print shape (rows, columns)
print("\nCity Dataset shape (rows, columns):", city_df.shape)
print("County Dataset shape (rows, columns):", county_df.shape)