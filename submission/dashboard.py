import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dashboard Bike Sharing", layout="wide")

# LOAD DATA
df = pd.read_csv('main_data.csv')

# FIX: tambahkan ini
df['dteday'] = pd.to_datetime(df['dteday'])
df['year'] = df['dteday'].dt.year

st.title('Dashboard Bike Sharing 🚲')

# FILTER
st.sidebar.header('Filter Data')

year = st.sidebar.selectbox(
    'Pilih Tahun',
    sorted(df['year'].unique())
)

hour_range = st.sidebar.slider(
    'Pilih Jam',
    0, 23, (0, 23)
)

# FILTER DATA
filtered_df = df[
    (df['year'] == year) &
    (df['hr'] >= hour_range[0]) &
    (df['hr'] <= hour_range[1])
].copy()

# CEK DATA
if filtered_df.empty:
    st.warning("Data tidak tersedia untuk filter yang dipilih.")
else:
    st.subheader("Data yang Ditampilkan")
    st.write(filtered_df.head())

    # GRAFIK JAM
    hourly = filtered_df.groupby('hr')['cnt'].mean().reset_index()

    fig, ax = plt.subplots()
    sns.lineplot(data=hourly, x='hr', y='cnt', ax=ax)
    st.pyplot(fig)

    # GRAFIK MUSIM
    season = filtered_df.groupby('season')['cnt'].mean().reset_index()

    fig2, ax2 = plt.subplots()
    sns.barplot(data=season, x='season', y='cnt', ax=ax2)
    st.pyplot(fig2)