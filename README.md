# bakery

### Tautan menuju aplikasi PWS: http://janssen-benedict-bakery.pbp.cs.ui.ac.id/


### -----------------------------------------------------------------------TUGAS 2-----------------------------------------------------------------------


### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

- Pertama-tama, saya menciptakan direktori untuk proyek Django bakery yang saya ingin buat (direktori terluar). Kemudian, saya membuat dan mengaktifkan virtual environment untuk proyek ini. Setelah itu, saya menginstalasi segala dependencies yang dibutuhkan oleh proyek ini (melalui requirements.txt) dan memulai proyek Django saya yang bernama "bakery". Setelah memastikan bahwa direktori proyek sudah dibuat, saya menambahkan host lokal ke dalam daftar host yang dapat mengakses aplikasi web (menambahkan localhost dan 127.0.0.1 pada ALLOWED_HOSTS di settings.py). Akhirnya, saya perlu memastikan bahwa server Django dapat dijalankan, saya menjalankan server dengan manage.py dan terlihat bahwa pembuatan proyek Django bakery saya berhasil.

- Saya menambahkan aplikasi bernama "main" pada proyek tersebut dengan memanfaatkan manage.py dan menggunakan command startapp. Setelah direktori aplikasi itu berhasil dibuat, saya mendaftarkan main ke dalam daftar aplikasi yang ada (pada INSTALLED_APPS di settings.py).

- Saya membuat routing URL untuk proyek ini melalui file urls.py di direktori proyek bakery. File urls.py pada proyek bakery akan mengatur rute URL proyek yang akan mengarah pada rute yang terdefinisi pada urls.py di aplikasi main dengan mengimpor rute URL dari aplikasi main (from django.urls import path, include) dan menambahkan rutenya ke daftar path URL-nya (urlpatterns = [path('', include('main.urls'))]).

- Saya membuat model pada aplikasi main melalui file models.py. Setelah mengimpor class yang digunakan untuk membuat model dalam Django (from Django.db import models), saya membuat class/model bernama Product. Atribut yang saya berikan pada model tersebut adalah name, price, description, category, dan quantity, serta atribut tambahan dalam bentuk fungsi is_in_stock() untuk memeriksa jika kuantitas produk bernilai lebih dari 0 atau tidak dan juga fungsi __str__() untuk memperoleh nama dari Product tersebut. Untuk menyimpan perubahan yang telah saya buat pada model, saya melakukan migrasi model menggunakan manage.py serta command makemigrations dan migrate.

- Pada views.py, saya perlu menciptakan fungsi untuk menerima permintaan HTTP dan mengembalikan render atau tampilan yang sesuai. Fungsi tersebut dinamakan show_main() yang menerima permintaan HTTP (request) serta terdapat nama aplikasi, NPM saya, nama saya sendiri, dan kelas PBP saya dalam data yang akan ditampilkan (context). Fungsi itu mengembalikan render yang akan menampilkan tampilan template main.html yang mengintegrasikan apa yang terdapat pada context. Agar main.html pasti menampilkan apa yang terdapat pada context, main.html perlu dimodifikasi untuk menampilkan data tersebut.

- Saya membuat routing URL untuk proyek ini melalui file urls.py di direktori main. File urls.py pada aplikasi main akan mengatur rute URL yang terkait pada aplikasi tersebut. Saya mengimpor apa yang diperlukan untuk mendefinisikan pola URL (from django.urls import path) dan fungsi show_main() yang sudah dibuat tadi (from main.views import show_main) sebagai apa yang akan ditampilkan saat pengguna mengklik URL tersebut. Saya memberikan nama 'main' pada pola URL aplikasi ini (melalui app_name) dan menambahkan path URL ke dalam urlpatterns (urlpatterns = [path('', show_main, name='show_main')]). Path URL akan diarahkan ke halaman web utama yang menampilkan nama aplikasi, NPM saya, nama saya sendiri, dan kelas PBP saya, sesuai dengan apa yang terdapat pada fungsi show_main().

- Saya juga melakukan inisiasi git pada proyek Django ini dan membuat repository publik pada GitHub dengan nama yang sama, yaitu "bakery". Saya menambahkan file .gitignore, menghubungkan direktori terluar proyek ini dengan repository yang saya buat di GitHub, serta melakukan command add, commit, dan push agar data pada direktori terluar tersimpan pada repository GitHub tersebut.

- Setelah aplikasi 'bakery' sudah diciptakan, saya melakukan deployment proyek ini ke server Pacil Web Service. Saya menghubungkan proyek baru yang dibuat pada PWS dengan direktori utama proyek ini dengan menambahkan URL deployment PWS saya ke daftar host (ALLOWED_HOSTS pada settings.py) dan menjalankan command-command yang diperlukan untuk melakukan push atau deployment ke server PWS.

- Saya menciptakan file README.md yang berisi penjelasan mengenai implementasi checklist tugas ini serta menjawab beberapa pertanyaan penting yang lain.


### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

Bagan: https://drive.google.com/file/d/1bxnk8fQtALKch54aiQWUrVZ01ZljJdtv/view?usp=sharing

Saat pengguna membuat request client ke web aplikasi berbasis Django, request tersebut diteruskan ke server Django. Django kemudian melakukan routing URL pada file urls.py atau mendeteksi path URL yang tepat agar dapat menampilkan data yang ingin diakses oleh request client tersebut. URL kemudian memetakan request kepada view. Penampilan data kepada pengguna diatur oleh view, yang dibentuk melalui fungsi pada file views.py. File views.py mengelola data dengan memanfaatkan model yang telah dibuat pada file models.py, model memiliki peran menghubungkan aplikasi dengan database-nya. Dari views.py, manipulasi terhadap data atau pemerolehan data dapat dilakukan melalui models.py. Data yang diperoleh akan diteruskan ke komponen yang merancang tampilan halaman webnya, yaitu file template HTML-nya. Pada proyek 'bakery', file template yang ada adalah main.html, yang memanfaatkan data yang diperoleh dari views.py untuk menunjukkan tampilan halaman web proyek tersebut. Tampilan halaman web tersebut diteruskan kembali kepada view dan dikembalikan kepada pengguna sebagai response dari requestnya, ini menunjukkan bahwa request telah diterima dan dieksekusikan. Bila terdapat input dari pengguna pada halaman HTML tersebut, data diteruskan kembali kepada view agar dapat dikelola. Jadi, terlihat bahwa komponen-komponen proyek Django tersebut saling berkaitan.


### 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
Fungsi utama git dalam pengembangan perangkat lunak adalah sebagai alat untuk memanajemen source code perangkat lunak tersebut. Git mampu melacak perubahan yang terjadi pada perangkat lunak dan berfungsi sebagai sistem kontrol versi (Version Control System) suatu perangkat lunak, sehingga seorang developer mampu menyimpan versi-versi berbeda dari perangkat lunak yang diciptakan dan juga dapat kembali ke versi yang lama jika diperlukan. Selain itu, Git memungkinkan beberapa developer untuk bekerja sama dalam mengembangkan suatu perangkat lunak serta memanfaatkan branch paralel untuk proses pengembangan nonlinear.


### 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak sebab Django merupakan framework pengembangan perangkat lunak yang bersifat cukup ramah bagi pemula. Framework Django mendukung pengembangan cepat (rapid development) dan memiliki banyak fitur keamanan yang dapat menjaminkan proses pengembangan perangkat lunak yang aman bagi para pemula. Selain itu, cara penggunaan Django bersifat sederhana dan mudah untuk dipahami, dengan berbagai sumber resmi yang ada untuk membantu para pemula dalam penggunaan framework tersebut.


### 5. Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut sebagai ORM karena model pada Django memungkinkan manipulasi data pada suatu database relasional melalui object dan class pada Python (suatu bahasa pemrograman yang berbasis object-oriented). Pada model Django, terjadi pemetaan object-object Python dengan database relasional tersebut, datanya direpresentasikan melalui object Python tersebut dan memungkinkan perubahan dan pengembangan data secara efisien.


### -----------------------------------------------------------------------TUGAS 3-----------------------------------------------------------------------


Screenshot pengaksesan URL proyek menggunakan Postman: https://drive.google.com/drive/folders/1gF8R9XbeALAtU6zx3gxdKBtbufiL6Kw2?usp=sharing


### 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery dibutuhkan dalam pengimplementasian sebuah platform agar seorang pengembang dapat mengirimkan data dari satu stack ke stack lainnya. Dengan adanya data delivery, data yang dibutuhkan dalam pengembangan aplikasi pada platform (seperti data dalam format HTML, JSON, dan XML) dapat diakses dan diproses secara efektif dan tepat.


### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, dari apa yang saya dapat peroleh dari berbagai sumber tepercaya, JSON merupakan format yang lebih baik dibandingkan dengan HTML. Asalan mengapa JSON bersifat lebih baik adalah karena JSON bersifat lebih sederhana dan mudah dipahami. Syntax yang digunakan oleh XML bersifat lebih kompleks, sehingga membuat proses membaca dan menulis data menggunakan XML dapat menjadi lebih sulit dibandingkan dengan melakukan hal yang sama menggunakan JSON,  yang menggunakan syntax yang lebih sederhana dan tidak membutuhkan banyak tag. Selain itu, data format JSON bersifat lebih mudah untuk di-parse dibandingkan dengan data format XML. Karena alasan-alasan tersebut, JSON menjadi lebih populer dibandingkan XML.


### 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Fungsi dari method is_valid() pada form Django adalah untuk memastikan bahwa data yang diinput oleh pengguna pada suatu form Django bersifat valid atau tidak. Method ini memeriksa data yang diinput dan menentukan validitas data tersebut sesuai dengan kondisi validasi yang ditentukan. Jika bersifat valid, akan dikembalikan nilai boolean true. Jika tidak valid, akan dikembalikan nilai boolean false.


### 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token merupakan token unik yang dibutuhkan saat membuat suatu form di Django sebagai elemen keamanan (security) karena dapat mencegah terjadinya serangan CSRF yang berbahaya. Jika csrf_token tidak ditambahkan pada form Django, maka aplikasi tersebut menjadi lebih rentan terhadap serangan-serangan tersebut. Hal ini tentu saja dapat dimanfaatkan oleh penyerang karena server Django tidak akan mengetahui sumber atau origin mana yang tepercaya dan yang mana yang tidak dapat dipercaya. Jadi, saat pengguna terautentikasi pada aplikasi web yang terlihat tepercaya, penyerang dapat saja membuat sebuah form palsu yang akan mengeksekusikan code berbahaya saat pengguna membukanya. Kemudian, code berbahaya itu mengirimkan request ke server dan verifikasi tidak akan terjadi sebab tidak ada csrf_token. 


### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).