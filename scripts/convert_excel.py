import pandas as pd

def process_energy_sheet(df):
    """Process City and County sheets by combining first 5 rows for headers"""
    new_header = df.iloc[:4].fillna("").astype(str).agg(" ".join).str.strip()
    df = df.iloc[4:]  # Drop the first 4 rows after combining them into one header row
    df.columns = new_header
    return df

# Load in only a few tabs
sheets_to_use = ["City", "County"]

# Define column filters for each sheet type
CITY_COLUMNS = [
    'city_name', 'latitude', 'longitude', 'population', 'doe_climate_zone',
    'Residential Electricity  consumption (MWh)', 'Residential Natural Gas  consumption (Mcf)',
    'Residential Electricity  utility customers', 'Residential Natural Gas  utility customers',
    'Commercial Electricity  consumption (MWh)', 'Commercial Natural Gas  consumption (Mcf)',
    'Commercial Electricity  utility customers', 'Commercial Natural Gas  utility customers',
    'Industry Electricity  consumption (MWh)', 'Industry Natural Gas  consumption (Mcf)',
    'Residential Electricity  GHG emissions (mtons CO2e)', 
    'Commercial Electricity  GHG emissions (mtons CO2e)',
    'Industry Electricity  GHG emissions (mtons CO2e)'
]


COUNTY_COLUMNS = [
    'state_id', 'state_abbr', 'county_name', 'latitude', 'longitude',
    'population', 'doe_climate_zone',
    'Residential Electricity  consumption (MWh)',
    'Residential Natural Gas  consumption (Mcf)',
    'Residential Electricity  utility customers',
    'Residential Natural Gas  utility customers',
    'Commercial Electricity  consumption (MWh)',
    'Commercial Natural Gas  consumption (Mcf)', 
    'Commercial Electricity  utility customers',
    'Commercial Natural Gas  utility customers',
    'Industry Electricity  consumption (MWh)',
    'Industry Natural Gas  consumption (Mcf)',
    'On Road Transportation Gasoline  consumption (gallons)',
    'On Road Transportation Diesel  consumption (gallons)',
    'Residential Electricity  GHG emissions mtons CO2e',
    'Commercial Electricity  GHG emissions mtons CO2e', 
    'Industry Electricity  GHG emissions mtons CO2e',
    'On-road Transportation Gasoline  GHG emissions mtons CO2e',
    'On-road Transportation Diesel  GHG emissions mtons CO2e'
]


file_path = "data/raw_2016cityandcountyenergyprofiles_units correction.xlsb"
output_dir = "data/"

sheets = pd.read_excel(file_path, sheet_name=sheets_to_use, engine="pyxlsb")

# Save each sheet to a separate CSV file
for sheet_name, df in sheets.items():
    # Apply different processing for energy profile sheets vs gazetteer
    if sheet_name == "City":
        df = process_energy_sheet(df)
        df = df.loc[df['state_abbr'] == 'CO']
        df = df[CITY_COLUMNS]
    elif sheet_name == "County":
        df = process_energy_sheet(df)
        df = df.loc[df['state_abbr'] == 'CO']
        df = df[COUNTY_COLUMNS]
    
    # Save to CSV
    output_path = f"{output_dir}{sheet_name}_energy_profiles.csv"
    df.to_csv(output_path, index=False)
    print(f"Data from sheet '{sheet_name}' saved to {output_path}")