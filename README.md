# 🎮 Video Game Sales Analysis

## Project Overview
---

A data analysis project using video games sales data to explore, visualise and analyse console and games sales performance

This project usings video games sales data to 
- Track sale of three seventh generation consoles globally
- Sales of games by genre
- Sale of games by region around the world

## Dataset
---
Video Game Sales
- [Download here](https://www.kaggle.com/datasets/gregorut/videogamesales)
    - The dataset (`vgsales.csv`) contains historical data on video game sales worldwide.
 
## Tools
---
- Excel - Data Cleaning
- Python - Data analyis and visualisation

## Data Cleaning
---
In the initial data perparation phase, the follow tasks were performed 
1. Data extraction and loading
2. Data inspection
3. Handling missing values
4. Data cleaning and formating

## Goals
---
1. Which of the three seventh generation consoles (Xbox 360, Playstation 3, and Nintendo Wii) had the highest total sales globally.
2. Visualise the average sales for games in the most popular three genres and to differentiate between NA, EU, and global sales.
3. Are some genres significantly more likely to perform better or worse in Japan than others?

## Data Analysis
---
1.  Which of the three seventh generation consoles had the highest total sales globally.
  
```
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
```

2. Visualise the average sales for games in the most popular three genres (differentiate between reigons and global sales)

```
import matplotlib.pyplot as plt
import seaborn as sns

# Group by Genre and calculate the average sales
average_sales_by_genre = df.groupby('Genre')[['NA_Sales', 'EU_Sales', 'Global_Sales']].mean().reset_index()

# Sort genres by Global Sales to find the top 3
most_popular_genres = average_sales_by_genre.sort_values(by='Global_Sales', ascending=False).head(3)

# Melt the DataFrame for easier plotting
melted_sales = most_popular_genres.melt(id_vars='Genre', var_name='Region', value_name='Average_Sales')

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(data=melted_sales, x='Genre', y='Average_Sales', hue='Region')
plt.title('Average Sales for Games in the Most Popular Three Genres')
plt.ylabel('Average Sales (in millions)')
plt.xlabel('Genre')
plt.legend(title='Region')
plt.show()
```
![Average Sales of Games in the Most Popular Three Genres](https://github.com/user-attachments/assets/acd5352d-1460-412c-81e4-3265c6ec0ce1)

3. The genres that are more likely to perform better or worse in Japan than others

```
import pandas as pd
import scipy.stats as stats

# Load the dataset
vgsales = pd.read_csv('vgsales.csv')

# Group by Genre and calculate the average sales in Japan
average_jp_sales_by_genre = vgsales.groupby('Genre')['JP_Sales'].mean().reset_index()

# Sort genres by JP Sales
average_jp_sales_by_genre = average_jp_sales_by_genre.sort_values(by='JP_Sales', ascending=False)

# Display the average sales in Japan by genre
average_jp_sales_by_genre
```

