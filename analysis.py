import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Google Play Store Analysis")

# Load Data
df = pd.read_csv("datastore.csv")
df.drop_duplicates(subset="App", inplace=True)
df.dropna(subset=["Rating"], inplace=True)
df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")
df["Reviews"] = pd.to_numeric(df["Reviews"], errors="coerce")
df["Installs"] = df["Installs"].str.replace(r"[+,]", "", regex=True)
df["Installs"] = pd.to_numeric(df["Installs"], errors="coerce")
df = df[df["Rating"].between(0, 5)]

# 1. Rating Distribution
st.subheader("1. Rating Distribution")
fig, ax = plt.subplots()
ax.hist(df["Rating"].dropna(), bins=20, color="steelblue", edgecolor="black")
ax.set_xlabel("Rating")
ax.set_ylabel("Number of Apps")
ax.set_title("Rating Distribution")
st.pyplot(fig)

# 2. Top 10 Categories
st.subheader("2. Top 10 Categories by App Count")
top_cat = df["Category"].value_counts().head(10)
fig, ax = plt.subplots()
ax.bar(top_cat.index, top_cat.values, color="orange")
ax.set_ylabel("Number of Apps")
ax.set_title("Top 10 Categories")
plt.xticks(rotation=45, ha="right")
st.pyplot(fig)

# 3. Free vs Paid
st.subheader("3. Free vs Paid Apps")
type_count = df["Type"].value_counts()
fig, ax = plt.subplots()
ax.pie(type_count.values, labels=type_count.index, autopct="%1.1f%%", colors=["green", "red"])
ax.set_title("Free vs Paid")
st.pyplot(fig)

# 4. Top 10 Most Installed Apps
st.subheader("4. Top 10 Most Installed Apps")
top_apps = df.nlargest(10, "Installs")[["App", "Installs"]]
fig, ax = plt.subplots()
ax.barh(top_apps["App"], top_apps["Installs"] / 1e6, color="purple")
ax.set_xlabel("Installs (Millions)")
ax.set_title("Most Installed Apps")
st.pyplot(fig)

# 5. Average Rating by Category
st.subheader("5. Average Rating by Category (Top 10)")
avg_rating = df.groupby("Category")["Rating"].mean().sort_values(ascending=False).head(10)
fig, ax = plt.subplots()
ax.bar(avg_rating.index, avg_rating.values, color="teal")
ax.set_ylabel("Avg Rating")
ax.set_ylim(3, 5)
ax.set_title("Avg Rating by Category")
plt.xticks(rotation=45, ha="right")
st.pyplot(fig)

st.caption("Dataset: googleplaystore.csv from Kaggle")
