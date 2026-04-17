import pandas as pd

# Load the CSV from your local data folder
df = pd.read_csv('data/ices_nga.csv')
print(df.head())