import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset.csv")



# Show first 5 rows
print(df.head())

# Data Cleaning
df = df.dropna()

# Clean Installs column
df['Installs'] = df['Installs'].str.replace('+','', regex=False)
df['Installs'] = df['Installs'].str.replace(',','', regex=False)

df['Installs'] = df['Installs'].astype(int)

# Convert Price

df['Price'] = df['Price'].str.replace('$','', regex=False)
df['Price'] = df['Price'].astype(float)


# -------------------------------
# 📊 GRAPH 1: Installs vs Rating
# -------------------------------

top_apps = df.sort_values(by='Installs', ascending=False).head(10)
plt.figure(figsize=(10,5))
plt.bar(top_apps['App'], top_apps['Installs'])
plt.xlabel("App Name")
plt.ylabel("Installs")
plt.title("Top 10 Apps by Installs")

# -------------------------------
# 📊 GRAPH 2: Category vs Rating
# -------------------------------
category_rating = df.groupby('Category')['Rating'].mean().sort_values(ascending=False)
plt.figure(figsize=(10,5))
category_rating.head(10).plot(kind='bar')
plt.title("Top Categories by Rating")
plt.ylabel("Average Rating")
# plt.show()

# -------------------------------
# 📊 GRAPH 3: Free vs Paid
# -------------------------------
free_paid = df.groupby('Type')['Rating'].mean()
plt.figure(figsize=(10,5))
free_paid.plot(kind='bar')
plt.title("Free vs Paid Apps Rating")
# plt.show()

# -------------------------------
# 📊 GRAPH 4: Rating Distribution
# -------------------------------
plt.figure(figsize=(10,5))
df['Rating'].hist()

plt.title("Rating Distribution")

plt.show()

# Insights print
print("\nTop Categories:\n", category_rating.head())
print("\nFree vs Paid:\n", free_paid)
