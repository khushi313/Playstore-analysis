import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("📊 Play Store Analysis Dashboard")

# -------------------------------
# 📁 Load dataset
# -------------------------------
df = pd.read_csv("dataset.csv")

# -------------------------------
# 🧹 Data Cleaning (SAFE VERSION)
# -------------------------------

# Drop rows where Rating is missing (important)
df = df.dropna(subset=['Rating'])

# Clean Installs column
df['Installs'] = df['Installs'].astype(str)
df['Installs'] = df['Installs'].str.replace('+', '', regex=False)
df['Installs'] = df['Installs'].str.replace(',', '', regex=False)
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')

# Clean Price column
df['Price'] = df['Price'].astype(str)
df['Price'] = df['Price'].str.replace('$', '', regex=False)
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# -------------------------------
# 📊 Dataset Preview
# -------------------------------
st.subheader("Dataset Preview")
st.write(df.head())

# -------------------------------
# 📊 GRAPH 1: Top Apps by Installs
# -------------------------------
st.subheader("Top 10 Apps by Installs")

top_apps = df.sort_values(by='Installs', ascending=False).head(10)

fig1, ax1 = plt.subplots()
ax1.bar(top_apps['App'], top_apps['Installs'])
plt.xticks(rotation=45)

st.pyplot(fig1)
fig1.tight_layout()

# -------------------------------
# 📊 GRAPH 2: Category vs Rating
# -------------------------------
st.subheader("Top Categories by Rating")

category_rating = df.groupby('Category')['Rating'].mean().sort_values(ascending=False).head(10)

fig2, ax2 = plt.subplots()
category_rating.plot(kind='bar', ax=ax2)

st.pyplot(fig2)
fig2.tight_layout()

# -------------------------------
# 📊 GRAPH 3: Free vs Paid
# -------------------------------
st.subheader("Free vs Paid Apps Rating")

free_paid = df.groupby('Type')['Rating'].mean()

fig3, ax3 = plt.subplots()
free_paid.plot(kind='bar', ax=ax3)

st.pyplot(fig3)
fig3.tight_layout()

# -------------------------------
# 📊 GRAPH 4: Rating Distribution
# -------------------------------
st.subheader("Rating Distribution")

fig4, ax4 = plt.subplots()
df['Rating'].hist(ax=ax4)

st.pyplot(fig4)
fig4.tight_layout()

# -------------------------------
# 📌 Insights
# -------------------------------
st.subheader("Insights")

st.write("⭐ Top Categories:")
st.write(category_rating)

st.write("💰 Free vs Paid Apps:")
st.write(free_paid)
