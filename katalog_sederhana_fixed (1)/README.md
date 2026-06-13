# Website Katalog Sederhana dengan Django

Nama: Muhammad Alvin
NIM: 2208107010089

## Penjelasan Singkat Program
Program ini adalah website katalog produk sederhana yang dibuat menggunakan
framework Django. Website memiliki 4 halaman utama:

1. **Homepage (/)** - Menampilkan sambutan dan deskripsi singkat website
2. **Daftar Produk (/produk/)** - Menampilkan 3 produk (data hardcoded di views.py)
3. **Detail Produk (/produk/<id>/)** - Menampilkan detail spesifik produk berdasarkan ID
4. **Kontak (/kontak/)** - Menampilkan informasi kontak toko

## Fitur
- Routing URL berbeda untuk setiap halaman (produk/urls.py)
- Menggunakan template Django dengan base.html sebagai template induk (template inheritance)
- Data produk disimpan dalam list of dictionary Python di views.py (tanpa database)
- Tampilan responsive dengan CSS sederhana

## Cara Menjalankan
1. Pastikan Python dan Django sudah terinstall:
   ```
   pip install django
   ```
2. Masuk ke folder project (folder yang berisi manage.py):
   ```
   cd katalog_sederhana
   ```
3. Jalankan server:
   ```
   python manage.py runserver
   ```
4. Buka browser ke `http://127.0.0.1:8000/`

## Struktur Halaman
| Halaman        | URL            |
|----------------|----------------|
| Homepage       | /              |
| Daftar Produk  | /produk/       |
| Detail Produk  | /produk/<id>/  |
| Kontak         | /kontak/       |

## Teknologi
- Django 5.x
- HTML5
- CSS3
