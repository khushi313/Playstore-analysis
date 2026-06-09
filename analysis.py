import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Play Store Dashboard", layout="wide")

st.title("📊 Play Store Analysis Dashboard (Simple Version)")

# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv("dataset.csv")
df = df.dropna(subset=['Rating'])

# -------------------------------
# CLEAN DATA
# -------------------------------
df['Installs'] = df['Installs'].astype(str).str.replace('+','', regex=False).str.replace(',','', regex=False)
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')

df['Price'] = df['Price'].astype(str).str.replace('$','', regex=False)
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# -------------------------------
# SIMPLE FORMAT FUNCTION (K / L / Cr)
# -------------------------------
def format_num(num):
    if num >= 1e7:
        return f"{num/1e7:.1f} Cr"
    elif num >= 1e5:
        return f"{num/1e5:.1f} L"
    elif num >= 1e3:
        return f"{num/1e3:.1f} K"
    else:
        return str(int(num))

# -------------------------------
# 🔥 TOP APPS
# -------------------------------
st.subheader("🔥 Top 10 Apps by Installs")

top_apps = df.sort_values(by='Installs', ascending=False).head(10)

fig1, ax1 = plt.subplots(figsize=(10,5))
ax1.bar(top_apps['App'], top_apps['Installs'])

ax1.set_title("Top Apps by Installs")
ax1.set_xlabel("Apps")
ax1.set_ylabel("Installs")

ax1.set_yticklabels([format_num(x) for x in ax1.get_yticks()])

plt.xticks(rotation=45, ha='right')
st.pyplot(fig1)
plt.clf()

# -------------------------------
# ⭐ CATEGORY RATING
# -------------------------------
st.subheader("⭐ Top Categories by Rating")

cat_rating = df.groupby('Category')['Rating'].mean().sort_values(ascending=False).head(10)

fig2, ax2 = plt.subplots()
ax2.bar(cat_rating.index, cat_rating.values)

ax2.set_title("Category Ratings")
plt.xticks(rotation=45, ha='right')

st.pyplot(fig2)
plt.clf()

# -------------------------------
# 💰 FREE vs PAID PIE CHART
# -------------------------------
st.subheader("💰 Free vs Paid Apps")

type_counts = df['Type'].value_counts()

fig3, ax3 = plt.subplots()
ax3.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%')

ax3.set_title("App Type Distribution")

st.pyplot(fig3)
plt.clf()

# -------------------------------
# 📊 RATING DISTRIBUTION
# -------------------------------
st.subheader("📊 Rating Distribution")

fig4, ax4 = plt.subplots()
ax4.hist(df['Rating'], bins=10, color='skyblue', edgecolor='black')

ax4.set_title("How Apps Are Rated")
ax4.set_xlabel("Rating")
ax4.set_ylabel("Number of Apps")

st.pyplot(fig4)
plt.clf()

# -------------------------------
# 📲 CATEGORY INSTALLS
# -------------------------------
st.subheader("📲 Category-wise Installs")

installs = df.groupby('Category')['Installs'].sum().sort_values(ascending=False).head(10)

fig5, ax5 = plt.subplots()
ax5.bar(installs.index, installs.values)

ax5.set_title("Top Categories by Installs")
ax5.set_ylabel("Installs")

ax5.set_yticklabels([format_num(x) for x in ax5.get_yticks()])

plt.xticks(rotation=45, ha='right')
st.pyplot(fig5)
plt.clf()
