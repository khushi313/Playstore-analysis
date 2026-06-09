import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Play Store Analysis Dashboard")

# -------------------------------
# Load Data
# -------------------------------
df = pd.read_csv("dataset.csv")

# -------------------------------
# Clean Data
# -------------------------------
df = df.dropna(subset=['Rating'])

df['Installs'] = df['Installs'].astype(str).str.replace('+','').str.replace(',','')
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')

df['Price'] = df['Price'].astype(str).str.replace('$','')
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# -------------------------------
# 🔥 TOP APPS
# -------------------------------
st.subheader("🔥 Top Apps by Installs")

top_apps = df.sort_values(by='Installs', ascending=False).head(10)

fig1, ax1 = plt.subplots(figsize=(10,5))
ax1.bar(top_apps['App'], top_apps['Installs'])
ax1.set_title("Top Apps")
ax1.set_ylabel("Installs")
plt.xticks(rotation=45, ha='right')

st.pyplot(fig1)
plt.clf()

# -------------------------------
# ⭐ CATEGORY RATING
# -------------------------------
st.subheader("⭐ Category Rating")

cat_rating = df.groupby('Category')['Rating'].mean().head(10)

fig2, ax2 = plt.subplots()
cat_rating.plot(kind='bar', ax=ax2)
ax2.set_title("Category vs Rating")

st.pyplot(fig2)
plt.clf()

# -------------------------------
# 💰 PIE CHART: FREE vs PAID
# -------------------------------
st.subheader("💰 Free vs Paid Apps")

type_counts = df['Type'].value_counts()

fig3, ax3 = plt.subplots()
ax3.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%')
ax3.set_title("Free vs Paid Share")

st.pyplot(fig3)
plt.clf()

# -------------------------------
# 📊 RATING DISTRIBUTION (NEW EASY CHART)
# -------------------------------
st.subheader("📊 Rating Distribution")

fig4, ax4 = plt.subplots()
ax4.hist(df['Rating'], bins=10, color='skyblue', edgecolor='black')
ax4.set_title("Ratings Spread")

st.pyplot(fig4)
plt.clf()

# -------------------------------
# 📊 INSTALLS COMPARISON (NEW SIMPLE BAR)
# -------------------------------
st.subheader("📲 Installs Comparison (Top 10)")

installs = df.groupby('Category')['Installs'].sum().sort_values(ascending=False).head(10)

fig5, ax5 = plt.subplots()
installs.plot(kind='bar', ax=ax5, color='orange')
ax5.set_title("Category Installs")

st.pyplot(fig5)
plt.clf()
