Tautan menuju aplikasi PWS:


1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

- Pertama-tama, saya menciptakan direktori untuk proyek Django bakery yang saya ingin buat. Kemudian, saya membuat dan mengaktifkan virtual environment untuk proyek ini. Setelah itu, saya menginstalasi segala dependencies yang dibutuhkan oleh proyek ini (melalui requirements.txt) dan memulai proyek Django saya yang bernama "bakery". Setelah memastikan bahwa direktori proyek sudah dibuat, saya menambahkan host lokal ke dalam daftar host yang dapat mengakses aplikasi web (menambahkan localhost dan 127.0.0.1 pada ALLOWED_HOSTS di settings.py). Akhirnya, saya perlu memastikan bahwa server Django dapat dijalankan, saya menjalankan server dengan manage.py dan terlihat bahwa pembuatan proyek Django bakery saya berhasil.

- Saya menambahkan aplikasi bernama "main" pada proyek tersebut dengan memanfaatkan manage.py dan menggunakan command startapp. Setelah direktori aplikasi itu berhasil dibuat, saya mendaftarkan main ke dalam daftar aplikasi yang ada (pada INSTALLED_APPS di settings.py).

- Saya membuat routing URL untuk proyek ini melalui file urls.py di direktori proyek bakery. File urls.py pada proyek bakery akan mengatur rute URL proyek yang akan mengarah pada rute yang terdefinisi pada urls.py di aplikasi main dengan mengimpor rute URL dari aplikasi main (from django.urls import path, include) dan menambahkan rutenya ke daftar path URL-nya (urlpatterns = [path('', include('main.urls'))]).

- Saya membuat model pada aplikasi main melalui file models.py. Setelah mengimpor class yang digunakan untuk membuat model dalam Django (from Django.db import models), saya membuat class/model bernama Product. Atribut yang saya berikan pada model tersebut adalah name, price, description, category, dan quantity, serta atribut tambahan dalam bentuk fungsi is_in_stock() untuk memeriksa jika kuantitas produk bernilai lebih dari 0 atau tidak dan juga fungsi __str__() untuk memperoleh nama dari Product tersebut. Untuk menyimpan perubahan yang telah saya buat pada model, saya melakukan migrasi model menggunakan manage.py serta command makemigrations dan migrate.

-
-
-
-


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.


3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
Fungsi utama git dalam pengembangan perangkat lunak adalah sebagai alat untuk memanajemen source code perangkat lunak tersebut. Git mampu melacak perubahan yang terjadi pada perangkat lunak dan berfungsi sebagai sistem kontrol versi suatu perangkat lunak, sehingga seorang developer mampu menyimpan versi-versi berbeda dari perangkat lunak yang diciptakan dan juga dapat kembali ke versi yang lama jika diperlukan. Selain itu, Git memungkinkan beberapa developer untuk bekerja sama dalam mengembangkan suatu perangkat lunak serta memanfaatkan branch paralel untuk proses pengembangan nonlinear.


4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak sebab Django merupakan framework pengembangan perangkat lunak yang bersifat cukup ramah bagi pemula yang belum mampu melakukan pengembangan perangkat lunak melalui suatu framework pengembangan. Selain itu, cara penggunaan Django bersifat sederhana dan mudah untuk dipahami.


5. Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut sebagai ORM karena model pada Django memungkinkan manipulasi data pada suatu database relasional melalui object dan class pada Python (suatu bahasa pemrograman yang berbasis object-oriented). Data pada database tersebut direpresentasikan melalui object (model Django) pada Python dan memungkinkan perubahan dan pengembangan data secara efisien.
