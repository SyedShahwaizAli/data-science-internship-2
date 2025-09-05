import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    return pd.read_csv("Global_Superstore.csv", encoding="ISO-8859-1")

df = load_data()

st.title("📊 Global Superstore Business Dashboard")

st.write("### Sample Data")
st.dataframe(df.head(20))

st.sidebar.header("Filters")
region = st.sidebar.multiselect("Select Region(s):", df["Region"].unique(), default=df["Region"].unique())
category = st.sidebar.multiselect("Select Category(s):", df["Category"].unique(), default=df["Category"].unique())
sub_category = st.sidebar.multiselect("Select Sub-Category(s):", df["Sub-Category"].unique(), default=df["Sub-Category"].unique())

df_filtered = df[(df["Region"].isin(region)) & (df["Category"].isin(category)) & (df["Sub-Category"].isin(sub_category))]

total_sales = df_filtered["Sales"].sum()
total_profit = df_filtered["Profit"].sum()
top_customers = df_filtered.groupby("Customer Name")["Sales"].sum().nlargest(5)

st.subheader("Key Performance Indicators")
col1, col2 = st.columns(2)
col1.metric("💰 Total Sales", f"${total_sales:,.2f}")
col2.metric("📈 Total Profit", f"${total_profit:,.2f}")

st.subheader("Sales & Profit by Category")
cat_summary = df_filtered.groupby("Category")[["Sales","Profit"]].sum().reset_index()
fig, ax = plt.subplots()
cat_summary.plot(x="Category", y=["Sales","Profit"], kind="bar", ax=ax)
st.pyplot(fig)

st.subheader("Top 5 Customers by Sales")
fig, ax = plt.subplots()
top_customers.plot(kind="bar", ax=ax, color="skyblue")
plt.ylabel("Sales")
st.pyplot(fig)

st.subheader("Region-wise Sales")
region_summary = df_filtered.groupby("Region")["Sales"].sum().reset_index()
fig, ax = plt.subplots()
sns.barplot(x="Region", y="Sales", data=region_summary, ax=ax)
st.pyplot(fig)
