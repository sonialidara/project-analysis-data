#Dashboard Streamlit

#Nama : SONIA LIDARA
#ID Dicoding : https://www.dicoding.com/users/sonialidara02/
#Email : sonialidara@gmail.com

# Import Library
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# LOAD DATA


@st.cache_resource
def load_data():
    data = pd.read_csv("./dataset/hour.csv")
    return data


data = load_data()


# TITLE DASHBOARD
# Set page title
st.title("Bike Share Analyst Dashboard")


# SIDEBAR
st.sidebar.title("Contact Person:")
st.sidebar.markdown("**• SONIA LIDARA**")
st.sidebar.markdown(
    "**• Email: [sonialidara@gmail.com](sonialidara@gmail.com)**")
st.sidebar.markdown(
    "**• ID Dicoding: [deemas_dee](https://www.dicoding.com/users/sonialidara02/)**")


st.sidebar.title("Dataset Bike Share")
# Show the dataset
if st.sidebar.checkbox("Show Dataset"):
    st.subheader("Raw Data")
    st.write(data)

# Display summary statistics
if st.sidebar.checkbox("Show Summary Statistics"):
    st.subheader("Summary Statistics")
    st.write(data.describe())

# Show dataset source
st.sidebar.markdown("[Download Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset/)")

st.sidebar.markdown('**Weather:**')
st.sidebar.markdown('1: Cerah, Sedikit awan, Berawan sebagian, Berawan sebagian')
st.sidebar.markdown('2: Kabut + Berawan, Kabut + Awan pecah, Kabut + Sedikit awan, Kabut')
st.sidebar.markdown('3: Salju Ringan, Hujan Ringan + Badai Petir + Awan Tersebar, Hujan Ringan + Awan Tersebar')
st.sidebar.markdown('4: Hujan Lebat + Palet Es + Badai Petir + Kabut, Salju + Kabut')




# VISUALIZATION

# create a layout with two columns
col1, col2 = st.columns(2)

with col1:
    # Season-wise bike share count
    # st.subheader("Season-wise Bike Share Count")

    # Mapping dari angka ke label musim
    season_mapping = {1: "spring", 2: "summer", 3: "fall", 4: "winter"}
    data["season_label"] = data["season"].map(season_mapping)

    season_count = data.groupby("season_label")["cnt"].sum().reset_index()
    fig_season_count = px.bar(season_count, x="season_label",

    y="total_count", title="Jumlah Penyewa berdasarkan Musim")
    y="cnt", title="Season-wise Bike Share Count")
    st.plotly_chart(fig_season_count, use_container_width=True,
    height=400, width=600)

with col2:
    # Weather situation-wise bike share count
    # st.subheader("Weather Situation-wise Bike Share Count")


    weather_count = data.groupby("weather_condition")["total_count"].sum().reset_index()
    fig_weather_count = px.bar(weather_count, x="weather_condition",
                               y="total_count", title="Jumlah Penyewa berdasar Cuaca")

    weather_count = data.groupby("weathersit")["cnt"].sum().reset_index()
    fig_weather_count = px.bar(weather_count, x="weathersit",
                               y="cnt", title="Weather Situation-wise Bike Share Count")

    # Mengatur tinggi dan lebar gambar
    st.plotly_chart(fig_weather_count, use_container_width=True,height=400, width=800)


# Hourly bike share count
# st.subheader("Hourly Bike Share Count")
hourly_count = data.groupby("hr")["cnt"].sum().reset_index()
fig_hourly_count = px.line(
    hourly_count, x="hr", y="cnt", title="Hourly Bike Share Count")
st.plotly_chart(fig_hourly_count, use_container_width=True,
                height=400, width=600)

# Humidity vs. Bike Share Count
# st.subheader("Humidity vs. Bike Share Count")
fig_humidity_chart = px.scatter(
    data, x="hum", y="cnt", title="Humidity vs. Bike Share Count")
st.plotly_chart(fig_humidity_chart)

# Wind Speed vs. Bike Share Count
# st.subheader("Wind Speed vs. Bike Share Count")
fig_wind_speed_chart = px.scatter(
    data, x="windspeed", y="cnt", title="Wind Speed vs. Bike Share Count")
st.plotly_chart(fig_wind_speed_chart)

# Temperature vs. Bike Share Count
# st.subheader("Temperature vs. Bike Share Count")
fig_temp_chart = px.scatter(data, x="temp", y="cnt",
                            title="Temperature vs. Bike Share Count")
st.plotly_chart(fig_temp_chart, use_container_width=True,
                height=400, width=800)

# Show data source and description
st.sidebar.title("About")
st.sidebar.info("Dashboard ini menampilkan visualisasi untuk sekumpulan data Bike Share. "
                "Dataset ini mengandung informasi mengenai penyewaan sepeda berdasarkan berbagai variabel seperti musim, suhu, kelembaban, dan faktor lainnya.")
