import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset.csv")

# Show first 5 rows
print(df.head())

# -------------------------------
# DATA CLEANING
# -------------------------------
df = df.dropna()

# Clean Installs column
df['Installs'] = df['Installs'].str.replace('+', '', regex=False)
df['Installs'] = df['Installs'].str.replace(',', '', regex=False)
df['Installs'] = df['Installs'].astype(int)

# Clean Price column
df['Price'] = df['Price'].str.replace('$', '', regex=False)
df['Price'] = df['Price'].replace('Everyone', '0')   # extra safety (common dataset issue)
df['Price'] = df['Price'].astype(float)

# Clean Rating (optional safety)
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
df = df.dropna(subset=['Rating'])

# -------------------------------
# 📊 GRAPH 1: Top 10 Apps by Installs
# -------------------------------
top_apps = df.sort_values(by='Installs', ascending=False).head(10)

plt.figure(figsize=(12,6))
plt.bar(top_apps['App'], top_apps['Installs'])
plt.xticks(rotation=45, ha='right')
plt.xlabel("App Name")
plt.ylabel("Installs")
plt.title("Top 10 Apps by Installs")
plt.tight_layout()
plt.show()

# -------------------------------
# 📊 GRAPH 2: Top Categories by Rating
# -------------------------------
category_rating = df.groupby('Category')['Rating'].mean().sort_values(ascending=False)

plt.figure(figsize=(12,6))
category_rating.head(10).plot(kind='bar')
plt.title("Top Categories by Rating")
plt.ylabel("Average Rating")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -------------------------------
# 📊 GRAPH 3: Free vs Paid Apps Rating
# -------------------------------
free_paid = df.groupby('Type')['Rating'].mean()

plt.figure(figsize=(6,5))
free_paid.plot(kind='bar', color=['green', 'orange'])
plt.title("Free vs Paid Apps Rating")
plt.ylabel("Average Rating")
plt.tight_layout()
plt.show()

# -------------------------------
# 📊 GRAPH 4: Rating Distribution
# -------------------------------
plt.figure(figsize=(10,5))
plt.hist(df['Rating'], bins=20, color='skyblue', edgecolor='black')
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Apps")
plt.tight_layout()
plt.show()

# -------------------------------
# INSIGHTS
# -------------------------------
print("\nTop Categories:\n", category_rating.head())
print("\nFree vs Paid:\n", free_paid)
