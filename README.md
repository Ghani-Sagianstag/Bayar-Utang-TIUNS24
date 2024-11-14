# Kelompok 7, Kelas B
1. I0324047 | Ghani Ziyad Sagiansyah 
2. I0324049 | Inashofa Rosyidin 
3. I0324066 | Safira Naafi Widyarani 

# Bayar-Utang-TIUNS24
Membuat simulasi perhitungan cicilan pinjaman/hutang selama beberapa bulan dengan menghitung cicilan per bulan, bunga, serta saldo akhir pinjaman, hingga cicilan lunas.

# Fitur Program
- Mode Cicilan Tetap
- Mode Cicilan Menurun
- Mode Cicilan Fluktuatif sesuai BI-Rate

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

 
