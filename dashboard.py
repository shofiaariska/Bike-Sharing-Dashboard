
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('main_data.csv')

st.title('Dashboard Bike Sharing 🚲')

# ===============================
# FILTER
# ===============================
st.sidebar.header('Filter Data')

# Filter Tahun
year = st.sidebar.selectbox('Pilih Tahun', sorted(df['yr'].unique()))

# Filter Jam
hour_range = st.sidebar.slider('Pilih Jam', 0, 23, (0, 23))

# Filter Data
filtered_df = df[
    (df['yr'] == year) &
    (df['hr'] >= hour_range[0]) &
    (df['hr'] <= hour_range[1])
]

# ===============================
# 1. PENYEWAAN BERDASARKAN CUACA
# ===============================
st.subheader('Pengaruh Cuaca terhadap Penyewaan')

weather_data = filtered_df.groupby('weathersit')['cnt'].mean()

fig1, ax1 = plt.subplots()
weather_data.plot(kind='bar', ax=ax1)

ax1.set_title('Rata-rata Penyewaan per Cuaca')
ax1.set_xlabel('Cuaca')
ax1.set_ylabel('Jumlah Penyewaan')

st.pyplot(fig1)

# ===============================
# 2. PENYEWAAN BERDASARKAN MUSIM
# ===============================
st.subheader('Penyewaan Berdasarkan Musim')

season_data = filtered_df.groupby('season')['cnt'].mean()

fig2, ax2 = plt.subplots()
season_data.plot(kind='bar', ax=ax2)
ax2.set_title('Rata-rata Penyewaan per Musim')
st.pyplot(fig2)

# ===============================
# 3. POLA JAM (LANJUTAN)
# ===============================
st.subheader('Pola Penyewaan per Jam')

hour_data = filtered_df.groupby('hr')['cnt'].mean()

fig3, ax3 = plt.subplots()
hour_data.plot(ax=ax3)
ax3.set_title('Penyewaan per Jam')
st.pyplot(fig3)

# ===============================
# 4. HARI KERJA VS LIBUR
# ===============================
st.subheader('Hari Kerja vs Libur')

day_data = filtered_df.groupby('workingday')['cnt'].mean()

fig4, ax4 = plt.subplots()
day_data.plot(kind='bar', ax=ax4)
ax4.set_xticklabels(['Libur', 'Kerja'], rotation=0)
st.pyplot(fig4)
