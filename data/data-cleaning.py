import pandas as pd


# Read in data set
df = pd.read_csv('data/assign1-grades.csv')

# Assign valid parameter ranges to each column
valid_school = ['GP', 'MS']


# Ensure columns are properly formatted 
df['school'] = df['school'].str.upper()

# Remove null and invalid data
df = df[~df['school'].isin(valid_school)]

# Show dataset
print(df.head())
