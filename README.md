1. perbedaan json,xml,html
  json = JavaScript yang digunakan dalam transfer dan penyimpanan data, format penulisannya berbentuk text
  xml = Extensible Markup Language yang digunakan untuk menyederhanakan pertukaran dan penyimpanan data (opening tag dan closing tag)
  html = Bahasa yang menggunakan tag untuk menyatakan kode yang harus dimengerti oleh browser agar halaman tersebut dapat ditampilkan

2. data delivery dalam pengimplementasian sebuah platform
  pengirimian data dibutuhkan dari satu stack ke stack lain yang mana bermacam macam bentuknya

3. cara mengimplementasikan checklist
  1. Permintaan masuk pada server Django akan diproses melalui urls.py dan diteruskan ke views.py
  2. Jika diperlukan database views.py akan memanggil models.py melalui fungsi show_mywatchlist kemudian show_mywatchlist meminta semua object MyWaatchlist dari              models.py
  3. Pada MyWaatchlist terdiri dari watched, tittle, rating, release_date, review barang kemudian data akan dikembalikan ke views.py
  4. Hasil proses tersebut akan di mapping di html yang sudah didefinisikan kemudian html akan menjadi respon user

4. hasil postman
xml : ![image](https://user-images.githubusercontent.com/90234027/194107598-ffba83e5-446f-4159-aeee-723025799076.png)

json :  ![image](https://user-images.githubusercontent.com/90234027/194107574-f78f40fa-e97e-4169-a67f-08c46d778646.png)

html : ![image](https://user-images.githubusercontent.com/90234027/194107552-b8269a4d-ae27-4474-9758-43b5583106a8.png)
