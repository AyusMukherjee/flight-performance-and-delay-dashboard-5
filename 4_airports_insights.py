import streamlit as st
import pandas as pd
import plotly.express as px
from utils.weather_api import get_current_weather

st.set_page_config(page_title="Airport Insights", layout="wide")
st.title("🛬 Origin Airport Delay Insights")

df = pd.read_csv("data/data1.csv", parse_dates=["FL_DATE"])

st.subheader("Average Delay by Airport")
delay_by_airport = df.groupby("ORIGIN")["DEP_DELAY"].mean().sort_values(ascending=False).head(15)
fig1 = px.bar(delay_by_airport, title="Top Airports by Avg Departure Delay")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Flight Volume by Airport")
volume_by_airport = df["ORIGIN"].value_counts().head(15)
fig2 = px.bar(volume_by_airport, title="Flight Volume per Origin Airport")
st.plotly_chart(fig2, use_container_width=True)



