Laporan Praktikum Pemrograman Berorientasi Objek

Nama  : Febryan Valentino Putra
Nim   : 2509106094

Implementasi OOP Lanjutan (Inheritance, Overriding, Encapsulation, dan Relasi Objek)

Abstraksi Program
Program ini dikembangkan menggunakan bahasa pemrograman Python untuk merepresentasikan sistem manajemen klinik sederhana. Implementasi dirancang guna menerapkan prinsip-prinsip Pemrograman Berorientasi Objek secara komprehensif, mencakup pewarisan atribut, penyembunyian data, polimorfisme melalui method overriding, serta pemodelan hubungan antar entitas (asosiasi, agregasi, dan komposisi).

Penerapan Prinsip Pemrograman Berorientasi Objek yaitu
1. Inheritance (Pewarisan)
   Class Pasien dan Dokter bertindak sebagai subclass yang mewarisi atribut serta metode umum dari superclass Orang.
   
2. Encapsulation (Enkapsulasi)
   Atribut nomor induk kependudukan (__nik) pada class Orang didefinisikan sebagai data privat. Akses dan modifikasi nilai dilakukan secara aman melalui mekanisme property getter dan setter yang dilengkapi validasi panjang karakter (16 digit).
   
3. Method Overriding
   Penerapan polimorfisme dinamis dilakukan melalui penimpaan metode tampilkan_info() pada masing-masing class anak guna menyajikan informasi entitas secara spesifik.
4. Relasi UML
   - Agregasi: Class Klinik menampung kumpulan objek Dokter dalam bentuk struktur data daftar.
   - Komposisi: Class RekamMedis diinisialisasi untuk merekam riwayat medis entitas pasien secara terstruktur.

Spesifikasi Entitas dan Data Uji
- Entitas Pasien: 
  1. Andi (NIK: 6471012345678901, Alamat: Jl. Mulawarman)
  2. Siti (NIK: 6471098765432109, Alamat: Jl. A. Yani)
- Entitas Dokter: 
  1. Dr. Budi (NIK: 6471111111111111, Alamat: Jl. P. Antasari)
  2. Dr. Dewi (NIK: 6471222222222222, Alamat: Jl. Lambung Mangkurat)

Petunjuk Eksekusi Program
Pastikan lingkungan eksekusi Python telah terpasang pada perangkat Anda. Jalankan perintah berikut melalui terminal atau baris perintah:

python main.py
