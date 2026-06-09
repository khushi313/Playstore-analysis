import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="centered")

st.title("📊 Play Store Dashboard (Simple & Clean)")

# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv("dataset.csv")
df = df.dropna(subset=['Rating'])

# -------------------------------
# CLEAN INSTALLS
# -------------------------------
df['Installs'] = df['Installs'].astype(str).str.replace('+','', regex=False).str.replace(',','', regex=False)
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')

# -------------------------------
# SIMPLE FORMAT
# -------------------------------
def format_num(n):
    if n >= 1e7:
        return f"{n/1e7:.1f} Cr"
    elif n >= 1e5:
        return f"{n/1e5:.1f} L"
    elif n >= 1e3:
        return f"{n/1e3:.1f} K"
    else:
        return str(int(n))

# -------------------------------
# 🔥 FIX 1: TOP APPS (CLEAR VERSION)
# -------------------------------
st.subheader("🔥 Top 10 Apps by Installs (Clear View)")

top_apps = df[['App','Installs']].dropna().sort_values(by='Installs', ascending=False).head(10)

fig1, ax1 = plt.subplots(figsize=(6,4))  # SMALL SIZE FIX
ax1.barh(top_apps['App'], top_apps['Installs'])  # horizontal bar = EASY READ

ax1.set_xlabel("Installs")
ax1.set_title("Top Apps")

ax1.set_xticklabels([format_num(x) for x in ax1.get_xticks()])

st.pyplot(fig1)
plt.clf()

# -------------------------------
# 🔥 FIX 2: CATEGORY RATING (CLEAN ONLY RATING)
# -------------------------------
st.subheader("⭐ Top Categories by Average Rating")

cat_rating = df.groupby('Category')['Rating'].mean().sort_values(ascending=True).tail(10)

fig2, ax2 = plt.subplots(figsize=(6,4))
ax2.barh(cat_rating.index, cat_rating.values, color='skyblue')

ax2.set_xlabel("Average Rating")
ax2.set_title("Category Rating")

st.pyplot(fig2)
plt.clf()

# -------------------------------
# 💰 PIE CHART (SIMPLE)
# -------------------------------
st.subheader("💰 Free vs Paid Apps")

type_counts = df['Type'].value_counts()

fig3, ax3 = plt.subplots(figsize=(4,4))
ax3.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%')

st.pyplot(fig3)
plt.clf()

# -------------------------------
# 📊 RATING DISTRIBUTION (VERY CLEAR)
# -------------------------------
st.subheader("📊 App Rating Distribution")

fig4, ax4 = plt.subplots(figsize=(6,4))
ax4.hist(df['Rating'], bins=8, color='lightgreen', edgecolor='black')

ax4.set_xlabel("Rating")
ax4.set_ylabel("No. of Apps")

st.pyplot(fig4)
plt.clf()
