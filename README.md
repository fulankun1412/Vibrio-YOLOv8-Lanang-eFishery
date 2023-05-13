# Deteksi dan Penghitungan Bakteri Vibrio dari Cawan Petri Dish menggunakan YOLOv8
Selamat datang di proyek "Deteksi dan Penghitungan Bakteri Vibrio dari Cawan Petri Dish menggunakan YOLOv8"! Proyek ini dibuat sebagai bagian dari tugas take home untuk melamar posisi di eFishery.

## Deskripsi Proyek
Proyek ini bertujuan untuk mengembangkan sebuah sistem yang dapat mendeteksi dan menghitung jumlah bakteri Vibrio dalam gambar cawan Petri Dish menggunakan teknologi YOLOv8. Cawan Petri Dish adalah alat yang sering digunakan dalam penelitian mikrobiologi untuk mengkultur bakteri. Dengan memanfaatkan kemampuan deteksi objek dan komputasi visual dari YOLOv8, proyek ini akan memberikan solusi otomatis yang dapat membantu mempercepat proses identifikasi dan penghitungan bakteri Vibrio.

## Instalasi dan Penggunaan
Berikut adalah langkah-langkah untuk menginstal dan menjalankan proyek ini di local environtment, sangat disarankan untuk menggunakan virtual environment atau sudah terpasang docker:
### Python Lokal
1. Kloning repositori ini: Gunakan perintah git clone untuk mengkloning repositori ini ke direktori lokal.
```
git clone https://github.com/fulankun1412/Vibrio-YOLOv8-Lanang-eFishery.git
```
2. Pengaturan lingkungan virtual (opsional): Disarankan untuk membuat dan mengaktifkan lingkungan virtual Python sebelum melanjutkan instalasi dependensi. Anda dapat menggunakan venv atau alat serupa.
3. Instalasi dependensi: Masuk ke direktori proyek dan jalankan perintah berikut untuk menginstal dependensi yang diperlukan.
```
pip install -r requirements.txt
```
4. Untuk mengeksekusi aplikasi dan sehingga muncul interface aplikasinya, jalankan perintah eksekusi di dalam direktori
```
streamlit run app.py
```
5. Buka browser internet dan masuk ke localhost:8501, aplikasi terbuka selamat mencoba.

### docker-compose
1. Kloning repositori ini: Gunakan perintah git clone untuk mengkloning repositori ini ke direktori lokal.
```
git clone https://github.com/fulankun1412/Vibrio-YOLOv8-Lanang-eFishery.git
```
2. Jalankan perintah `docker-compose` ini untuk mulai build dan menjalankan langsung aplikasi
```
docker-compose up
```
3. Buka browser internet dan masuk ke localhost:8501, aplikasi terbuka selamat mencoba.

## Interface antar muka
### Input gambar
![image](https://github.com/fulankun1412/Vibrio-YOLOv8-Lanang-eFishery/assets/16248869/9dea2503-535f-41e3-bb46-01db01686667)
### Upload Gambar
![image](https://github.com/fulankun1412/Vibrio-YOLOv8-Lanang-eFishery/assets/16248869/3899a2d9-a9fe-4bc0-b627-d0f1a9c33d66)
### Hasil deteksi dan Perhitungan
![image](https://github.com/fulankun1412/Vibrio-YOLOv8-Lanang-eFishery/assets/16248869/08175c0a-2a99-46d4-8176-a72b9e5da08e)

## Referensi 
Dokumentasi YOLOv8: [Ultralytics YOLOv8](https://docs.ultralytics.com/modes/)
