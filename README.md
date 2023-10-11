# InkWanderers

### Anggota Kelompok:
- Kevin Gilbert Sinaga (2206826053)
- Muhamad Rifqi (2206081433)
- Nabiel Ahmad Ardhityo (2206083331)
- Narendra Dzulqarnain (2206081881)
- Rafael Bismo Dewandaru (2206824666)

<details>
<summary>Cerita aplikasi yang diajukan serta manfaatnya</summary>
Melalui website ini, user dapat dengan mudah menyusun daftar buku yang ingin mereka baca, yang memungkinkan mereka mengatur dan merencanakan bacaan mereka dengan lebih baik. User dapat menggunakan bookmark untuk mencatat buku-buku yang menarik minat mereka. Kemampuan untuk menambahkan buku ke dalam collection dengan cepat juga memberikan kemudahan bagi user. User dapat menjelajahi berbagai buku dalam katalog dengan mudah, menemukan buku yang menarik, dan langsung menambahkannya ke dalam collection mereka. Modul review juga memberikan user kesempatan untuk berbagi pendapat mereka tentang buku yang telah mereka baca, membantu user lain dalam memilih buku yang sesuai dengan minat mereka. Ini juga memperkaya pengalaman membaca dengan memungkinkan user berinteraksi dengan komunitas pembaca yang lebih besar. <br />
<br />
Batasan collection maksimal 10 buku adalah pengingat penting untuk tetap fokus pada buku-buku yang benar-benar menjadi prioritas. Ini membantu user untuk mengelola waktunya dengan lebih baik dan menjaga collection mereka agar tetap relevan dengan preferensi mereka. Modul bookmark memberikan kemudahan bagi user untuk menandai buku-buku yang ingin mereka pinjam atau baca di masa depan, tanpa harus menyimpan semuanya di collection. Ini mempermudah perencanaan bacaan mereka dan membantu mereka mengingat judul-judul yang menarik hati. Secara keseluruhan, website ini memberikan alat yang bermanfaat bagi user untuk mengatur dan memaksimalkan pengalaman membaca mereka, berbagi ulasan dan rekomendasi dengan sesama user, serta menjadikan proses pemilihan dan membaca buku lebih efisien dan memuaskan.<br />
</details>

<details>
<summary>Daftar modul yang akan diimplementasikan</summary>
1. Modul untuk membuat role (baik role user dan admin)
2. Modul collection list buku yang dibaca oleh role user
    - User dapat menambahkan buku dari katalog kedalam collection
    - Buku yang ada di dalam collection user akan hilang dari katalog
    - User dapat melihat buku yang sudah mereka tambahkan ke collection dan memberikan reviews
    - Maksimal buku yang ada di dalam collection user adalah 10
3. Modul katalog buku yang bisa ditambahkan oleh admin dan diakses oleh user 
    - Admin dapat menambahkan sebanyak-banyaknya buku ke dalam katalog
    - Admin dapat menghapus buku dari katalog
    - Admin dapat melihat katalog buku
    - User dapat melihat buku yang berada di katalog dan menambahkannya ke collection
4. Modul review buku yang telah dibaca
    - Setelah user memasukkan buku ke dalam collection buku, user dapat mengembalikan buku dari collection user kembali ke katalog dan menambahkan review untuk buku tersebut
5. Modul bookmark buku oleh user
    - Bookmark digunakan untuk menandakan buku yang ingin dipinjam oleh user apabila isi buku di dalam collection sudah mencapai 10
    - Buku yang sudah di bookmark oleh user lain tetap dapat terlihat di katalog
</details>

<details>
<summary>Sumber dataset katalog buku</summary>
Berikut sumber data set yang kami gunakan
DatasetF05 https://www.kaggle.com/datasets/dylanjcastillo/7k-books-with-metadata/
</details>

<details>
<summary>Role atau peran pengguna beserta deskripsinya</summary>
Terdapat dua jenis role dalam website ini, yaitu:<br />
User<br />
Masing-masing user dapat memiliki satu collection dan bookmark. User dapat menambahkan buku ke dalam collection atau bookmark. Bookmark dapat berisi buku sebanyak-banyaknya, sedangkan collection hanya dapat berisi maksimal sepuluh buku.<br />
<br />
Admin<br />
Seorang admin dapat menambahkan buku baru ke dalam katalog yang sudah tersedia.<br />
</details>