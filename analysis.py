import streamlit as st
import pandas as pd
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

df['Installs'] = df['Installs'].astype(str).str.replace('+','', regex=False).str.replace(',','', regex=False)
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')

df['Price'] = df['Price'].astype(str).str.replace('$','', regex=False)
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# -------------------------------
# 🔥 TOP APPS BY INSTALLS
# -------------------------------
st.subheader("🔥 Top Apps by Installs")

top_apps = df.sort_values(by='Installs', ascending=False).head(10)

fig1, ax1 = plt.subplots(figsize=(10,5))
ax1.bar(top_apps['App'], top_apps['Installs'])

ax1.set_title("Top Apps by Installs")
ax1.set_xlabel("Apps")
ax1.set_ylabel("Installs")

# ✅ FIX SCIENTIFIC NOTATION (1e10 problem)
ax1.ticklabel_format(style='plain', axis='y')

plt.xticks(rotation=45, ha='right')

st.pyplot(fig1)
plt.clf()

# -------------------------------
# ⭐ CATEGORY VS RATING
# -------------------------------
st.subheader("⭐ Category vs Rating")

cat_rating = df.groupby('Category')['Rating'].mean().sort_values(ascending=False).head(10)

fig2, ax2 = plt.subplots(figsize=(8,5))
cat_rating.plot(kind='bar', ax=ax2, color='skyblue')

ax2.set_title("Category Rating")
ax2.set_ylabel("Average Rating")

st.pyplot(fig2)
plt.clf()

# -------------------------------
# 💰 FREE VS PAID PIE CHART
# -------------------------------
st.subheader("💰 Free vs Paid Apps")

type_counts = df['Type'].value_counts()

fig3, ax3 = plt.subplots()
ax3.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%')
ax3.set_title("Free vs Paid Share")

st.pyplot(fig3)
plt.clf()

# -------------------------------
# 📊 RATING DISTRIBUTION
# -------------------------------
st.subheader("📊 Rating Distribution")

fig4, ax4 = plt.subplots()
ax4.hist(df['Rating'], bins=10, color='lightgreen', edgecolor='black')

ax4.set_title("Ratings Distribution")
ax4.set_xlabel("Rating")
ax4.set_ylabel("Count")

st.pyplot(fig4)
plt.clf()

# -------------------------------
# 📲 CATEGORY INSTALLS (NEW CHART)
# -------------------------------
st.subheader("📲 Category-wise Installs")

installs = df.groupby('Category')['Installs'].sum().sort_values(ascending=False).head(10)

fig5, ax5 = plt.subplots()
installs.plot(kind='bar', ax=ax5, color='orange')

ax5.set_title("Category Installs")
ax5.set_ylabel("Total Installs")

# ✅ FIX SCIENTIFIC NOTATION HERE ALSO
ax5.ticklabel_format(style='plain', axis='y')

st.pyplot(fig5)
plt.clf()
