import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Play Store Data Analysis Dashboard")

# Load dataset
df = pd.read_csv("dataset.csv")

# -------------------------------
# DATA CLEANING
# -------------------------------
df = df.dropna()

df['Installs'] = df['Installs'].str.replace('+', '', regex=False)
df['Installs'] = df['Installs'].str.replace(',', '', regex=False)
df['Installs'] = df['Installs'].astype(int)

df['Price'] = df['Price'].str.replace('$', '', regex=False)
df['Price'] = df['Price'].replace('Everyone', '0')
df['Price'] = df['Price'].astype(float)

df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
df = df.dropna(subset=['Rating'])

st.subheader("Dataset Preview")
st.dataframe(df.head())

# -------------------------------
# GRAPH 1
# -------------------------------
st.subheader("Top 10 Apps by Installs")

top_apps = df.sort_values(by='Installs', ascending=False).head(10)

fig, ax = plt.subplots()
ax.bar(top_apps['App'], top_apps['Installs'])
plt.xticks(rotation=45)
st.pyplot(fig)

# -------------------------------
# GRAPH 2
# -------------------------------
st.subheader("Top Categories by Rating")

category_rating = df.groupby('Category')['Rating'].mean().sort_values(ascending=False)

fig, ax = plt.subplots()
category_rating.head(10).plot(kind='bar', ax=ax)
st.pyplot(fig)

# -------------------------------
# GRAPH 3
# -------------------------------
st.subheader("Free vs Paid Apps Rating")

free_paid = df.groupby('Type')['Rating'].mean()

fig, ax = plt.subplots()
free_paid.plot(kind='bar', ax=ax, color=['green','orange'])
st.pyplot(fig)

# -------------------------------
# GRAPH 4
# -------------------------------
st.subheader("Rating Distribution")

fig, ax = plt.subplots()
ax.hist(df['Rating'], bins=20)
st.pyplot(fig)

st.success("Analysis Complete 🚀")
