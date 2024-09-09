# bakery

### Tautan menuju aplikasi PWS:


### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

- Pertama-tama, saya menciptakan direktori untuk proyek Django bakery yang saya ingin buat (direktori terluar). Kemudian, saya membuat dan mengaktifkan virtual environment untuk proyek ini. Setelah itu, saya menginstalasi segala dependencies yang dibutuhkan oleh proyek ini (melalui requirements.txt) dan memulai proyek Django saya yang bernama "bakery". Setelah memastikan bahwa direktori proyek sudah dibuat, saya menambahkan host lokal ke dalam daftar host yang dapat mengakses aplikasi web (menambahkan localhost dan 127.0.0.1 pada ALLOWED_HOSTS di settings.py). Akhirnya, saya perlu memastikan bahwa server Django dapat dijalankan, saya menjalankan server dengan manage.py dan terlihat bahwa pembuatan proyek Django bakery saya berhasil.

- Saya menambahkan aplikasi bernama "main" pada proyek tersebut dengan memanfaatkan manage.py dan menggunakan command startapp. Setelah direktori aplikasi itu berhasil dibuat, saya mendaftarkan main ke dalam daftar aplikasi yang ada (pada INSTALLED_APPS di settings.py).

- Saya membuat routing URL untuk proyek ini melalui file urls.py di direktori proyek bakery. File urls.py pada proyek bakery akan mengatur rute URL proyek yang akan mengarah pada rute yang terdefinisi pada urls.py di aplikasi main dengan mengimpor rute URL dari aplikasi main (from django.urls import path, include) dan menambahkan rutenya ke daftar path URL-nya (urlpatterns = [path('', include('main.urls'))]).

- Saya membuat model pada aplikasi main melalui file models.py. Setelah mengimpor class yang digunakan untuk membuat model dalam Django (from Django.db import models), saya membuat class/model bernama Product. Atribut yang saya berikan pada model tersebut adalah name, price, description, category, dan quantity, serta atribut tambahan dalam bentuk fungsi is_in_stock() untuk memeriksa jika kuantitas produk bernilai lebih dari 0 atau tidak dan juga fungsi __str__() untuk memperoleh nama dari Product tersebut. Untuk menyimpan perubahan yang telah saya buat pada model, saya melakukan migrasi model menggunakan manage.py serta command makemigrations dan migrate.

- Pada views.py, saya perlu menciptakan fungsi untuk menerima permintaan HTTP dan mengembalikan render atau tampilan yang sesuai. Fungsi tersebut dinamakan show_main() yang menerima permintaan HTTP (request) serta terdapat nama aplikasi, NPM saya, nama saya sendiri, dan kelas PBP saya dalam data yang akan ditampilkan (context). Fungsi itu mengembalikan render yang akan menampilkan tampilan template main.html yang mengintegrasikan apa yang terdapat pada context. Agar main.html pasti menampilkan apa yang terdapat pada context, main.html perlu dimodifikasi untuk menampilkan data tersebut.

- Saya membuat routing URL untuk proyek ini melalui file urls.py di direktori main. File urls.py pada aplikasi main akan mengatur rute URL yang terkait pada aplikasi tersebut. Saya mengimpor apa yang diperlukan untuk mendefinisikan pola URL (from django.urls import path) dan fungsi show_main() yang sudah dibuat tadi (from main.views import show_main) sebagai apa yang akan ditampilkan saat pengguna mengklik URL tersebut. Saya memberikan nama 'main' pada pola URL aplikasi ini (melalui app_name) dan menambahkan path URL ke dalam urlpatterns (urlpatterns = [path('', show_main, name='show_main')]). Path URL akan diarahkan ke halaman web utama yang menampilkan nama aplikasi, NPM saya, nama saya sendiri, dan kelas PBP saya, sesuai dengan apa yang terdapat pada fungsi show_main().

- Saya juga melakukan inisiasi git pada proyek Django ini dan membuat repository publik pada GitHub dengan nama yang sama, yaitu "bakery". Saya menambahkan file .gitignore, menghubungkan direktori terluar proyek ini dengan repository yang saya buat di GitHub, serta melakukan command add, commit, dan push agar data pada direktori terluar tersimpan pada repository GitHub tersebut.

- Setelah aplikasi 'bakery' sudah diciptakan, saya melakukan deployment proyek ini ke server Pacil Web Service.

- Saya menciptakan file README.md yang berisi penjelasan mengenai implementasi checklist tugas ini serta menjawab beberapa pertanyaan penting yang lain.


### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.


### 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
Fungsi utama git dalam pengembangan perangkat lunak adalah sebagai alat untuk memanajemen source code perangkat lunak tersebut. Git mampu melacak perubahan yang terjadi pada perangkat lunak dan berfungsi sebagai sistem kontrol versi (Version Control System) suatu perangkat lunak, sehingga seorang developer mampu menyimpan versi-versi berbeda dari perangkat lunak yang diciptakan dan juga dapat kembali ke versi yang lama jika diperlukan. Selain itu, Git memungkinkan beberapa developer untuk bekerja sama dalam mengembangkan suatu perangkat lunak serta memanfaatkan branch paralel untuk proses pengembangan nonlinear.


### 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak sebab Django merupakan framework pengembangan perangkat lunak yang bersifat cukup ramah bagi pemula. Framework Django mendukung pengembangan cepat (rapid development) dan memiliki banyak fitur keamanan yang dapat menjaminkan proses pengembangan perangkat lunak yang aman bagi para pemula. Selain itu, cara penggunaan Django bersifat sederhana dan mudah untuk dipahami, dengan berbagai sumber resmi yang ada untuk membantu para pemula dalam penggunaan framework tersebut.


### 5. Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut sebagai ORM karena model pada Django memungkinkan manipulasi data pada suatu database relasional melalui object dan class pada Python (suatu bahasa pemrograman yang berbasis object-oriented). Pada model Django, terjadi pemetaan object-object Python dengan database relasional tersebut, datanya direpresentasikan melalui object Python tersebut dan memungkinkan perubahan dan pengembangan data secara efisien.
