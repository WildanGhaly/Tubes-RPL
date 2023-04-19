# Tugas Besar Mata Kuliah Rekayasa Perangkat Lunak IF2250
> Tugas Besar: Implementasi Perancangan Perangkat Lunak

## Anggota Kelompok
<table>
    <tr>
        <td colspan="3", align = "center"><center>Nama Program: Hear Ur Feelings Tool (H.U.F.T)</center></td>
    </tr>
    <tr>
        <td>No.</td>
        <td>Nama</td>
        <td>NIM</td>
    </tr>
    <tr>
        <td>1.</td>
        <td>Jason Rivalino</td>
        <td>13521008</td>
    </tr>
    <tr>
        <td>2.</td>
        <td>Christophorus Dharma Winata</td>
        <td>13521009</td>
    </tr>
    <tr>
        <td>3.</td>
        <td>Haikal Ardzi Shofiyyurrohman</td>
        <td>13521012</td>
    </tr>
    <tr>
        <td>4.</td>
        <td>Hidayatullah Wildan Ghaly Buchary</td>
        <td>13521015</td>
    </tr>
    <tr>
        <td>5.</td>
        <td>Muhammad Haidar Akita Tresnadi</td>
        <td>13521025</td>
    </tr>
</table>

## Table of Contents
* [Deskripsi Singkat](#deskripsi-singkat)
* [Struktur File](#struktur-file)
* [Requirements](#requirements)
* [Cara Menjalankan Program](#cara-menjalankan-program)
* [Daftar Modul](#daftar-modul)
* [Acknowledgements](#acknowledgements)

## Deskripsi Singkat 
Hear Ur Feelings Tool (H.U.F.T) adalah sebuah aplikasi perangkat lunak yang mencatat suasana hati keseharian dari penggunanya. Dalam aplikasi ini, pengguna bisa mengekspresikan suasana hatinya. Aplikasi ini nantinya juga bisa mengolah data dan memprediksi suasana hati pengguna. Selain itu, aplikasi ini juga dapat membantu untuk memberikan motivasi dan semangat kepada pengguna. Aplikasi ini dibuat untuk satu pengguna dimana pengguna tidak perlu untuk melakukan registrasi atau login dalam mencatat mood kesehariannya. Saat membuka aplikasi, pengguna akan diberi kata-kata mutiara atau suatu quote random untuk membantu pengguna dalam menghadapi mood yang dirasakannya. Pengguna juga dapat menambahkan quote sendiri yang dapat diubah dan dihapus ke depannya. Di dalam aplikasi, pengguna dapat memasukkan kondisi mood harian yang dialaminya. Mood yang dapat dicatat antara lain kondisi mood terror, grief, rage, loathing, vigilance, ecstasy, amazement, dan admiration (diambil dari Plutchik Wheel Of Emotions). Mood yang dimasukkan juga dapat disunting setelahnya. Jika pengguna sudah melakukan pengisian kondisi mood selama 15 hari, aplikasi akan menampilkan prediksi mood dan pengguna bisa memberi masukkan terkait hasil prediksi tersebut. Selain masukan mood, aplikasi ini juga menyediakan fitur pencatatan jurnal harian yang bisa menjadi semacam notes untuk mencatat keseharian pengguna dan riwayat tidur untuk mencatat lama waktu tidur malam hari. Riwayat masukan mood dan riwayat tidur dapat dilihat pada aplikasi dalam bentuk statistik atau grafik sederhana. Hasil catatan jurnal juga dapat dicek riwayatnya dalam bentuk tabel sederhana.

## Struktur File
```bash
📦Tucil2_13521008
 ┣ 📂doc
 ┣ 📂img
 ┣ 📂src
 ┗ 📜README.md
 ```
 
## Requirements
1. Bahasa Pemrograman Python (sudah dilengkapi dengan library pyqt5 dan matplotlib)

Instalasi pada terminal:
```bash
pip install pyqt5
pip install matplotlib
```

2. Aplikasi Code Runner (Rekomendasi: Visual Studio Code)


## Cara Menjalankan Program
Langkah-langkah proses setup program adalah sebagai berikut:
1. Clone Repository Github ini
2. Run program dengan mengetikkan `py src/Main.py` pada terminal pada directory yang sesuai dengan directory lokasi clone program 

## Daftar Modul
<table>
    <tr>
        <td>No.</td>
        <td colspan="2", align= "center">Nama Modul</td>
        <td>Implementasi</td>
    </tr>
    <tr>
        <td>1.</td>
        <td colspan="2", align= "left">Main Menu</td>
        <td>13521008</td>
    </tr>
    <tr>
        <td>2.</td>
        <td colspan="2", align= "left">Mood</td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td>a.</td>
        <td>Mood Input</td>
        <td>13521008, 13521015</td>
    </tr>
    <tr>
        <td></td>
        <td>b.</td>
        <td>Mood Visualization</td>
        <td>13521015</td>
    </tr>
    <tr>
        <td></td>
        <td>c.</td>
        <td>Mood Prediction</td>
        <td>13521015</td>
    </tr>
    <tr>
        <td>3.</td>
        <td colspan="2", align= "left">Journal</td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td>a.</td>
        <td>Journal Input</td>
        <td>13521009</td>
    </tr>
    <tr>
        <td></td>
        <td>b.</td>
        <td>Journal List</td>
        <td>13521009</td>
    </tr>
        <tr>
        <td>4.</td>
        <td colspan="2", align= "left">Sleep</td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td>a.</td>
        <td>Sleep Input</td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td>b.</td>
        <td>Sleep Visualization</td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td>c.</td>
        <td>Sleep Recommendation</td>
        <td></td>
    </tr>
    </tr>
        <tr>
        <td>5.</td>
        <td colspan="2", align= "left">Quotes</td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td>a.</td>
        <td>Choose Option</td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td>b.</td>
        <td>Add Quotes</td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td>c.</td>
        <td>Edit Quotes</td>
        <td></td>
    </tr>
    <tr>
        <td>6.</td>
        <td colspan="2", align= "left">Information</td>
        <td>13521008, 13521015</td>
    </tr>
</table>


## Daftar Tabel Basis Data



## Acknowledgements
- Tuhan Yang Maha Esa
- Dosen Mata Kuliah yaitu Pak Rinaldi (K1), Bu Ulfa (K2), dan Pak Rila (K3)
- Kakak-Kakak Asisten Mata Kuliah Strategi Algoritma IF2211
