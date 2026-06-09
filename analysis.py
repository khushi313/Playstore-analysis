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
# 🧹 Data Cleaning
# -------------------------------
df = df.dropna(subset=['Rating'])

df['Installs'] = df['Installs'].astype(str)
df['Installs'] = df['Installs'].str.replace('+', '', regex=False)
df['Installs'] = df['Installs'].str.replace(',', '', regex=False)
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')

df['Price'] = df['Price'].astype(str)
df['Price'] = df['Price'].str.replace('$', '', regex=False)
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# -------------------------------
# 📊 Dataset Preview
# -------------------------------
st.subheader("📌 Dataset Preview")
st.dataframe(df.head())

# -------------------------------
# 📊 GRAPH 1: Top Apps by Installs
# -------------------------------
st.subheader("🔥 Top 10 Apps by Installs")

top_apps = df.sort_values(by='Installs', ascending=False).head(10)

fig1, ax1 = plt.subplots(figsize=(10,5))
ax1.bar(top_apps['App'], top_apps['Installs'])
ax1.set_title("Top Apps by Installs")
ax1.set_xlabel("Apps")
ax1.set_ylabel("Installs")
plt.xticks(rotation=45, ha='right')

st.pyplot(fig1)
plt.clf()

# -------------------------------
# 📊 GRAPH 2: Category vs Rating
# -------------------------------
st.subheader("⭐ Top Categories by Rating")

category_rating = df.groupby('Category')['Rating'].mean().sort_values(ascending=False).head(10)

fig2, ax2 = plt.subplots(figsize=(8,5))
category_rating.plot(kind='bar', ax=ax2)
ax2.set_title("Category vs Rating")
ax2.set_xlabel("Category")
ax2.set_ylabel("Average Rating")

st.pyplot(fig2)
plt.clf()

# -------------------------------
# 📊 GRAPH 3: Free vs Paid Apps
# -------------------------------
st.subheader("💰 Free vs Paid Apps Rating Comparison")

free_paid = df.groupby('Type')['Rating'].mean().fillna(0)

fig3, ax3 = plt.subplots(figsize=(5,4))
free_paid.plot(kind='bar', ax=ax3, color=['green', 'orange'])
ax3.set_title("Free vs Paid Apps")
ax3.set_ylabel("Average Rating")

st.pyplot(fig3)
plt.clf()

# -------------------------------
# 📊 GRAPH 4: Rating Distribution
# -------------------------------
st.subheader("📊 Rating Distribution")

fig4, ax4 = plt.subplots(figsize=(6,4))
ax4.hist(df['Rating'], bins=10, color='skyblue', edgecolor='black')
ax4.set_title("Rating Distribution")
ax4.set_xlabel("Rating")
ax4.set_ylabel("Count")

st.pyplot(fig4)
plt.clf()

# -------------------------------
# 📌 CLEAN INSIGHTS SECTION
# -------------------------------
st.subheader("📌 Insights (Clean View)")

st.markdown("### ⭐ Top Categories")
st.dataframe(category_rating)

st.markdown("### 💰 Free vs Paid Apps (Average Rating)")
st.dataframe(free_paid)

st.markdown("### 🔥 Key Insight")
st.write("• Free apps dominate installs 📈")
st.write("• Paid apps generally have slightly higher ratings 💰")
st.write("• Most apps are rated between 4.0 - 4.5 ⭐")
