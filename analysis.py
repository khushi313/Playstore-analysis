import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Play Store Dashboard (Easy Version)")

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
# 🔍 SEARCH BAR (APP NAME)
# -------------------------------
search_app = st.text_input("🔍 Search App Name")

if search_app:
    df = df[df['App'].str.contains(search_app, case=False, na=False)]

# -------------------------------
# 📂 CATEGORY FILTER
# -------------------------------
category_list = df['Category'].dropna().unique()
selected_category = st.selectbox("📂 Select Category", ["All"] + list(category_list))

if selected_category != "All":
    df = df[df['Category'] == selected_category]

# -------------------------------
# 📊 TOP APPS
# -------------------------------
st.subheader("🔥 Top Apps by Installs")

top_apps = df.sort_values(by='Installs', ascending=False).head(10)

fig1, ax1 = plt.subplots(figsize=(8,4))
ax1.bar(top_apps['App'], top_apps['Installs'])
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
st.pyplot(fig2)
plt.clf()

# -------------------------------
# 💰 PIE CHART: FREE vs PAID
# -------------------------------
st.subheader("💰 Free vs Paid Apps (%)")

type_counts = df['Type'].value_counts()

fig3, ax3 = plt.subplots()
ax3.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%')
ax3.set_title("Free vs Paid Apps Share")

st.pyplot(fig3)
plt.clf()

# -------------------------------
# 📌 INSIGHTS
# -------------------------------
st.subheader("📌 Insights")

st.write("Total Apps:", len(df))
st.write("Top Categories:")
st.dataframe(cat_rating)
