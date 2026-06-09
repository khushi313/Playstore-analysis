import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("datastore.csv")

print("Shape:", df.shape)
print(df.head())

# Data Cleaning
df = df.dropna()

df['Installs'] = df['Installs'].str.replace('+', '', regex=False)
df['Installs'] = df['Installs'].str.replace(',', '', regex=False)
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')

df['Price'] = df['Price'].str.replace('$', '', regex=False)
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
df = df.dropna(subset=['Installs', 'Rating', 'Price'])

print("\nCleaned Data Shape:", df.shape)

# -------------------------------
# GRAPH 1: Top 10 Apps by Installs
# -------------------------------
top_apps = df.sort_values(by='Installs', ascending=False).head(10)

plt.figure(figsize=(12, 5))
plt.bar(range(10), top_apps['Installs'] / 1e6, color='steelblue')
plt.xticks(range(10), top_apps['App'], rotation=45, ha='right', fontsize=9)
plt.xlabel("App Name")
plt.ylabel("Installs (in Millions)")
plt.title("Top 10 Apps by Installs")
plt.tight_layout()
plt.savefig("graph1_top_installs.png")
plt.show()

# -------------------------------
# GRAPH 2: Top 10 Categories by Rating
# -------------------------------
category_rating = df.groupby('Category')['Rating'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 5))
plt.bar(range(10), category_rating.values, color='orange')
plt.xticks(range(10), category_rating.index, rotation=45, ha='right', fontsize=9)
plt.ylabel("Average Rating")
plt.title("Top 10 Categories by Average Rating")
plt.ylim(0, 5)
plt.tight_layout()
plt.savefig("graph2_category_rating.png")
plt.show()

# -------------------------------
# GRAPH 3: Free vs Paid Apps Rating
# -------------------------------
free_paid = df.groupby('Type')['Rating'].mean()

plt.figure(figsize=(6, 5))
plt.bar(free_paid.index, free_paid.values, color=['green', 'red'], width=0.4)
plt.ylabel("Average Rating")
plt.title("Free vs Paid Apps - Avg Rating")
plt.ylim(0, 5)
for i, val in enumerate(free_paid.values):
    plt.text(i, val + 0.05, f"{val:.2f}", ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig("graph3_free_vs_paid.png")
plt.show()

# -------------------------------
# GRAPH 4: Rating Distribution
# -------------------------------
plt.figure(figsize=(10, 5))
plt.hist(df['Rating'], bins=20, color='purple', edgecolor='black')
plt.xlabel("Rating")
plt.ylabel("Number of Apps")
plt.title("Rating Distribution of Apps")
plt.tight_layout()
plt.savefig("graph4_rating_dist.png")
plt.show()

# Insights
print("\nTop 10 Categories by Rating:\n", category_rating)
print("\nFree vs Paid Avg Rating:\n", free_paid)
