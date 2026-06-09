import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Play Store Analysis Dashboard")

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
# FORMAT FUNCTION (Cr / L / K)
# -------------------------------
def format_indian(num):
    if num >= 1e7:
        return f"{num/1e7:.1f} Cr"
    elif num >= 1e5:
        return f"{num/1e5:.1f} L"
    elif num >= 1e3:
        return f"{num/1e3:.1f} K"
    else:
        return str(int(num))

# -------------------------------
# 🔥 TOP APPS BY INSTALLS
# -------------------------------
st.subheader("🔥 Top Apps by Installs")

top_apps = df.sort_values(by='Installs', ascending=False).head(10)

fig1, ax1 = plt.subplots(figsize=(10,5))
ax1.bar(top_apps['App'], top_apps['Installs'])

ax1.set_title("Top Apps by Installs")
ax1.set_xlabel("Apps")
ax1.set_ylabel("Installs (Cr / L / K)")

# ✅ HUMAN READABLE Y AXIS
ax1.set_yticklabels([format_indian(x) for x in ax1.get_yticks()])

# 📌 SUBTITLE
ax1.text(0.5, -0.25,
         "Values shown in Crore / Lakh / Thousand",
         transform=ax1.transAxes,
         ha='center')

plt.xticks(rotation=45, ha='right')
st.pyplot(fig1)
plt.clf()

# -------------------------------
# ⭐ CATEGORY RATING
# -------------------------------
st.subheader("⭐ Category vs Rating")

cat_rating = df.groupby('Category')['Rating'].mean().sort_values(ascending=False).head(10)

fig2, ax2 = plt.subplots()
cat_rating.plot(kind='bar', ax=ax2)

ax2.set_title("Category Rating")

st.pyplot(fig2)
plt.clf()

# -------------------------------
# 💰 FREE VS PAID PIE
# -------------------------------
st.subheader("💰 Free vs Paid Apps")

type_counts = df['Type'].value_counts()

fig3, ax3 = plt.subplots()
ax3.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%')

ax3.set_title("Free vs Paid Apps")

st.pyplot(fig3)
plt.clf()

# -------------------------------
# 📊 CATEGORY INSTALLS
# -------------------------------
st.subheader("📲 Category Installs")

installs = df.groupby('Category')['Installs'].sum().sort_values(ascending=False).head(10)

fig4, ax4 = plt.subplots()
ax4.bar(installs.index, installs.values)

ax4.set_ylabel("Installs (Cr / L / K)")

# ✅ HUMAN FORMAT Y AXIS
ax4.set_yticklabels([format_indian(x) for x in ax4.get_yticks()])

plt.xticks(rotation=45, ha='right')
st.pyplot(fig4)
plt.clf()
