import streamlit as st
import pandas as pd
import plotly.express as px

# Title and description
st.title("🚗 Used Vehicles Dashboard — USA")
st.markdown("""
This interactive dashboard allows you to explore used vehicle listings in the United States.  
You can filter by model year, condition, transmission, fuel type, vehicle type, and paint color.  
Visualizations help you understand how price varies across different features.
""")

# Load and clean data
df = pd.read_csv("vehicles_us.csv")
df = df.dropna()
df = df[(df['price'] > 500) & (df['price'] < 100000)]
df = df.drop_duplicates()

# Sidebar filters
st.sidebar.header("Filters")

years = sorted(df['model_year'].dropna().unique())
years.insert(0, "All")
selected_year = st.sidebar.selectbox("Model Year", years)

conditions = sorted(df['condition'].unique())
conditions.insert(0, "All")
selected_condition = st.sidebar.selectbox("Condition", conditions)

transmissions = sorted(df['transmission'].unique())
transmissions.insert(0, "All")
selected_transmission = st.sidebar.selectbox("Transmission", transmissions)

fuels = sorted(df['fuel'].unique())
fuels.insert(0, "All")
selected_fuel = st.sidebar.selectbox("Fuel Type", fuels)

types = sorted(df['type'].unique())
types.insert(0, "All")
selected_type = st.sidebar.selectbox("Vehicle Type", types)

colors = sorted(df['paint_color'].dropna().unique())
colors.insert(0, "All")
selected_color = st.sidebar.selectbox("Paint Color", colors)

# Apply filters
filtered_df = df.copy()

if selected_year != "All":
    filtered_df = filtered_df[filtered_df['model_year'] == selected_year]

if selected_condition != "All":
    filtered_df = filtered_df[filtered_df['condition'] == selected_condition]

if selected_transmission != "All":
    filtered_df = filtered_df[filtered_df['transmission'] == selected_transmission]

if selected_fuel != "All":
    filtered_df = filtered_df[filtered_df['fuel'] == selected_fuel]

if selected_type != "All":
    filtered_df = filtered_df[filtered_df['type'] == selected_type]

if selected_color != "All":
    filtered_df = filtered_df[filtered_df['paint_color'] == selected_color]

# Key metrics
st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Average Price", f"${filtered_df['price'].mean():,.0f}")
col2.metric("Average Odometer", f"{filtered_df['odometer'].mean():,.0f} mi")
col3.metric("Vehicles Found", f"{len(filtered_df)}")

# Visualizations
st.subheader("Price vs Odometer by Vehicle Type")
fig1 = px.scatter(filtered_df, x="odometer", y="price", color="type", title="Price vs Odometer")
st.plotly_chart(fig1)

st.subheader("Odometer Distribution")
fig2 = px.histogram(filtered_df, x="odometer", nbins=50)
st.plotly_chart(fig2)

st.subheader("Price by Condition")
fig3 = px.box(filtered_df, x="condition", y="price", color="condition")
st.plotly_chart(fig3)

st.subheader("Price Distribution by Type and Model")
fig4 = px.treemap(filtered_df, path=['type', 'model'], values='price', title="Treemap: Type and Model")
st.plotly_chart(fig4)

st.subheader("Price by Vehicle Type")
fig5 = px.box(filtered_df, x="type", y="price", color="type", title="Price by Vehicle Type")
st.plotly_chart(fig5)

# Data table
st.subheader("Filtered Data")
st.dataframe(filtered_df)

# Download button
st.download_button(
    label="Download Filtered Data as CSV",
    data=filtered_df.to_csv(index=False).encode('utf-8'),
    file_name='filtered_vehicles.csv',
    mime='text/csv'
)