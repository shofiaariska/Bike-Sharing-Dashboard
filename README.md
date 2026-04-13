# Bike-Sharing-Dashboard

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis data penyewaan sepeda guna memahami pola penggunaan berdasarkan waktu (jam) dan kondisi cuaca selama periode 2011–2012.

Analisis dilakukan menggunakan Python, dan hasilnya divisualisasikan dalam bentuk dashboard interaktif menggunakan Streamlit untuk membantu pengambilan keputusan berbasis data.

---

## Pertanyaan Bisnis
1. Dalam periode Januari–Desember 2012, pada jam berapa saja (per jam) dan kondisi cuaca apa terjadi puncak penyewaan sepeda, dan bagaimana perusahaan harus menyesuaikan strategi distribusi sepeda serta promosi harian untuk memaksimalkan penggunaan pada jam-jam tersebut?
2. Selama empat musim di tahun 2012, musim mana yang menghasilkan pertumbuhan penyewaan tertinggi dibandingkan tahun sebelumnya, dan strategi apa yang harus diterapkan untuk meningkatkan permintaan pada musim dengan performa terendah dalam 3 bulan ke depan?

---

## Setup Environment
## Menggunakan Anaconda
conda create --name bike-ds python=3.9 -y
conda activate bike-ds
pip install --upgrade pip
pip install -r requirements.txt
## Menggunakan Terminal / Shell 
# Membuat folder project 
mkdir bike_sharing_analysis
cd bike_sharing_analysis

# Membuat virtual environment
python -m venv venv

# Aktivasi environment
# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

## Menjalankan Dashboard
python -m streamlit run dashboard.py

## Struktur Proyek
submission/
├── dashboard/
│   ├── main_data.csv
│   └── dashboard.py
│
├── data/
│   ├── hour.csv
│   └── day.csv
│
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt

## Insight
1. Puncak Penyewaan Berdasarkan Jam & Cuaca (2012)
Puncak penyewaan terjadi pada:
Pagi (07.00–09.00)
Sore (17.00–19.00)
Penyewaan tertinggi terjadi pada cuaca cerah
Cuaca buruk menyebabkan penurunan signifikan, termasuk pada jam sibuk

Implikasi:
Pola ini menunjukkan penggunaan dominan untuk aktivitas komuter
Rekomendasi:
Tambahkan distribusi sepeda pada jam sibuk
Fokuskan promosi saat cuaca cerah
Berikan insentif saat cuaca buruk

2. Analisis Musim & Pertumbuhan Penyewaan
Musim dengan performa tertinggi: musim panas dan gugur
Musim dengan performa terendah: musim dingin
Pertumbuhan penyewaan lebih tinggi pada musim dengan cuaca hangat
Cuaca hangat meningkatkan aktivitas luar ruangan dan penggunaan sepeda
Rekomendasi (untuk 3 bulan ke depan):
Fokus peningkatan pada musim dingin:
Promo diskon / cashback
Kampanye penggunaan sepeda
Distribusi di area strategis (kantor, kampus, transport hub)
