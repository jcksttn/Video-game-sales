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