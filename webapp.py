import streamlit as st
import plotly.express as px
import sqlite3

connection = sqlite3.connect("tempData.db")
cursor = connection.cursor()

cursor.execute("SELECT date FROM temperature")
date = cursor.fetchall()
exact_date = [item[0] for item in date]

cursor.execute("SELECT temperature FROM temperature")
temperature = cursor.fetchall()
exact_temperature = [item[0] for item in temperature]

figure = px.line(x=exact_date,y=exact_temperature, labels={"x": "Date", "y":"Temperature (C)"})

st.plotly_chart(figure)