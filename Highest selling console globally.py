import pandas as pd

# Load the dataset
df = pd.read_csv('vgsales.csv')

# Filter the dataset for the three consoles
consoles = ['X360', 'PS3', 'Wii']
filtered_df = df[df['Platform'].isin(consoles)]

# Group by Platform and sum the Global Sales
sales_summary = filtered_df.groupby('Platform')['Global_Sales'].sum().reset_index()

# Sort the results to find the console with the highest sales
sales_summary = sales_summary.sort_values(by='Global_Sales', ascending=False)

sales_summary