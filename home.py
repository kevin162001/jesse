import streamlit as st
import pandas as pd
from function import load_data
import plotly.express as px
import plotly.graph_objects as go


def app():
    # Judul dan Informasi mengenai Dasboard
    st.title("Dashboard Pemantauan dan Prediksi Banjir Berbasis Curah Hujan di Kabupaten Cilacap :thunder_cloud_and_rain:")
    st.write("Selamat datang di Dashboard Pemantauan dan Prediksi Banjir Berbasis Curah Hujan di **Kabupaten Cilacap**! "
            "Kabupaten Cilacap, Jawa Tengah, sering mengalami masalah banjir, khususnya dalam rentang waktu tahun 2020-2023. " 
            "Dengan menggabungkan data kejadian banjir dari **BNPB** dan informasi curah hujan harian dari **WorldWeatherOnline**, " 
            "kami menciptakan solusi prediktif berupa dashboard ini. Kami menganalisis curah hujan, membuat model forecast,"
            "dan memvisualisasikannya agar dapat memberikan pemahaman yang lebih baik mengenai potensi risiko banjir. " 
            "Dengan fitur-fitur seperti data historis, forecast, dan prediksi kejadian banjir, kami berharap " 
            "dashboard ini dapat menjadi alat yang berguna dalam menghadapi tantangan banjir di **Kabupaten Cilacap**."
            )
    st.info("Semua data curah hujan diukur dalam satuan mm/jam.")

  # Load Dataset
    df = load_data("data/train.csv")

    # Data Historis Banjir
    df_class = df.copy()
    df_class['date'] = pd.to_datetime(df_class['date'])
    df_class.set_index('date', inplace=True)

    # Pemfilteran Data Berdasarkan Range Waktu
    date_range = st.date_input("Pilih Rentang Waktu", [df_class.index.min(), df_class.index.max()], key="date_range")
    start_date, end_date = date_range
    filtered_df_class = df_class.loc[start_date:end_date]

    # Menampilkan Data Historis Banjir
    st.header("Data Historis Kejadian Banjir")
    st.write(filtered_df_class)

    st.header("Visualisasi Tren untuk Masing-masing Variabel")
    st.subheader("Tren Kecepatan Angin Kumulatif")
    fig_iws = px.line(filtered_df_class, x=filtered_df_class.index, y="Iws", title="Tren Kecepatan Angin Kumulatif")
    st.plotly_chart(fig_iws)
