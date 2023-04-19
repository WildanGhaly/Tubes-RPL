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
* [Tampilan Interface Program](#tampilan-interface-program)
* [Daftar Tabel Basis Data](#daftar-tabel-basis-data)
* [Acknowledgements](#acknowledgements)


## Deskripsi Singkat 
Hear Ur Feelings Tool (H.U.F.T) adalah sebuah aplikasi perangkat lunak yang mencatat suasana hati keseharian dari penggunanya. Dalam aplikasi ini, pengguna bisa mengekspresikan suasana hatinya. Aplikasi ini nantinya juga bisa mengolah data dan memprediksi suasana hati pengguna. Selain itu, aplikasi ini juga dapat membantu untuk memberikan motivasi dan semangat kepada pengguna. Aplikasi ini dibuat untuk satu pengguna dimana pengguna tidak perlu untuk melakukan registrasi atau login dalam mencatat mood kesehariannya. Saat membuka aplikasi, pengguna akan diberi kata-kata mutiara atau suatu quote random untuk membantu pengguna dalam menghadapi mood yang dirasakannya. Pengguna juga dapat menambahkan quote sendiri yang dapat diubah dan dihapus ke depannya. Di dalam aplikasi, pengguna dapat memasukkan kondisi mood harian yang dialaminya. Mood yang dapat dicatat antara lain kondisi mood terror, grief, rage, loathing, vigilance, ecstasy, amazement, dan admiration (diambil dari Plutchik Wheel Of Emotions). Mood yang dimasukkan juga dapat disunting setelahnya. Jika pengguna sudah melakukan pengisian kondisi mood selama 15 hari, aplikasi akan menampilkan prediksi mood dan pengguna bisa memberi masukkan terkait hasil prediksi tersebut. Selain masukan mood, aplikasi ini juga menyediakan fitur pencatatan jurnal harian yang bisa menjadi semacam notes untuk mencatat keseharian pengguna dan riwayat tidur untuk mencatat lama waktu tidur malam hari. Riwayat masukan mood dan riwayat tidur dapat dilihat pada aplikasi dalam bentuk statistik atau grafik sederhana. Hasil catatan jurnal juga dapat dicek riwayatnya dalam bentuk tabel sederhana.

## Struktur File
```bash
📦Tucil2_13521008
 ┣ 📂bin
 ┣ 📂doc
 ┃ ┣ 📜Change Background.png
 ┃ ┣ 📜Get Quotes.png
 ┃ ┣ 📜Journal Input.png
 ┃ ┣ 📜Journal List.png
 ┃ ┣ 📜Main Menu.png
 ┃ ┣ 📜Mood Input.png
 ┃ ┣ 📜Mood Prediction Rate.png 
 ┃ ┣ 📜Mood Prediction.png
 ┃ ┣ 📜Mood Visualization.png
 ┃ ┣ 📜Quotes Delete.png
 ┃ ┣ 📜Quotes Edit.png
 ┃ ┣ 📜Quotes Input.png
 ┃ ┣ 📜Select Quotes Menu.png 
 ┃ ┣ 📜Sleep Recommendation.png
 ┃ ┣ 📜Sleep Time Input.png
 ┃ ┗ 📜Sleep Time Visualization.png 
 ┣ 📂image
 ┃ ┣ 📂Information
 ┃ ┃ ┗ 📜showinfo.png
 ┃ ┣ 📂Journal
 ┃ ┃ ┣ 📜background.jpg
 ┃ ┃ ┣ 📜journal input fg.png
 ┃ ┃ ┗ 📜journal list fg.png
 ┃ ┣ 📂Main Menu
 ┃ ┃ ┣ 📜background.jpg
 ┃ ┃ ┣ 📜bgtemp1.jpg
 ┃ ┃ ┣ 📜bgtemp2.jpg
 ┃ ┃ ┣ 📜changebg.png
 ┃ ┃ ┣ 📜display.png
 ┃ ┃ ┣ 📜infobutton.png 
 ┃ ┃ ┣ 📜journalbutton.png 
 ┃ ┃ ┣ 📜mainmenu.jpg
 ┃ ┃ ┣ 📜moodbutton.png 
 ┃ ┃ ┣ 📜quit.png
 ┃ ┃ ┣ 📜quotesbutton.png
 ┃ ┃ ┗ 📜sleepbutton.png
 ┃ ┣ 📂Mood
 ┃ ┃ ┣ 📜SubmitButton.png
 ┃ ┃ ┣ 📜SubmitButtonNoText.png
 ┃ ┃ ┣ 📜default_background.jpg
 ┃ ┃ ┣ 📜mood input fg with back.png
 ┃ ┃ ┣ 📜mood input fg.png
 ┃ ┃ ┣ 📜mood prediction fg.png
 ┃ ┃ ┣ 📜mood prediction rate fg.png
 ┃ ┃ ┣ 📜mood visualization fg.png
 ┃ ┃ ┣ 📜mood_input.jpg
 ┃ ┃ ┣ 📜mood_input_rev1.jpg
 ┃ ┃ ┣ 📜mood_prediction.jpg
 ┃ ┃ ┣ 📜mood_prediction_rate.jpg
 ┃ ┃ ┣ 📜mood_visual.jpg
 ┃ ┃ ┣ 📜new bg mood input fg.png
 ┃ ┃ ┣ 📜new bg mood prediction fg.png
 ┃ ┃ ┣ 📜new bg mood prediction rate fg.png
 ┃ ┃ ┣ 📜new bg mood visualization fg.png
 ┃ ┃ ┣ 📜next button.png
 ┃ ┃ ┗ 📜submit button.png
 ┃ ┣ 📂Quotes
 ┃ ┃ ┣ 📜mendapat quotes fg black.png
 ┃ ┃ ┣ 📜quotes delete.png
 ┃ ┃ ┣ 📜quotes edit fg black.png
 ┃ ┃ ┣ 📜quotes input fg black.png
 ┃ ┃ ┣ 📜select quotes menu fg black.png 
 ┃ ┃ ┗ 📜select quotes menu fg.png
 ┃ ┣ 📂Sleep
 ┃ ┃ ┣ 📜andaBermasalah.png
 ┃ ┃ ┣ 📜background.jpg
 ┃ ┃ ┣ 📜bearChronoType.png 
 ┃ ┃ ┣ 📜dolphinChronoType.png
 ┃ ┃ ┣ 📜lionChronoType.png
 ┃ ┃ ┣ 📜sleep recommendation fg.png
 ┃ ┃ ┣ 📜sleep time input fg.png 
 ┃ ┃ ┣ 📜sleep time visualization fg.png
 ┃ ┃ ┗ 📜wolfChronoType.png
 ┃ ┣ 📜background.jpg
 ┃ ┣ 📜bgtemp0.jpg
 ┃ ┣ 📜bgtemp1.jpg
 ┃ ┗ 📜bgtemp2.jpg
 ┣ 📂src
 ┃ ┣ 📂Information
 ┃ ┃ ┣ 📜information.py
 ┃ ┃ ┗ 📜information_GUI.py
 ┃ ┣ 📂Journal
 ┃ ┃ ┣ 📜Journal.py
 ┃ ┃ ┣ 📜JournalDatabase.py
 ┃ ┃ ┣ 📜JournalInput_Call.py
 ┃ ┃ ┣ 📜JournalInput_GUI.py
 ┃ ┃ ┣ 📜JournalList_Call.py
 ┃ ┃ ┣ 📜JournalList_GUI.py 
 ┃ ┃ ┗ 📜Journal_rc.py
 ┃ ┣ 📂MainMenu
 ┃ ┃ ┣ 📜main_menu_GUI.py 
 ┃ ┃ ┗ 📜mainmenu.py
 ┃ ┣ 📂Mood
 ┃ ┃ ┣ 📜mood.py
 ┃ ┃ ┣ 📜mood_pyqt.py
 ┃ ┃ ┣ 📜mood_pyqt_feedback.py
 ┃ ┃ ┣ 📜mood_pyqt_prediction.py
 ┃ ┃ ┣ 📜mood_pyqt_visual.py
 ┃ ┃ ┣ 📜mood_pyqt_visual_calendar.py 
 ┃ ┃ ┣ 📜mood_service.py
 ┃ ┃ ┣ 📜moodinput.py
 ┃ ┃ ┣ 📜moodvisualize.py
 ┃ ┃ ┣ 📜resource_rc.py 
 ┃ ┃ ┣ 📜ui_mood_feedback.py
 ┃ ┃ ┣ 📜ui_mood_input_rev1.py 
 ┃ ┃ ┣ 📜ui_mood_prediction.py
 ┃ ┃ ┣ 📜ui_mood_visual.py
 ┃ ┃ ┗ 📜ui_mood_visual_calendar.py
 ┃ ┣ 📂Quotes
 ┃ ┃ ┣ 📜Choose_Call.py
 ┃ ┃ ┣ 📜Choose_GUI.py
 ┃ ┃ ┣ 📜Quotes.py
 ┃ ┃ ┣ 📜Quotes_Delete_GUI.py
 ┃ ┃ ┣ 📜Quotes_GUI(old).py
 ┃ ┃ ┣ 📜Quotes_Input_Call.py
 ┃ ┃ ┣ 📜Quotes_Input_GUI.py
 ┃ ┃ ┣ 📜Quotes_Popup.py
 ┃ ┃ ┣ 📜Quotes_Popup_Call.py
 ┃ ┃ ┣ 📜Quotes_Service.py
 ┃ ┃ ┣ 📜Quotes_delete_Call.py
 ┃ ┃ ┣ 📜Quotes_edit_Call.py
 ┃ ┃ ┣ 📜Quotes_edit_Call.py
 ┃ ┃ ┣ 📜rc_choose(old).py
 ┃ ┃ ┣ 📜rc_choose.py
 ┃ ┃ ┣ 📜rc_edit(old).py
 ┃ ┃ ┣ 📜rc_edit.py
 ┃ ┃ ┣ 📜rc_input(old).py
 ┃ ┃ ┣ 📜rc_input.py
 ┃ ┃ ┗ 📜rc_popup.py
 ┃ ┣ 📂Sleep
 ┃ ┃ ┣ 📜Sleep.py
 ┃ ┃ ┣ 📜Sleep_Input_GUI.py 
 ┃ ┃ ┣ 📜Sleep_Plot.py
 ┃ ┃ ┣ 📜Sleep_Recommendation.py
 ┃ ┃ ┣ 📜Sleep_Service.py
 ┃ ┃ ┣ 📜Sleep_Visualization_GUI.py
 ┃ ┃ ┗ 📜resource_rc.py
 ┃ ┗ 📜main.py
 ┗ 📜README.md
 ```
 
## Requirements
1. Bahasa Pemrograman Python (sudah dilengkapi dengan library pyqt5, matplotlib, plotly)

Instalasi pada terminal:
```bash
pip install pyqt5
pip install matplotlib
pip install plotly
```

2. Aplikasi Code Runner (Rekomendasi: Visual Studio Code)


## Cara Menjalankan Program
Langkah-langkah proses setup program adalah sebagai berikut:
1. Clone Repository Github ini
2. Run program dengan mengetikkan `cd src` untuk berpindah ke directory src, lalu ketikkan `Main.py` pada terminal

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
        <td>13521008, 13521012</td>
    </tr>
    <tr>
        <td>2.</td>
        <td colspan="3", align= "left">Mood</td>
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
        <td colspan="3", align= "left">Journal</td>
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
        <td colspan="3", align= "left">Sleep</td>
    </tr>
    <tr>
        <td></td>
        <td>a.</td>
        <td>Sleep Input</td>
        <td>13521012, 13521025</td>
    </tr>
    <tr>
        <td></td>
        <td>b.</td>
        <td>Sleep Visualization</td>
        <td>13521012</td>
    </tr>
    <tr>
        <td></td>
        <td>c.</td>
        <td>Sleep Recommendation</td>
        <td>13521012</td>
    </tr>
    </tr>
        <tr>
        <td>5.</td>
        <td colspan="3", align= "left">Quotes</td>
    </tr>
    <tr>
        <td></td>
        <td>a.</td>
        <td>Choose Option</td>
        <td>13521025</td>
    </tr>
    <tr>
        <td></td>
        <td>b.</td>
        <td>Add Quotes</td>
        <td>13521015, 13521025</td>
    </tr>
    <tr>
        <td></td>
        <td>c.</td>
        <td>Edit Quotes</td>
        <td>13521025</td>
    </tr>
    <tr>
        <td></td>
        <td>d.</td>
        <td>Delete Quotes</td>
        <td>13521025</td>
    </tr>
    <tr>
        <td>6.</td>
        <td colspan="2", align= "left">Information</td>
        <td>13521008, 13521015</td>
    </tr>
    <tr>
        <td>7.</td>
        <td colspan="2", align= "left">Module Design</td>
        <td>13521008</td>
    </tr>
</table>

## Tampilan Interface Program
![Screenshot 2023-04-19 172424](https://user-images.githubusercontent.com/91790457/233046998-b8c59510-17d7-4b7a-b4ae-d5108b96ece4.png)


## Daftar Tabel Basis Data
<h4>Mood.csv</h4>
<table>
    <tr>
        <td colspan="10", align = "center"><center>Atribut</center></td>
    </tr>
    <tr>
        <td>Date</td>
        <td>ID</td>
        <td>Joy</td>
        <td>Sadness</td>
        <td>Anger</td>
        <td>Fear</td>
        <td>Disgust</td>
        <td>Surprise</td>
        <td>Trust</td>
        <td>Anticipation</td>
    </tr>
</table>

<h4>Feedback.csv</h4>
<table>
    <tr>
        <td colspan="2", align = "center"><center>Atribut</center></td>
    </tr>
    <tr>
        <td>Rating</td>
        <td>Feedback</td>
    </tr>
</table>

<h4>Journal.csv</h4>
<table>
    <tr>
        <td colspan="3", align = "center"><center>Atribut</center></td>
    </tr>
    <tr>
        <td>ID</td>
        <td>IsiJournal</td>
        <td>JudulJournal</td>
    </tr>
</table>

<h4>Sleep.csv</h4>
<table>
    <tr>
        <td colspan="6", align = "center"><center>Atribut</center></td>
    </tr>
    <tr>
        <td>ID(HHBBTTTTJJMM)</td>
        <td>jamTidurStart</td>
        <td>menitTidurStart</td>
        <td>jamTidurEnd</td>
        <td>menitTidurEnd</td>
        <td>durasi(menit)</td>
    </tr>
</table>

<h4>Quotes.csv</h4>
<table>
    <tr>
        <td colspan="2", align = "center"><center>Atribut</center></td>
    </tr>
    <tr>
        <td>Number</td>
        <td>Quote</td>
    </tr>
</table>

## Acknowledgements
- Tuhan Yang Maha Esa
- Dosen Mata Kuliah Rekayasa Perangkat Lunak IF2250
- Kakak-Kakak Asisten Mata Kuliah Rekayasa Perangkat Lunak IF2250
