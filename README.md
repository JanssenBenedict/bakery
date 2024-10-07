# bakery

Nama: Janssen Benedict
NPM: 2306152102
Kelas: PBP D

### Tautan menuju aplikasi PWS: http://janssen-benedict-bakery.pbp.cs.ui.ac.id/


### ---------------------------------------------------------TUGAS 2---------------------------------------------------------


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


### ---------------------------------------------------------TUGAS 3---------------------------------------------------------


Screenshot pengaksesan URL proyek menggunakan Postman: https://drive.google.com/drive/folders/1gF8R9XbeALAtU6zx3gxdKBtbufiL6Kw2?usp=sharing


### 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery dibutuhkan dalam pengimplementasian sebuah platform agar seorang pengembang dapat mengirimkan data dari satu stack ke stack lainnya. Dengan adanya data delivery, data yang dibutuhkan dalam pengembangan aplikasi pada platform (seperti data dalam format HTML, JSON, dan XML) dapat diakses dan diproses secara efektif dan tepat. Pengiriman data dapat berlangsung dengan cepat dan akurat serta menghindari terjadinya korupsi data atau permasalahan lain akibat data yang tidak disinkronisasikan.


### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, dari apa yang saya dapat peroleh dari berbagai sumber tepercaya, JSON merupakan format yang lebih baik dibandingkan dengan HTML. Asalan mengapa JSON bersifat lebih baik adalah karena JSON bersifat lebih sederhana dan mudah dipahami. Syntax yang digunakan oleh XML bersifat lebih kompleks, sehingga membuat proses membaca dan menulis data menggunakan XML dapat menjadi lebih sulit dibandingkan dengan melakukan hal yang sama menggunakan JSON,  yang menggunakan syntax yang lebih sederhana dan tidak membutuhkan banyak tag. Selain itu, data format JSON bersifat lebih mudah untuk di-parse dibandingkan dengan data format XML. Karena alasan-alasan tersebut, JSON menjadi lebih populer dibandingkan XML.


### 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Fungsi dari method is_valid() pada form Django adalah untuk memastikan bahwa data yang diinput oleh pengguna pada suatu form Django bersifat valid atau tidak. Method ini memeriksa data yang diinput dan menentukan validitas data tersebut sesuai dengan kondisi validasi yang ditentukan. Jika bersifat valid, akan dikembalikan nilai boolean true. Jika tidak valid, akan dikembalikan nilai boolean false. Method ini dibutuhkan agar data yang diinput pengguna dipastikan benar dan tidak berbahaya. Jika bersifat valid, data yang diinput dapat disimpan dan diakses. Jika bersifat tidak valid, pesan error dapat ditunjukkan.


### 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token merupakan token unik yang dibutuhkan saat membuat suatu form di Django sebagai elemen keamanan (security) karena dapat mencegah terjadinya serangan CSRF yang berbahaya. Serangan CSRF atau Cross-Site Request Forgery merupakan serangan siber yang dapat memaksa pengguna yang terautentikasi pada suatu aplikasi web untuk mengeksekusi command yang tidak baik atau berbahaya. Jika csrf_token tidak ditambahkan pada form Django, maka aplikasi tersebut menjadi lebih rentan terhadap serangan-serangan tersebut. Hal ini tentu saja dapat dimanfaatkan oleh penyerang karena server Django tidak akan mengetahui sumber atau origin mana yang tepercaya dan yang mana yang tidak dapat dipercaya. Jadi, saat pengguna terautentikasi pada aplikasi web yang terlihat tepercaya, penyerang dapat saja membuat sebuah form palsu yang akan mengeksekusikan code berbahaya saat pengguna membukanya. Code berbahaya itu dapat mengirimkan request ke server dan verifikasi tidak akan terjadi sebab tidak ada csrf_token. 


### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

#### - Membuat input form untuk menambahkan objek model pada app sebelumnya:
1. Pertama-tama, saya membuat file base.html yang berfungsi sebagai template dasar atau kerangka umum untuk halaman web lainnya (skeleton). Saya menggunakan template tags Django yang sesuai serta mengimplementasikan encoding UTF-8, mengatur layout atau viewport dari halaman webnya, serta mengimplementasikan style water.css. File base.html tersimpan dalam direktori templates di direktori utama proyek bakery, saya menambahkan kerangka tersebut ke dalam daftar template pada settings.py di direktori proyek bakery ('DIRS': [BASE_DIR / 'templates'] pada TEMPLATES).
2. Saya menambahkan atribut id pada model Product (yang sudah dibuat di models.py saat tugas 2) yang menerima input dari field UUID, kemudian saya juga melakukan proses migrasi agar perubahan pada model tersimpan. 
3. Saya membuat file forms.py yang akan mengandung struktur form untuk membuat Product bakery yang baru. Dalam file tersebut, saya mengimport model Product dan juga ModelForm untuk membuat form. Saya membuat class ProductForm yang merepresentasikan formnya (mengekstensi ModelForm), dengan Product sebagai model yang digunakan dan data field untuk form berupa nama produk (name), harganya (price), deskripsinya (description), kategorinya (category), dan jumlah stok yang tersedia (quantity).
4. Pada file views.py di direktori main, saya mengimport redirect (dari django.shortcuts), ProductForm, dan model Product. Kemudian, saya menciptakan fungsi create_product(request). Fungsi ini akan membuat ProductForm baru sesuai input pengguna pada request.POST (form = ProductForm(request.POST or None)), kemudian memeriksa jika input pada form valid dan jika method requestnya berupa POST (if form.is_valid() and request.method == "POST":). Jika kondisi tersebut dipenuhi, data form disimpan dan pengguna diredirect kembali ke halaman main (return redirect('main:show_main')). Jika kondisinya tidak terpenuhi, form tersebut disimpan dalam dictionary 'context' dan template create_product.html dirender kembali pada halaman web menggunakan data form pada 'context'. Response HTML tersebut terjadi bila kondisi awal tersebut tidak dipenuhi, sehingga form tidak disimpan datanya dan dirender ulang.
5. Kemudian, fungsi show_main(request) dimodifikasi dengan memperoleh semua object Product yang tersimpan di database (products = Product.objects.all()) dan memasukkannya sebagai data yang akan ditampilkan di halaman main ('products': product pada context).
6. Di urls.py pada direktori main, fungsi create_product yang baru saja dibuat diimport. Setelah itu, ditambahkan path URL di urlpatterns untuk mengakses fungsi tersebut (path('create-product', create_product, name='create_product')).
7. Di direktori main/templates, saya membuat file create_product.html (yang meng-extend base.html). Pada file tersebut, dibuat block untuk form dengan method POST dan csrf_token diimplementasikan. Kemudian, saya menggunakan syntax HTML untuk membuat tabel dan menambahkan template tag untuk menampilkan data field di forms.py sebagai suatu tabel ({{ form.as_table }}). Akhirnya, saya membuat tombol 'Add Product' untuk meng-submit request data tersebut ke fungsi create_product(request) di views.py.
8. Akhirnya, saya memodifikasi file main.html untuk meng-extend base.html dan menggunakan syntax yang tepat untuk menampilkan semua data Product dalam bentuk tabel, saya juga menambahkan tombol "Add New Product" yang akan me-redirect pengguna ke halaman form (create_product) untuk menambahkan data Product bakery yang baru. Saya menjalankan proyek Django tersebut dan melihat bahwa halaman webnya serta proses penambahan Product dapat berjalan dengan lancar.

#### - Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID:
Pada views.py di direktori main, saya mengimpor HTTPResponse dan serializers untuk membuat fungsi views yang dibutuhkan.
1. Saya membuat fungsi show_xml() yang menerima parameter request, menyimpan hasil query semua data Product dalam variabel, dan mengembalikan suatu HTTPResponse yang memanfaatkan data Product hasil query yang diserialisasi menjadi XML dan meng-set jenis konten response (content_type) sebagai application/xml.
2. Saya membuat fungsi show_json() yang menerima parameter request, menyimpan hasil query semua data Product dalam variabel, dan mengembalikan suatu HTTPResponse yang memanfaatkan data Product hasil query yang diserialisasi menjadi JSON dan meng-set jenis konten response (content_type) sebagai application/json.
3. Saya membuat fungsi show_xml_by_id() yang menerima parameter request, menyimpan hasil query semua data Product dalam variabel dengan id tertentu (filter(pk=id)), dan mengembalikan suatu HTTPResponse yang memanfaatkan data Product hasil query yang diserialisasi menjadi XML dan meng-set jenis konten response (content_type) sebagai application/xml.
4. Saya membuat fungsi show_json_by_id() yang menerima parameter request, menyimpan hasil query semua data Product dalam variabel dengan id tertentu (filter(pk=id)), dan mengembalikan suatu HTTPResponse yang memanfaatkan data Product hasil query yang diserialisasi menjadi JSON dan meng-set jenis konten response (content_type) sebagai application/json.

#### - Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2:
Pada urls.py, keempat fungsi yang saya baru saja buat harus diimpor dan ditambahkan 4 path URL baru ke dalam urlpatterns agar dapat mengakses fungsi-fungsi tersebut. Proyek Django dijalankan lagi dan dapat diperiksa jika fungsi tersebut berhasil diimplementasikan dengan menjalankan link http://localhost:8000/xml/, http://localhost:8000/xml/[id]/, http://localhost:8000/json/, http://localhost:8000/json/[id]/.

#### - Menjawab beberapa pertanyaan berikut pada README.md pada root folder:
Saya menjawab 5 pertanyaan tersebut di dalam file README.md pada direktori utama proyek ini.

#### - Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md:
Saya sudah mengakses keempat URL menggunakan Postman dan melampirkan screenshotnya dalam bentuk link Google Drive. Screenshot pengaksesan URL proyek menggunakan Postman: https://drive.google.com/drive/folders/1gF8R9XbeALAtU6zx3gxdKBtbufiL6Kw2?usp=sharing

#### - Melakukan add-commit-push ke GitHub:
Setelah memastikan bahwa Tugas 3 sudah dikerjakan dengan lengkap, saya menambahkan file deploy.yml di direktori .github/workflows yang akan membantu saya dalam melakukan push ke git dan sekaligus juga ke PWS. Saya menambahkan repository secret baru pada repository bakery di GitHub menggunakan format yang sesuai. Setelah itu, saya melakukan command git add, commit, dan push ke GitHub yang sekaligus juga melakukan push ke PWS.


### ---------------------------------------------------------TUGAS 4---------------------------------------------------------


### 1. Apa perbedaan antara HttpResponseRedirect() dan redirect()?
HttpResponseRedirect() merupakan suatu fungsi dari module django.http yang menghasilkan response HTTP dengan status code 302 agar dapat dilakukan redirect atau mengarahkan pengguna ke suatu URL spesifik, sedangkan redirect() merupakan suatu fungsi dari module django.shortcut yang akan mengembalikan suatu instance HttpResponseRedirect() untuk melakukan hal yang sama. HttpResponseRedirect() hanya menerima URL sebagai argumen dan response yang diterima akan membuat browser melakukan redirect ke URL tersebut. Sementara itu, redirect() tidak hanya menerima URL eksplisitnya sebagai argumen, tapi juga nama pattern URL, instance/object suatu model, ataupun nama suatu view. Fungsi shortcut redirect() bersifat lebih fleksibel dan lebih mudah untuk digunakan karena dapat menerima berbagai jenis parameter, sedangkan HttpResponseRedirect() hanya menerima URL eksplisitnya. Hanya saja, HttpResponseRedirect() mungkin dapat bersifat lebih efektif dalam kasus di mana masih perlu dilakukan beberapa pengaturan atau modifikasi terhadap response tersebut sebelum harus dikembalikan.


### 2. Jelaskan cara kerja penghubungan model Product dengan User!
Penghubungan model Product dengan model User dilakukan menggunakan ForeignKey. Dalam tugas ini, models.ForeignKey() dari modul django.db berfungsi menghubungkan satu Product dengan satu User melalui sebuah hubungan di mana suatu produk pasti terasosiasikan dengan seorang user. Di dalam model Product, ForeignKey diimplementasikan dengan kode user=models.ForeignKey(User, on_delete=models.CASCADE). Ini menciptakan suatu atribut baru yang dimiliki oleh semua object Product, yaitu user yang membuat Product tersebut. ForeignKey menunjuk pada model User yang menghasilkan instance Product tersebut dan Product akan dihapus dari database bila User tersebut juga dihapus dari sistem (on_delete=models.CASCADE).


### 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

- Perbedaan utama antara proses authentication dan authorization adalah bahwa authentication merupakan proses untuk memverifikasi identitas seorang pengguna agar dapat dipastikan bahwa pengguna yang ingin mengakses resources pada suatu sistem benar-benar merupakan pengguna yang terdaftar pada sistem tersebut, sedangkan authorization merupakan proses untuk memberikan hak atau perizinan tertentu (access rights) kepada pengguna yang sudah terautentikasi agar dapat diketahui apa yang dapat dilakukan dan tidak dapat dilakukan oleh pengguna di sistem tersebut.

- Saat pengguna melakukan proses login, authentication dan authorization dilakukan. Proses authentication dilakukan dengan meminta pengguna untuk memasukkan data penting, seperti username dan password pengguna. Jika data tersebut sesuai dengan yang terdapat pada database sistem, identitas pengguna telah diverifikasi dan pengguna dapat melakukan login. Setelah login berhasil dilakukan, perizinan atau hak akses yang sesuai akan diberikan kepada pengguna agar apa yang dapat diakses oleh pengguna pada sistem tersebut dibatasi sesuai dengan perizinan yang dimilikinya.

- Django mengimplementasikan authentication dan authorization dengan memanfaatkan fungsi-fungsi pada modul django.contrib.auth. Untuk proses authentication, fungsi yang dapat dimanfaatkan adalah authenticate() dan login() untuk melaksanakan proses autentikasi identitas pengguna dan login ke dalam aplikasi web setelah autentikasi berhasil. Fungsi authenticate() memverifikasikan kredensial yang diberikan pengguna dan mengembalikan object User (yang merepresentasikan pengguna tersebut) jika valid (model User menyimpan atribut data penting milik pengguna yang terdaftar pada sistem). Setelah identitas pengguna diverifikasi oleh fungsi itu, fungsi login() akan menetapkan session untuk pengguna tersebut pada aplikasi web yang diakses. Untuk proses authorization, yang dapat dimanfaatkan adalah decorators. Salah satu contoh decorator tersebut adalah @login_required. Decorator @login_required mengharuskan semua pengguna untuk melakukan proses login terlebih dahulu sebelum dapat mengakses halaman utama suatu aplikasi web. Decorator ini biasanya ditempatkan di atas fungsi view untuk menampilkan halaman utama serta dimasukkan URL halaman login sebagai argumen agar halaman login tersebut dapat ditampilkan saat aplikasi web tersebut dijalankan.


### 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

- Django mengingat pengguna yang telah login dengan memanfaatkan cookies (pada sisi klien) dan session (pada sisi server). Django memanfaatkan suatu cookie yang disebut sebagai session ID. Token session ID ini digunakan oleh aplikasi web Django untuk mengenali session yang unik pada aplikasi tersebut. Saat pengguna mengirimkan suatu request kepada server Django, session ID tersebut dikirimkan ke server dan akan dicocokkan dengan data session yang sudah tersimpan di database server. Jika session ditemukan (valid), maka Django menganggap pengguna sudah terautentikasi dan tidak perlu melakukan login ulang.

- Kegunaan lain dari cookies adalah mengetahui preferensi pengguna pada suatu halaman web (personalisasi), menyimpan isi keranjang belanja (situs e-commerce), serta menyimpan informasi/data lain mengenai pengguna yang berguna.

- Tidak semua cookies bersifat aman untuk digunakan. Cookies yang tidak dilindungi dengan baik dapat lebih rentan terhadap serangan di mana penyerang dapat mencuri informasi penting yang terdapat pada cookie tersebut. Bila hal tersebut terjadi, penyerang akan memperoleh kredensial penting yang dimiliki pengguna ataupun data aktivitas dan preferensi pengguna pada aplikasi web tersebut. Dengan data tersebut, penyerang dapat menggunakannya untuk melakukan session hijacking terhadap session pengguna ataupun menjual data penting tersebut untuk memperoleh keuntungan.


### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar:
1. Pada views.py di direktori main, saya mengimpor UserCreationForm (yang akan membantu dalam pembuatan form registrasi pengguna) dan messages (yang akan membantu menampilkan pesan bahwa registrasi berhasil). Setelah itu, saya membuat fungsi register(request) yang membuat form registrasi pengguna baru yang diisi oleh data input pengguna pada request.POST (form=UserCreationForm(request.POST)). Input form tersebut divalidasikan terlebih dahulu (if form.is_valid():), dan jika valid, data input form tersebut disimpan (form.save()) dan pengguna di-redirect kembali ke halaman login (return redirect('main:login')) untuk melakukan login dengan akun yang diregistrasi. Akhirnya, fungsi ini juga mengembalikan render dari halaman untuk melakukan registrasi pengguna baru (register.html) yang biasanya dikembalikan saat pengguna belum menginput apapun pada form registrasi atau jika data pada request.POST tidak valid. Agar fungsi tersebut berjalan dengan lancar, maka file template register.html perlu dibuat untuk menampilkan halaman di mana pengguna melakukan registrasi dan perlu ditambahkan path URL untuk mengakses fungsi register() pada urlpatterns di urls.py. 
2. Pada views.py, perlu diimpor AuthenticationForm (yang akan membantu dalam pembuatan form login) serta login dan authenticate (yang akan membantu dalam proses autentikasi pengguna). Saya membuat fungsi login_user(request) yang membuat form login/autentikasi pengguna yang diisi data input pengguna pada request.POST (form=AuthenticationForm(data=request.POST)). Jika input form login valid, maka fungsi login() digunakan untuk membuat session baru dan pengguna di-redirect ke halaman utama proyek (return redirect('main:show_main')). Selain itu, dikembalikan render dari halaman untuk melakukan login (login.html) jika pengguna belum memberi input atau data request.POST tidak valid. Agar berjalan dengan lancar, perlu dibuat file login.html untuk menampilkan halaman login tersebut dan ditambahkan path URL untuk mengakses fungsi login_user() pada urlpatterns di urls.py.
3. Pada views.py, perlu diimpor logout (yang akan membantu dalam penghapusan session pengguna). Saya membuat fungsi logout_user(request) yang menggunakan fungsi logout() untuk menghapus session pengguna yang terautentikasi, kemudian pengguna di-redirect kembali ke halaman untuk melakukan login (return redirect('main:login')).

- Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal:
Saya menjalankan aplikasi bakery pada local host, meregistrasikan dua akun dan membuat tiga Product bakery pada masing-masing akun tersebut. Bukti screenshotnya: https://drive.google.com/drive/folders/1zbAjR5HuAA8Y_H2BzlPxfqtDEhZIGQCn?usp=sharing

- Menghubungkan model Product dengan User:
Pada models.py di direktori main, saya mengimpor model User. Kemudian, pada model/class Product, saya menambahkan atribut berupa user yang menambahkan Product tersebut ke dalam sistem menggunakan ForeignKey (user=models.ForeignKey(User, on_delete=models.CASCADE)). ForeignKey menghubungkan satu Product dengan satu User, dan berbagai instance Product bisa saja dibuat oleh satu User yang sama (N-to-1 relationship). Kemudian, di views.py, dilakukan modifikasi pada fungsi create_product() di mana ditambahkan parameter commit=False pada form.save() untuk menghindari penyimpanan langsung Product yang telah dibuat. Ini dilakukan agar properti user pada Product tersebut dengan User yang terautentikasi pada sistem (request.user). Selain itu, pada fungsi show_main(), perlu dilakukan modifikasi di mana kumpulan object Product yang ditampilkan adalah Product yang terasosiasi dengan User spesifik tersebut saja (products = Product.objects.filter(user=request.user)). Setelah modifikasi tersebut dilakukan, perlu dilakukan migrasi untuk menyimpan perubahan pada model.

- Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi:
Pada views.py di direktori main, perlu diimpor komponen penting seperti HttpResponseRedirect, reverse, dan datetime. Pada fungsi login_user(), perlu dilakukan modifikasi untuk menambahkan suatu cookie yang dinamakan 'last_login' yang akan menyimpan data kapan terakhir kali seorang pengguna mengakses aplikasi tersebut. Setelah user melakukan login, response HTTP dibuat untuk me-redirect pengguna ke halaman utama (response=HttpResponseRedirect(reverse("main:show_main"))), tetapi sebelum dikembalikan, cookie 'last_login' dibuat dan ditambahkan ke dalam response-nya (response.set_cookie('last_login', str(datetime.datetime.now()))). Pada fungsi show_main(), data cookie ini ditambahkan ke dalam daftar informasi yang ingin ditampilkan (context) dan template halaman utama main.html dimodifikasi untuk menampilkan data cookie itu dengan template tag Django. Selain itu, pada fungsi logout_user(), penghapusan cookie 'last_login' perlu dilakukan ketika pengguna melakukan logout dari aplikasi. Untuk menampilkan username pengguna, pada daftar 'context', nama pengguna dapat di-set menjadi atribut username dari User yang terautentikasi ke dalam aplikasi tersebut ('name': request.user.username di context).

- Menjawab beberapa pertanyaan berikut pada README.md pada root folder (silakan modifikasi README.md yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas): Saya menjawab pertanyaan-pertanyaan tersebut pada file README.md di direktori utama proyek ini.

- Melakukan add-commit-push ke GitHub:
Setelah memastikan bahwa Tugas 4 telah dikerjakan dengan lengkap, kemudian saya melakukan command git add, commit, dan push ke GitHub yang sekaligus juga melakukan push ke PWS.


### ---------------------------------------------------------TUGAS 5---------------------------------------------------------


### 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Urutan prioritas pengambilan CSS selector:
1. Inline Styles: Inline Styles merupakan kategori CSS selector yang memiliki prioritas yang tertinggi.
Contohnya adalah: <h3 style="color: blue;">This.</h3>
2. Important Rule: Hal tersebut dapat tidak berlaku hanya jika digunakan !important (Important Rule), yang mampu melakukan override pada CSS selector manapun, bahkan Inline Styles.
Contohnya adalah: #this { color: blue !important; }
3. ID Selectors: ID Selectors memiliki prioritas yang lebih rendah daripada Inline Styles, tetapi lebih tinggi dibandingkan dengan Class Selectors, Pseudo-Class Selectors, dan Attribute Selectors.
Contohnya adalah: #this { color: blue; }
4. Class Selectors, Pseudo-Class Selectors, dan Attribute Selectors: Memiliki prioritas yang lebih rendah daripada ID Selectors, tetapi lebih tinggi dibandingkan Elements dan Pseudo-Elements.
Contohnya adalah: .this { color: blue; }, p[data-type="something"] { color: blue; }, dan p:hover { color: blue; }
5. Elements (Tag) dan Pseudo-Elements: Merupakan kategori CSS selector dengan prioritas yang terendah.
Contohnya adalah: p { color: blue; } dan p::after { content: "This = "; }


### 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive design merupakan konsep yang penting dalam pengembangan aplikasi web agar dapat meningkatkan kualitas penampilan halaman suatu aplikasi web pada berbagai perangkat berbeda, terutama pada perangkat dengan layar yang lebih kecil, seperti perangkat mobile. Dengan konsep responsive design, suatu halaman aplikasi web yang dapat ditampilkan secara rapi pada perangkat desktop dapat dibuat menjadi "mobile-friendly" atau terlihat lebih rapi dan baik untuk dipandang pada perangkat mobile juga. Contoh aplikasi yang sudah menerapkan responsive design adalah aplikasi-aplikasi seperti Shopee, Canva, Google Chrome, dan lain-lain sebab semua aplikasi tersebut mengimplementasikan suatu variasi penampilan halaman web pada perangkat mobile yang rapi dan sesuai dengan ukuran layar pada suatu perangkat mobile. Aplikasi yang terlihat belum menerapkan responsive design adalah sistem SIAK NG, sebab penampilan yang ditunjukkan bila sistem tersebut diakses melalui perangkat mobile terlihat kurang rapi, penampilan halaman web sistem ini yang terlihat lebih rapi hanya ditampilkan pada perangkat desktop.

### 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
1. Margin: Margin merupakan suatu ruang transparan yang terdapat di luar border suatu elemen dan berfungsi dalam mengatur jarak antar-elemen.
2. Border: Border merupakan suatu garis yang berada di antara padding isi/konten suatu elemen dengan ruang margin elemen tersebut.
3. Padding: Padding merupakan suatu ruang yang berada di antara garis border dengan isi/konten suatu elemen.
Cara pengimplementasiannya adalah:
.this {
    margin: 22px;
    border: 1px dashed red;
    padding: 15px;
}
Penjelasan:
- Margin telah di-set menjadi 22 pixel. Artinya, jarak elemen ini dengan elemen lainnya (baik itu elemen lain yang terdapat di atas, di bawah, di samping kiri, ataupun di samping kanan elemen ini) adalah 22 pixel.
- Border yang telah di-set berukuran 1 pixel, berupa garis putus-putus, dan berwarna merah.
- Padding telah di-set menjadi 15 pixel. Artinya, jarak antara isi/konten elemen dengan border (baik itu sisi border yang terdapat di atas, di bawah, di samping kiri, ataupun di samping kanan isi/konten elemen ini) adalah 15 pixel.


### 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexbox (atau Flexible Box) layout merupakan suatu sistem layout yang berfungsi dalam pengaturan elemen secara responsif dalam satu dimensi (satu baris atau satu kolom). Kegunaan dari Flexbox layout adalah untuk menyimpan dan menyusun elemen-elemen pada satu baris atau kolom serta mengatur posisi dan ukuran elemen-elemen tersebut secara fleksibel berdasarkan ruang yang ada. Grid layout merupakan suatu sistem layout yang berfungsi dalam pengaturan elemen secara responsif dalam suatu grid dua dimensi (seperti suatu tabel). Kegunaan dari Grid layout adalah untuk menyimpan dan menyusun elemen-elemen pada suatu layout dua dimensi (dengan banyak baris dan kolom) serta lebih cocok dalam pengaturan suatu desain yang bersifat lebih kompleks.


### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

* Implementasikan fungsi untuk menghapus dan mengedit product.
Jawaban:
Pertama-tama, saya harus mengimplementasikan fungsi view untuk melakukan penghapusan dan pengeditan product pada views.py. Untuk proses pengeditan product, saya menciptakan fungsi edit_product(request, id). Fungsi tersebut memperoleh object product dengan suatu ID tertentu saja dan memasukkan data object product tersebut ke dalam ProductForm agar data atribut product tersebut langsung berada pada isi field di formnya untuk dimodifikasi (form = ProductForm(request.POST or None, instance = Product.objects.get(pk=id))). Kemudian, perlu diperiksa validitas dari input data hasil modifikasi, jika valid, data tersebut disimpan dan pengguna di-redirect kembali ke halaman utama (Home). Bila apa yang diinput pengguna pada form ternyata tidak valid, sistem akan me-render ulang halaman web untuk edit product. Hal yang serupa dilakukan untuk proses penghapusan product. Pada views.py, diciptakan fungsi delete_product(request, id) yang memperoleh object product dengan suatu ID tertentu saja dan menghapusnya dari sistem (Product.objects.get(pk=id).delete()). Kemudian, pengguna di-redirect kembali ke halaman utama, tanpa object product tersebut. Di urls.py pada direktori main, kedua fungsi itu diimport dan ditambahkan path URL di urlpatterns untuk mengakses fungsi tersebut (nama route URL disertai ID-nya, seperti '.../<uuid:id>'). Untuk proses pengeditan product, saya kemudian menciptakan template HTML edit_product.html yang menampilkan halaman form yang serupa dengan form untuk menciptakan product baru, pengguna dapat memodifikasi input data yang sudah terdapat pada masing-masing atribut product dan menyimpannya. Akhirnya, pada template main.html di direktori main/templates, saya menambahkan dua data cell tabel baru pada setiap baris di tabel yang menampilkan semua product yang dibuat, data cell tersebut mengandung tombol untuk mengedit dan menghapus product tersebut (dipastikan bahwa object product pada baris itu juga yang dapat diedit atau dihapus dengan memasukkan product.pk sebagai parameter pada pembangunan URL untuk tombolnya).

* Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut:

- Kustomisasi halaman login, register, dan tambah product semenarik mungkin.
Jawaban:
1. Pertama-tama, saya ingin mengklarifikasikan bahwa saya menggunakan framework CSS Tailwind dan mengimplementasikannya ke dalam file base.html, yang menjadi dasar dari penampilan semua halaman web yang terdapat pada aplikasi ini. Semua halaman web HTML pada aplikasi Bakery ini akan meng-extend base.html dan mengimplementasikan Tailwind. Setelah melakukan konfigurasi static files pada aplikasi ini melalui settings.py, saya menambahkan file global.css untuk menambahkan beberapa style custom pada beberapa elemen tertentu. Saya melakukan styling custom pada elemen form seperti .form-style form input, form textarea, dan form select dengan menambahkan padding, border hitam jika kursor tidak difokuskan pada elemen tersebut, dan border hijau jika kursor difokuskan pada elemen tersebut. Kemudian, suatu animasi baru yang dinamakan shine diciptakan, di mana gradien warna elemen tersebut diubah secara terus-menerus agar terlihat seperti elemen yang berkilau. Saya kemudian memastikan bahwa file global.css diimplementasikan pada semua halaman web aplikasi ini dengan memasukkannya ke base.html.
2. Saya melakukan modifikasi terhadap template HTML login.html untuk melakukan kustomisasi halaman login. File tersebut tetap meng-extend base.html dan mengandung navigation bar-nya. Saya memastikan bahwa terdapat teks di atas form login yang besar serta posisinya di tengah (teksnya menyatakan bahwa itu adalah halaman login). Kemudian, menciptakan label untuk menyatakan area input data dan area input data tersebut, yaitu username dan password pengguna tersebut. Kemudian, terdapat tombol untuk melakukan login (meng-submit data username dan password). Bila pengguna belum terdaftar pada aplikasi ini, terdapat pesan yang mengandung hyperlink ke halaman registrasi. Saya juga melakukan kustomisasi di mana warna latar belakang, tombol, dan hyperlink adalah hijau.
3. Saya melakukan modifikasi terhadap template HTML register.html untuk melakukan kustomisasi halaman registrasi. File tersebut tetap meng-extend base.html dan mengandung navigation bar-nya. Saya memastikan bahwa terdapat teks di atas form registrasi yang besar serta posisinya di tengah (teksnya menyatakan bahwa itu adalah halaman registrasi). Kemudian, setiap field dari UserCreationForm diperoleh serta ditampilkan sebagai area input data (dan label di atasnya) menggunakan form-style yang sudah dikustomisasi sebelumnya. Kemudian, terdapat tombol untuk melakukan register (meng-submit data tersebut). Bila pengguna sudah terdaftar pada aplikasi ini, terdapat pesan yang mengandung hyperlink ke halaman login. Saya juga melakukan kustomisasi di mana warna latar belakang, tombol, dan hyperlink adalah hijau.
4. Saya melakukan modifikasi terhadap template HTML create_product.html untuk melakukan kustomisasi halaman tambah product. File tersebut tetap meng-extend base.html dan mengandung navigation bar-nya. Saya memastikan bahwa terdapat teks di atas form yang besar serta posisinya di tengah (teksnya menyatakan bahwa itu adalah halaman tambah product). Setiap field dari ProductForm diperoleh serta ditampilkan sebagai area input data (dan label di atasnya) menggunakan form-style yang sudah dikustomisasi sebelumnya. Kemudian, terdapat tombol untuk menambahkan product (meng-submit data tersebut). Bila data yang diinput pengguna sudah tepat, pengguna dikembalikan ke halaman utama dengan product baru tersebut ditampilkan sebagai card. Saya juga melakukan kustomisasi di mana warna latar belakang dan tombolnya hijau.

- Kustomisasi halaman daftar product menjadi lebih menarik dan responsive. Kemudian, perhatikan kondisi berikut:
1. Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.
Jawaban:
Halaman daftar product merupakan halaman utama aplikasi ini, file template HTML yang digunakan adalah main serta tetap meng-extend base.html dan mengandung navigation bar-nya.html. Pada main.html, terdapat card yang menyatakan informasi identitas dari pengguna yang login (tampilan diatur pada file card_info.html serta memanfaatkan animasi berkilau yang sebelumnya telah dibuat), teks yang memperoleh informasi kapan terakhir kali pengguna tersebut melakukan login (memanfaatkan cookie 'last_login'), tombol untuk menambahkan product baru (me-redirect pengguna ke halaman form untuk menambah product), serta daftar card product yang telah dibuat. Selain itu, saya melakukan kustomisasi di mana warna latar belakang, tombol, dan card-nya adalah hijau. Bila pengguna belum membuat product pada aplikasi ini, yang akan muncul bukanlah daftar card product, melainkan suatu gambar simbol "X" besar yang merah dengan teks yang menyatakan bahwa saat ini tidak ada product yang terdaftar pada sistem.
2. Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card (tidak boleh sama persis dengan desain pada Tutorial!).
Jawaban:
Bila sudah ada product yang tersimpan pada sistem ini, akan ditampilkan card dari setiap product, yang mengandung informasi product tersebut (nama, harga, deskripsi, kategori, dan kuantitas) dengan warna hijau pada headernya serta memanfaatkan animasi berkilau yang sebelumnya sudah dibuat (tampilan diatur pada file card_product.html). Bila product tersebut sudah memiliki kuantitas 0, yang ditampilkan pada kuantitas adalah teks "OUT OF STOCK". Untuk daftar informasi pengguna, digunakan Flexbox untuk menampilkan satu kolom yang menunjukkan card informasi mengenai pengguna tersebut. Untuk daftar product, digunakan grid untuk menampilkan setiap card product dalam sebuah tabel dengan 3 kolom.

- Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!
Jawaban:
Pada ujung kanan bawah tampilan card product, terdapat dua tombol kecil, yaitu tombol untuk mengedit product yang telah dibuat dan tombol untuk menghapus product tersebut. Pada card_product.html, saya melakukan pembuatan kedua tombol tersebut dan mengatur penampilannya. Untuk tombol pengeditan product, diberi warna ungu muda dengan gambar/ikon SVG suatu pena pada tombol tersebut. Bila pengguna mengklik tombol tersebut, pengguna akan diarahkan ke halaman untuk mengedit product (dilakukan dengan mengakses fungsi untuk mengedit product, <a href="{% url 'main:edit_product' product.pk %}" ... </a>). Tampilan halaman untuk mengedit product (edit_product.html) mirip dengan halaman untuk menambah product baru, dengan perbedaannya berupa teks yang terdapat di atas form serta form tersebut sudah terisi dengan data yang sudah dimiliki oleh setiap atribut pada product tersebut. Pengguna dapat melakukan modifikasi dan menekan tombol di bagian bawah form tersebut untuk menyimpan hasil pengeditan. Untuk tombol penghapusan product, diberi warna pink dengan gambar/ikon SVG suatu tempat sampah pada tombol tersebut. Bila pengguna mengklik tombol tersebut, product tersebut langsung dihapus dari sistem, sehingga daftar card product tidak akan menampilkan card product tersebut (dilakukan dengan mengakses fungsi untuk menghapus product, <a href="{% url 'main:delete_product' product.pk %}" ... </a>).


- Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.
Jawaban:
Saya mengimplementasikan navigation bar dengan file template navbar.html menggunakan syntax framework CSS Tailwind. Warna dari navigation bar yang saya buat untuk aplikasi ini adalah warna hijau tua. Selain itu, Flexbox diimplementasikan pada kode CSS agar dapat menunjukkan setiap elemen dari navigation bar dalam satu baris secara rapi. Fitur-fitur pada aplikasi tersebut yang ditampilkan pada navigation bar hanya ditampilkan secara penuh bila pengguna menggunakan perangkat deskstop. Jika pengguna belum terautentikasi pada aplikasi ini, navigation bar akan hanya menampilkan nama dari aplikasi ini di ujung kiri serta tombol untuk melakukan register dan tombol untuk melakukan login di ujung kanan. Jika pengguna sudah berhasil login ke aplikasi ini, navigation bar akan menunjukkan fitur-fitur lainnya, yaitu pilihan Home, Products, Categories, dan Cart di ujung kiri (bila diklik, Home dan Products akan mengarahkan pengguna ke halaman utama). Pada ujung kanan, terlihat suatu pesan yang menyatakan username dari pengguna yang terautentikasi ke dalam sistem ini serta tombol untuk melakukan logout. Bila pengguna menggunakan perangkat mobile untuk melihat aplikasi ini, fitur-fitur ini tetap ada, hanya saja fitur-fitur tersebut disembunyikan dan yang ditampilkan secara langsung pada navigation bar adalah tombol untuk melakukan ekspansi dan memperlihatkan fitur-fitur tersebut (hamburger button). Pengguna perangkat mobile perlu mengklik hamburger button tersebut untuk melihat fitur-fitur yang ditampilkan secara langsung pada perangkat desktop.


- Menjawab beberapa pertanyaan berikut pada README.md pada root folder (silakan modifikasi README.md yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).
Jawaban:
Saya menjawab pertanyaan-pertanyaan tersebut pada file README.md di direktori utama proyek ini.


- Melakukan add-commit-push ke GitHub.
Jawaban:
Setelah memastikan bahwa Tugas 5 telah dikerjakan dengan lengkap, kemudian saya melakukan command git add, commit, dan push ke GitHub yang sekaligus juga melakukan push ke PWS.


### ---------------------------------------------------------TUGAS 6---------------------------------------------------------


### 1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
Manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web adalah:
- Peningkatkan interaktivitas antara suatu halaman web (yang memanfaatkan JavaScript) dengan seorang pengguna melalui kemampuan JavaScript untuk mengandali event pada halaman web tersebut.
- Perubahan atau manipulasi terhadap konten pada suatu halaman web secara dinamis dan efisien. JavaScript memungkinkan data atau konten yang ditampilkan pada suatu halaman web untuk berubah sesuai perilaku pengguna tanpa harus melakukan refresh terhadap halaman web tersebut.
- Eksekusi kode JavaScript dilakukan pada peramban pengguna, bukan pada server situs web, sehingga pengimplementasian JavaScript dapat menghemat waktu dan penggunaan bandwith karena kompleksitas kode JavaScript tidak akan memengaruhi performa server situs web tersebut.
- JavaScript bersifat kompatibel dengan semua browser web modern sehingga script JavaScript yang diimplementasikan pada template halaman HTML web dapat berfungsi secara konsisten pada berbagai browser berbeda (Google Chrome, Mozilla Firefox, dan lainnya).


### 2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
Fungsi dari penggunaan await adalah untuk menunggu hasil dari fungsi JavaScript yang dapat mengembalikan nilai secara asinkronus, seperti fungsi fetch(). Bila await dimanfaatkan, JavaScript akan menunggu hingga operasi pada fungsi fetch() selesai dilaksanakan dulu sebelum berlanjut ke baris kode berikutnya yang ada. Bila await tidak digunakan, JavaScript akan terus menjalankan baris-baris kode yang berada di bawah baris kode dengan fungsi fetch() tanpa menunggu operasi pada fungsi fetch() untuk selesai. Bila terdapat kode yang memerlukan hasil yang diperoleh dari operasi pada fungsi fetch(), terdapat kemungkinan terjadinya kesalahan pada data yang diperoleh sebab fungsi fetch() belum selesai melaksanakan operasinya.


### 3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
Decorator csrf_exempt perlu digunakan pada fungsi view yang digunakan untuk AJAX POST karena request AJAX POST yang terkirim tidak mengandung token CSRF. Pada Django, adanya proteksi atau perlindungan CSRF merupakan default pada semua fungsi view yang mengandali request POST dan membutuhkan token CSRF agar request tersebut diterima. Agar fungsi view tersebut dapat menerima request AJAX POST tersebut tanpa token CSRF, dibutuhkan decorator csrf_exempt, yang memungkinkan Django untuk mengabaikan proteksi atau perlindungan CSRF pada view tersebut.


### 4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Melakukan pembersihan data (sanitization) pada frontend saja tidak cukup sebab seorang penyerang yang memasukkan input data yang berbahaya pada suatu aplikasi web dapat saja melewati proses pembersihan data dan mengirimkan input data yang berbahaya kepada server secara langsung. Bila input data yang berbahaya dari penyerang berhasil melewati (mem-bypass) pembersihan data pada frontend dan tidak ada pembersihan data pada backend, data yang berbahaya tersebut akan tersimpan di dalam database aplikasi web dan membahayakan keamanan aplikasi web tersebut. Oleh karena itu, pembersihan data tidak dilakukan di frontend saja, tetapi juga dilakukan di backend agar input data yang dimasukkan oleh pengguna dapat menjadi data yang bersifat "bersih" sebelum disimpan dan digunakan oleh aplikasi web tersebut.


### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

--- Mengubah tugas 5 yang telah dibuat sebelumnya menjadi menggunakan AJAX:

- AJAX GET:

1. Ubahlah kode cards data Product agar dapat mendukung AJAX GET.
Penjelasan:
Untuk membuat kode card Product dapat mendukung AJAX GET, saya menghapus potongan kode pada template main.html yang menggunakan block conditional dan for loop untuk memperoleh data Product serta menampilkan card Product yang ada atau menampilkan gambar bila tidak ada Product yang terdaftar pada sistem. Setelah itu, saya menggantikan potongan kode tersebut dengan satu elemen container div dengan ID "product_cards". Pada bagian block script, saya mengimplementasikan fungsi JavaScript asinkronus getProducts() yang memanfaatkan fetch() API untuk memperoleh data JSON masing-masing Product yang dibuat oleh pengguna secara asinkronus. Data JSON tersebut kemudian di-parse menjadi objek JavaScript dan dikembalikan oleh fungsi tersebut. Kemudian, saya membuat fungsi JavaScript asinkronus refreshProducts(), fungsi ini akan melakukan refresh terhadap data Product yang dibuat oleh pengguna dan menampilkannya pada container dengan ID "product_cards". Pertama-tama, fungsi ini menghapus isi HTML tersebut (isi className dan innerHTML) dan memanggil fungsi getProducts() untuk memperoleh data setiap Product. Jika data tersebut kosong (belum ada Product), isi className dan innerHTML akan di-set untuk menampilkan gambar dan pesan bahwa tidak ada Product yang tersedia pada sistem. Jika data tersebut tidak kosong, isi className akan di-set menjadi container dengan berbagai kolom untuk menampilkan setiap card Product dan innerHTML (child element) akan diisi dengan kode untuk membentuk dan menampilkan card yang berisi data mengenai Product tersebut (for each loop digunakan untuk memperoleh masing-masing Product yang dibuat), mirip dengan kode yang terdapat pada template card_product.html pada Tugas 5. Fungsi tersebut dipanggil setiap kali halaman web tersebut dibuka. Kode cards data Product ini mendukung AJAX GET karena data Product diperoleh secara asinkronus menggunakan fetch() API.

2. Lakukan pengambilan data Product menggunakan AJAX GET. Pastikan bahwa data yang diambil hanyalah data milik pengguna yang logged-in.
Penjelasan:
Untuk melakukan pengambilan data Product dengan AJAX GET, pada file views.py, saya menghapus baris kode yang memperoleh semua object Product berdasarkan pengguna dan menyimpannya pada daftar context di fungsi view show_main(). Karena fungsi JavaScript asinkronus getProducts() memperoleh data Product dalam bentuk JSON melalui fungsi view show_json(), baris kode untuk memperoleh semua object Product berdasarkan pengguna yang membuatnya ditambahkan ke fungsi show_json() (data=Product.objects.filter(user=request.user)). Dengan ini, setiap data Product yang diambil merupakan Product yang dibuat oleh pengguna yang terautentikasi ke dalam sistem tersebut saja.

- AJAX POST:

1. Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan Product.
Penjelasan:
Tombol yang saya buat untuk membuka modal dengan form untuk menambahkan Product akan ditampilkan di sebelah tombol "Add New Product". Cara pengimplementasiannya adalah:
<button data-modal-target="crudModal" data-modal-toggle="crudModal" class="btn bg-green-600 hover:bg-green-700 border-2 border-black text-white font-bold py-2 px-4 duration-300" onclick="showModal();">Add New Product by AJAX</button>
Saat tombol tersebut diklik, modal dengan ID "crudModal" ditampilkan dan fungsi JavaScript showModal().
Agar tombol tersebut dapat mengeksekusikan apa yang perlu dijalankan bila diklik, hal yang perlu dilakukan adalah mengimplementasikan modal form tersebut ke dalam aplikasi Bakery ini. Pada modal ini, container div utama yang terluar (dengan ID "crudModal") memberikan styling inisial pada modal dan awalnya masih tidak ditunjukkan (hidden). Kemudian, container div dengan ID "crudModalContent" mengandung konten dari modal form yang ingin dibentuk dengan ukuran tampilan yang berbeda tergantung pada ukuran layar yang menampilkannya. Di dalam container tersebut, terdapat header, body, dan footer modal. Header modal merupakan bagian yang membuat dan menampilkan judul form dan tombol untuk menutup modal (tombol "X"). Body modal merupakan bagian yang membuat dan menampilkan form baru agar pengguna dapat menginput data untuk Product baru yang ingin dibuat, field input data yang disediakan kepada pengguna untuk diisi adalah nama, harga, deskripsi, kategori, dan kuantitas Product tersebut. Akhirnya, footer untuk modal membuat dan menampilkan tombol untuk membatalkan penambahan Product baru pada form (Cancel) dan tombol untuk meng-submit data yang diinput untuk membuat Product baru (Create Product). Akhirnya, pada block script, perlu diimplementasikan fungsi-fungsi JavaScript agar modal dapat berfungsi, yaitu showModal() yang akan menampilkan modal dengan form yang telah dibuat serta hideModal() yang akan menutup tampilan modal bila tombol Cancel atau tombol "X".

2. Buatlah fungsi view baru untuk menambahkan Product baru ke dalam basis data.
Penjelasan:
Fungsi view baru yang perlu dibuat untuk menambahkan Product baru ke dalam basis data dengan AJAX POST adalah fungsi add_product_ajax(request). Fungsi tersebut memperoleh informasi mengenai nama, harga, deskripsi, kategori, dan kuantitas Product tersebut dari data POST request tersebut. Selain itu, data mengenai user atau pengguna yang mengirimkan request juga diperoleh. Kemudian, diciptakan object Product baru menggunakan data yang sudah diperoleh dan disimpan ke dalam database. Akhirnya, fungsi tersebut mengembalikan response dengan status code 201 untuk mengindikasikan bahwa proses penambahan Product baru berhasil. Selain itu, ditambahkan decorator csrf_exempt (Django tidak memeriksa keberadaan csrf_token pada POST request) dan require_POST (fungsi ini hanya dapat diakses saat pengguna mengirimkan POST request ke fungsi tersebut).

3. Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat.
Penjelasan:
Pada file urls.py, saya mengimpor fungsi view add_product_ajax yang baru saja diciptakan dan menambahkan path URL untuk mengakses fungsi add_product_ajax() pada urlpatterns di urls.py, nama rute path URL tersebut yang saya pilih adalah "create-ajax/" (path('create-ajax/', add_product_ajax, name='add_product_ajax')).

4. Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/.
Penjelasan:
Penghubungan form pada modal yang saya buat ke path /create-ajax/ dilakukan melalui pengimplementasian fungsi JavaScript addProduct() di block script pada main.html. Fungsi ini menggunakan fetch() API untuk mengirimkan request POST yang memperoleh data dari field input di form menambahkan Product baru dan memasukkannya ke body requestnya. Setelah proses tersebut selesai, fungsi asinkronus refreshProducts() dipanggil untuk melakukan refresh terhadap bagian halaman web yang menampung tampilan card semua Product yang dibuat. Kemudian, field input data pada form di modal dikosongkan dan modal tersebut ditutup. Akhirnya, pada block script itu juga, ditambahkan event listener pada form tersebut di mana mengklik tombol untuk meng-submit input data Product baru akan memanggil fungsi addProduct() dan mematikan default behavior dari event submisi pada form tersebut (e.preventDefault()).

5. Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar Product terbaru tanpa reload halaman utama secara keseluruhan.
Penjelasan:
Tanpa melakukan reload halaman web utama secara keseluruhan, setelah saya mengklik tombol "Create Product" pada form modal setelah menginput data yang dibutuhkan pada form tersebut, card untuk object Product baru yang saya baru saja tambahkan ke dalam sistem langsung muncul pada bagian daftar semua card di halaman web utama aplikasi Bakery ini. Refresh terjadi secara asinkronus dan saya tidak perlu melakukan reload secara keseluruhan untuk melihat tampilan card Product baru itu.

--- Menjawab beberapa pertanyaan berikut pada README.md pada root folder (silakan modifikasi README.md yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).
Saya menjawab pertanyaan-pertanyaan tersebut pada file README.md di direktori utama proyek ini.

--- Melakukan add-commit-push ke GitHub.
Setelah memastikan bahwa Tugas 6 telah dikerjakan dengan lengkap, kemudian saya melakukan command git add, commit, dan push ke GitHub yang sekaligus juga melakukan push ke PWS.