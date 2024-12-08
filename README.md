# Kelompok 7, Kelas B
1. I0324047 | Ghani Ziyad Sagiansyah (Ghani-Sagianstag)
2. I0324049 | Inashofa Rosyidin (Inashofa)
3. I0324066 | Safira Naafi Widyarani (Safira-bit)

# Aplikasi Peminjaman Uang
Aplikasi Peminjaman Uang Bank Santai adalah aplikasi sederhana yang dibuat untuk melakukan peminjaman uang secara mudah dan praktis. Aplikasi ini membuat simulasi cicilan yang harus dibayarkan per bulan sesuai dengan mode cicilan dan durasi cicilan yang dipilih oleh pengguna.

# Fitur Aplikasi
 **1. Admin**  
- **Sistem Login**  
  Fitur ini membuat keamanan data Bank Santai terjamin karena hanya admin yang memiliki akses khusus.  
- **Pengelolaan Durasi Cicilan**  
  Admin dapat menghapus durasi yang sudah ada maupun menambahkan durasi cicilan baru sesuai kebijakan yang ditetapkan Bank Santai.  
- **Pengelolaan Suku Bunga**  
  Admin dapat dengan mudah mengganti suku bunga berdasarkan BI Rate yang dapat berubah sewaktu-waktu.

 **2. Pengguna**  
- **Sistem Login dan Sign Up**  
  Pengguna diminta untuk memasukkan username dan password bagi yang sudah memiliki akun. Jika pengguna belum memiliki akun, aplikasi akan mengarahkan untuk membuat akun terlebih dahulu.  
- **Pengisian Nominal Pinjaman**  
  Pengguna mengisikan nominal yang akan dipinjam dengan mengetikkan pada kolom yang tersedia.  
- **Pemilihan Durasi Cicilan**  
  Pengguna hanya dapat memilih durasi cicilan yang diisikan oleh admin.  
- **Pemilihan Mode Cicilan**  
  1. **Cicilan Tetap**  
     Suku bunga yang digunakan adalah suku bunga tetap sebesar 5%. Cicilan ini memiliki jumlah pembayaran yang sama setiap bulan.  
  2. **Cicilan Menurun**  
     Mode ini menggunakan suku bunga tetap sebesar 5%. Jumlah pembayaran menurun setiap bulan karena bunga dihitung berdasarkan sisa pokok pinjaman.  
  3. **Cicilan Fluktuasi BI-Rate**  
     Suku bunga dalam mode cicilan ini berubah-ubah sesuai dengan nilai BI Rate yang diatur oleh admin. Namun, jumlah cicilannya sama setiap bulan.

# Flowchart
![flowchart revisi](https://github.com/user-attachments/assets/ea231f45-94e6-430a-bb7f-3e0ec9b9a33e)

# Flowchart (Revisi)
![flowchart revisi (1)](https://github.com/user-attachments/assets/d3651077-5d75-414b-90e6-a37caf5aac2c) 
Deskripsi Flowchart
1.	Diketahui suku bunga yang perlu dibayarkan setiap cicilan adalah 3% dari nominal pinjaman masing-masing pengguna.
2.	Pengguna menginput nominal pinjaman dan jumlah cicilan per bulannya.
3.	Pengguna memilih metode pembayaran:

a.	Jika pengguna memilih metode pembayaran cicilan tetap, maka jumlah total tagihan = nominal pinjaman x (100% + suku bunga) dan tagihan per bulan = jumlah cicilan x (100% + suku bunga). Jika setelah pembayaran cicilan menggunakan metode cicilan tetap total tagihan tidak kurang dari tagihan, maka total tagihan = total tagihan – tagihan. Jika sisa total tagihan masih tidak kurang dari tagihan, ulangi proses ini hingga total tagihan kurang dari tagihan. Jika total tagihan sudah kurang dari tagihan, maka pengguna hanya perlu membayarkan nominal sesuai dengan sisa tagihan sehingga total tagihan menjadi 0 yang berarti lunas.

b.	Jika pengguna memilih metode pembayaran cicilan menurun, maka ditetapkan angsuran = 0. Kemudian menghitung banyak bulan yang diperlukan untuk membayar tagihan yang dirumuskan banyak bulan = nominal pinjaman / jumlah cicilan. Jika angsuran kurang dari banyak bulan, maka tagihan = [nominal pinjaman x (100% + suku bunga)] / banyak bulan. Angsuran = angsuran + 1. Selanjutnya, nominal pinjaman = nominal pinjaman – tagihan. Ulangi proses ini hingga angsuran tidak kurang dari banyak bulan dan menjadi lunas.

c.	Jika pengguna tidak memilih metode pembayaran cicilan tetap dan menurun, otomatis pengguna akan diarahkan untuk menggunakan metode pembayaran cicilan fluktuatif sesuai BI-Rate. 

 
