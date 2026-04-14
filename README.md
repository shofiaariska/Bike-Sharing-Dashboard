# Bike Sharing Dashboard 🚲
## Deskripsi Proyek

Proyek ini bertujuan untuk menganalisis data penyewaan sepeda (*bike sharing dataset*) dan menyajikannya dalam bentuk visualisasi interaktif menggunakan **Streamlit**.

Analisis dilakukan untuk memahami pola penggunaan sepeda berdasarkan waktu, musim, dan kondisi cuaca, sehingga dapat membantu pengambilan keputusan berbasis data.

---

## Struktur Direktori

```bash
submission/
├── dashboard.py
├── main_data.csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

---

## Setup Environment

### 1. Clone Repository / Siapkan Folder

Pastikan semua file berada dalam satu folder sesuai struktur di atas.

---

### 2. Install Dependencies

Jalankan perintah berikut di terminal:

```bash
pip install -r requirements.txt
```

---

### 3. Jalankan Dashboard

Gunakan perintah berikut:

```bash
streamlit run dashboard.py
```

Dashboard akan terbuka otomatis di browser.

---

## Insight Analisis

Berdasarkan hasil eksplorasi data, diperoleh beberapa insight penting:

### Pola Penyewaan Berdasarkan Jam

* Penyewaan sepeda meningkat pada jam sibuk (*rush hour*), terutama:

  * Pagi hari (sekitar jam 07–09)
  * Sore hari (sekitar jam 17–19)
* Hal ini menunjukkan penggunaan sepeda dominan untuk aktivitas kerja atau sekolah.

---

### Pengaruh Cuaca

* Kondisi cuaca cerah memiliki jumlah penyewaan tertinggi.
* Cuaca buruk (hujan/kabut) menurunkan jumlah penyewaan secara signifikan.
* Artinya, cuaca menjadi faktor penting dalam keputusan pengguna.

---

### Pengaruh Musim

* Musim dengan cuaca lebih hangat (misalnya summer) cenderung memiliki jumlah penyewaan lebih tinggi.
* Musim dingin atau kondisi ekstrem menyebabkan penurunan penggunaan sepeda.

---

### Hari Kerja vs Libur

* Pada hari kerja, penyewaan lebih tinggi di jam sibuk (pola commuting).
* Pada hari libur, pola lebih merata sepanjang hari.

---

## Teknologi yang Digunakan

* Python
* Pandas
* Matplotlib & Seaborn
* Streamlit

---

## Catatan

* Pastikan file `main_data.csv` tersedia di direktori yang sama dengan `dashboard.py`
* Gunakan Python versi 3.8 atau lebih baru

---

## Author

Proyek ini dibuat untuk keperluan analisis data dan submission.

---
