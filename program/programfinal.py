import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import json
from PIL import Image, ImageDraw, ImageFont
import os

durations = [3, 6, 9, 12, 24, 36]  # Default pilihan durasi pembayaran

interest_rate = 6  # Suku bunga default adalah 6% sesuai dengan BI-Rate November 2024

# Tampilan Home
def show_cover(): 
    try:
        import os
        from PIL import Image, ImageTk

        file_path = os.path.join(os.path.dirname(__file__), "1.png") # Path relatif ke gambar
        
        background_image = Image.open(file_path) # Buka gambar dengan PIL
       
        max_width, max_height = 1568, 868  # Tentukan ukuran maksimum
        
        original_width, original_height = background_image.size # Dapatkan ukuran asli gambar
        
        scale = min(max_width / original_width, max_height / original_height) # Hitung rasio skala

        new_width = int(original_width * scale) # Hitung ukuran baru berdasarkan rasio
        new_height = int(original_height * scale)
        
        resized_image = background_image.resize((new_width, new_height), Image.Resampling.LANCZOS) # Ubah ukuran gambar
        bg_photo = ImageTk.PhotoImage(resized_image)

        
        canvas = tk.Canvas(window, width=new_width, height=new_height) # Buat canvas sesuai ukuran gambar yang diubah
        canvas.pack(fill="both", expand=True)

        
        canvas.create_image(0, 0, image=bg_photo, anchor="nw") # Tampilkan gambar sebagai latar belakang

        
        canvas.image = bg_photo # Simpan referensi gambar agar tidak dihapus oleh garbage collector
        
        button_next = tk.Button(window, text="Masuk", command=login_screen, font=("Century Gothic", 14), bg="white", fg="purple", 
                                cursor="hand2", pady=10, padx=20)
        canvas.create_window(760, 750, anchor="center", window=button_next)

    except FileNotFoundError as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", f"Gambar tidak ditemukan: {e}")
    except Exception as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

# Tampilan sign-up
def signup_screen():
    for widget in window.winfo_children():
        widget.destroy()

    try:
        # Load gambar latar belakang
        import os
        from PIL import Image, ImageTk
        # Path relatif ke gambar
        file_path = os.path.join(os.path.dirname(__file__), "3.png")
        background_image = Image.open(file_path)

        # Tentukan ukuran maksimum
        max_width, max_height = 1568, 868

        # Dapatkan ukuran asli gambar
        original_width, original_height = background_image.size

        # Hitung rasio skala
        scale = min(max_width / original_width, max_height / original_height)

        # Hitung ukuran baru berdasarkan rasio
        new_width = int(original_width * scale)
        new_height = int(original_height * scale)

        # Ubah ukuran gambar
        resized_image = background_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        bg_photo = ImageTk.PhotoImage(resized_image)

        # Buat canvas sesuai ukuran gambar yang diubah
        canvas = tk.Canvas(window, width=new_width, height=new_height)
        canvas.pack(fill="both", expand=True)

        # Tampilkan gambar sebagai latar belakang
        canvas.create_image(0, 0, image=bg_photo, anchor="nw")

        # Simpan referensi gambar agar tidak dihapus oleh garbage collector
        canvas.image = bg_photo

        # Tambahkan elemen-elemen GUI di atas gambar latar belakang
        global entry_username
        global entry_password
        
        entry_username = tk.Entry(window)
        canvas.create_window(770, 240, window=entry_username)  

        entry_password = tk.Entry(window, show="*")
        canvas.create_window(770, 325, window=entry_password)  

        button_signup = tk.Button(window, text="Sign Up", font=("Century Gothic", 15), cursor="hand2", bg="white", fg="purple", 
                                  command=signup)
        button_signup.pack(pady=20)
        canvas.create_window(770, 380, window=button_signup)

        button_to_login = tk.Button(window, text="Kembali ke Login", font=("Century Gothic", 15), cursor="hand2", bg="white", 
                                    fg="purple", command=login_screen)
        button_to_login.pack(pady=10)
        canvas.create_window(770, 600, window=button_to_login)

    except FileNotFoundError as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", f"Gambar tidak ditemukan: {e}")
    except Exception as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

def signup():
    username = entry_username.get()
    password = entry_password.get()

    if username and password:
        save_user_data(username, password)
        messagebox.showinfo("Pendaftaran Berhasil", "Akun berhasil dibuat!")
        login_screen()
    else:
        messagebox.showerror("Kesalahan", "Username dan password tidak boleh kosong!")

# Fungsi untuk sign up user
def signup():
    username = entry_username.get()
    password = entry_password.get()

    if username and password:
        save_user_data(username, password)
        messagebox.showinfo("Pendaftaran Berhasil", "Akun berhasil dibuat!")
        login_screen()
    else:
        messagebox.showerror("Kesalahan", "Username dan password tidak boleh kosong!")

# Fungsi untuk menyimpan data pengguna ke dalam file JSON
def save_user_data(username, password):
    users = load_users()
    users[username] = {"password": password}
    with open('users.json', 'w') as f:
        json.dump(users, f)

# Tampilan login
def login_screen():
    # Bersihkan semua elemen di jendela
    for widget in window.winfo_children():
        widget.destroy()

    try:
        # Load gambar latar belakang
        import os
        from PIL import Image, ImageTk
        # Path relatif ke gambar
        file_path = os.path.join(os.path.dirname(__file__), "2.png")
        background_image = Image.open(file_path)

        # Tentukan ukuran maksimum
        max_width, max_height = 1568, 868

        # Dapatkan ukuran asli gambar
        original_width, original_height = background_image.size

        # Hitung rasio skala
        scale = min(max_width / original_width, max_height / original_height)

        # Hitung ukuran baru berdasarkan rasio
        new_width = int(original_width * scale)
        new_height = int(original_height * scale)

        # Ubah ukuran gambar
        resized_image = background_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        bg_photo = ImageTk.PhotoImage(resized_image)

        # Buat canvas sesuai ukuran gambar yang diubah
        canvas = tk.Canvas(window, width=new_width, height=new_height)
        canvas.pack(fill="both", expand=True)

        # Tampilkan gambar sebagai latar belakang
        canvas.create_image(0, 0, image=bg_photo, anchor="nw")

        # Simpan referensi gambar agar tidak dihapus oleh garbage collector
        canvas.image = bg_photo

        # Tambahkan elemen-elemen GUI di atas gambar latar belakang
        global entry_username
        global entry_password

        entry_username = tk.Entry(window)
        canvas.create_window(770, 240, window=entry_username)  

        entry_password = tk.Entry(window, show="*")
        canvas.create_window(770, 325, window=entry_password)

        button_login = tk.Button(window, text="Login", font=("Century Gothic", 15), cursor="hand2", bg="white", fg="purple", 
                                 command=login)
        canvas.create_window(770, 370, window=button_login)
        
        button_to_signup = tk.Button(
        window, text="Sign Up", font=("Century Gothic", 15), cursor="hand2", bg="white", fg="purple",  command=signup_screen)
        canvas.create_window(770, 480, window=button_to_signup)

    except FileNotFoundError as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", f"Gambar tidak ditemukan: {e}")
    except Exception as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

# Fungsi untuk login user atau admin
def login():
    username = entry_username.get()
    password = entry_password.get()

    users = load_users()
    admin_data = load_admin()

    if username == admin_data["username"] and password == admin_data["password"]:
        admin_dashboard()
    elif username in users and users[username]["password"] == password:
        user_dashboard(username)
    else:
        messagebox.showerror("Login Gagal", "Username atau password salah!")

# Fungsi untuk memuat data pengguna dari file JSON
def load_users():
    try:
        with open('users.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Fungsi untuk menyimpan data admin bank
def save_admin_data():
    admin_data = {"username": "admin", "password": "admin123"}
    with open('admin.json', 'w') as f:
        json.dump(admin_data, f)

# Fungsi untuk memuat data admin dari file JSON
def load_admin():
    try:
        with open('admin.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        save_admin_data()
        return load_admin()

# Fungsi untuk menghitung cicilan dengan mode tetap
def calculate_fixed_payment(principal, months, interest_rate):
    interest = principal * (interest_rate / 100)
    total_payment = principal + interest
    monthly_payment = total_payment / months
    return monthly_payment

# Fungsi untuk menghitung cicilan dengan mode menurun
def calculate_decreasing_payment(principal, months, interest_rate):
    monthly_payments = []
    for month in range(1, months + 1):
        interest = (principal - (principal / months) * (month - 1)) * (interest_rate / 100)
        monthly_payment = (principal / months) + interest
        monthly_payments.append(monthly_payment)
    return monthly_payments

# Fungsi untuk menghitung cicilan dengan mode fluktuasi sesuai BI-Rate
def calculate_flexible_payment(principal, months, bi_rate):
    monthly_payments = []
    for month in range(1, months + 1):
        interest = principal * (bi_rate / 100)
        monthly_payment = (principal / months) + interest
        monthly_payments.append(monthly_payment)
    return monthly_payments

# Tampilan dashboard user
def user_dashboard(username):
    global entry_loan_amount
    for widget in window.winfo_children():
        widget.destroy()

    try:
        # Load gambar latar belakang
        import os
        from PIL import Image, ImageTk
        # Path relatif ke gambar
        file_path = os.path.join(os.path.dirname(__file__), "4.png")
        background_image = Image.open(file_path)

        # Tentukan ukuran maksimum
        max_width, max_height = 1568, 868

        # Dapatkan ukuran asli gambar
        original_width, original_height = background_image.size

        # Hitung rasio skala
        scale = min(max_width / original_width, max_height / original_height)

        # Hitung ukuran baru berdasarkan rasio
        new_width = int(original_width * scale)
        new_height = int(original_height * scale)

        # Ubah ukuran gambar
        resized_image = background_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        bg_photo = ImageTk.PhotoImage(resized_image)

        # Buat canvas sesuai ukuran gambar yang diubah
        canvas = tk.Canvas(window, width=new_width, height=new_height)
        canvas.pack(fill="both", expand=True)

        # Tampilkan gambar sebagai latar belakang
        canvas.create_image(0, 0, image=bg_photo, anchor="nw")

        # Simpan referensi gambar agar tidak dihapus oleh garbage collector
        canvas.image = bg_photo

        # Tambahkan elemen-elemen GUI di atas gambar latar belakang
        entry_loan_amount = tk.Entry(window)
        canvas.create_window(770, 200, window=entry_loan_amount)

        duration_var = tk.IntVar(value=durations[0])  # Pilihan awal
        dropdown_duration = tk.OptionMenu(window, duration_var, *durations)
        canvas.create_window(770, 276, window=dropdown_duration) 

        mode_var = tk.StringVar(value="fixed")
        radio_fixed = tk.Radiobutton(window, text="Cicilan Tetap", font=("Century Gothic", 15), bg="white", fg="purple",
                                     variable=mode_var, value="fixed")
        canvas.create_window(770, 365, window=radio_fixed) 

        radio_decreasing = tk.Radiobutton(window, text="Cicilan Menurun", font=("Century Gothic", 15), bg="white", fg="purple",
                                          variable=mode_var, value="decreasing")
        canvas.create_window(770, 405, window=radio_decreasing) 

        radio_flexible = tk.Radiobutton(window, text="Cicilan Fluktuasi BI-Rate", font=("Century Gothic", 15), bg="white", fg="purple",
                                        variable=mode_var, value="flexible")
        canvas.create_window(770, 445, window=radio_flexible) 

        button_calculate = tk.Button(
        window,text="Hitung Cicilan", font=("Century Gothic", 15), bg="white", fg="purple", cursor="hand2",
        command=lambda: calculate_loan(entry_loan_amount, duration_var, mode_var.get(), username))
        canvas.create_window(770, 550, window=button_calculate)  
        
        button_logout = tk.Button(window, text="Logout", font=("Century Gothic", 15), bg="white", fg="purple",
                                  cursor="hand2", command=login_screen)
        canvas.create_window(770, 700, window=button_logout)  

    except FileNotFoundError as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", f"Gambar tidak ditemukan: {e}")
    except Exception as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")
   
# Struk
def print_receipt(username, loan_amount, loan_duration, monthly_payments, mode):
    try:
        # Format detail cicilan per bulan dengan padding untuk rata kanan
        formatted_payments = "\n".join(
            [f"Bulan {str(i+1).zfill(2)} : Rp {safe_float(payment):>15,.2f}" for i, payment in enumerate(monthly_payments)]
        )

        # Membuat isi struk
        receipt_text = f"""
        ======================================
                     Bank Santai
               Solusi Anggaran Nyaman
                 Tanpa Alasan rIbet
        ======================================
        Username          : {username}
        Jumlah Pinjaman   : Rp {safe_float(loan_amount):,.2f}
        Durasi Pembayaran : {loan_duration} bulan
        Mode Cicilan      : {mode.capitalize()}

        Detail Cicilan Per Bulan:
        {formatted_payments}

        ======================================
        Pembayaran pertama: Rp {safe_float(monthly_payments[0]):,.2f}
        
        Reminder!!!
        Jangan lupa bayar tepat waktu yaaa
        ======================================
        """

        # Membuat jendela untuk pratinjau struk
        receipt_window = tk.Toplevel(window)
        receipt_window.title("Pratinjau Struk")
        receipt_window.geometry("600x500")
        
        # Widget teks untuk menampilkan struk
        text_receipt = tk.Text(receipt_window, wrap=tk.WORD)
        text_receipt.insert(tk.END, receipt_text)
        text_receipt.config(state=tk.DISABLED)  # Nonaktifkan pengeditan
        text_receipt.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Tombol untuk menyimpan struk sebagai gambar
        button_save = tk.Button(
            receipt_window,
            text="Simpan Struk",
            command=lambda: save_receipt_as_image(receipt_text)
        )
        button_save.pack(pady=10)

        # Tombol untuk menutup jendela
        button_close = tk.Button(receipt_window, text="Tutup", command=receipt_window.destroy)
        button_close.pack(pady=5)

    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

def save_receipt_as_image(receipt_text):
    # Set ukuran gambar awal
    width, height = 300, 400
    background_color = "white"
    text_color = "black"
    font_size = 20

    # Membuat gambar kosong sementara
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    # Menggunakan font default Pillow
    font = ImageFont.load_default()

    # Hitung tinggi setiap baris teks menggunakan `textbbox`
    line_spacing = 10 
    margin = 20
    lines = receipt_text.split("\n")
    max_line_width = 0
    total_height = margin
    line_dimensions = []

    for line in lines:
        bbox = draw.textbbox((0, 0), line.strip(), font=font)
        line_width = bbox[2] - bbox[0]
        line_height = bbox[3] - bbox[1]
        max_line_width = max(max_line_width, line_width)
        total_height += line_height + line_spacing
        line_dimensions.append((line.strip(), line_width, line_height))

    # Perbarui ukuran gambar sesuai teks
    width = max(max_line_width + 2 * margin, width)
    height = max(total_height + margin, height)
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    # Gambar teks ke gambar
    y = margin
    for line, line_width, line_height in line_dimensions:
        x = margin
        draw.text((x, y), line, fill=text_color, font=font)
        y += line_height + line_spacing

    # Menyimpan gambar
    filepath = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("Image files", "*.png"), ("All files", "*.*")],
        title="Simpan Struk sebagai Gambar")
    if filepath:
        image.save(filepath)
        messagebox.showinfo("Berhasil", f"Struk berhasil disimpan!")

# Fungsi untuk menyimpan struk ke file
def save_receipt(receipt):
    filepath = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        title="Simpan Struk")
    if filepath:
        with open(filepath, "w") as file:
            file.write(receipt)
        messagebox.showinfo("Berhasil", "Struk berhasil disimpan!")
        
def safe_float(value):
    try:
        if isinstance(value, str):
            value = value.replace("Rp", "").replace(",", "").strip()  # Menghapus simbol atau pemisah ribuan
        return float(value)
    except ValueError:
        return 0.0  # Mengembalikan nilai default jika gagal konversi

def calculate_loan(loan_amount_entry, loan_duration_entry, mode, username):
    try:
        loan_amount = float(loan_amount_entry.get())
        loan_duration = int(loan_duration_entry.get())

        if mode == "fixed":
           monthly_payment = calculate_fixed_payment(loan_amount, loan_duration, interest_rate)
           result = [monthly_payment] * loan_duration
        elif mode == "decreasing":
           result = calculate_decreasing_payment(loan_amount, loan_duration, interest_rate)
        elif mode == "flexible":
           result = calculate_flexible_payment(loan_amount, loan_duration, interest_rate)

        # Konversi hasil ke string dengan format yang benar
        result_str = [f"{safe_float(payment):,.2f}" for payment in result]

        # Buat jendela hasil
        result_window = tk.Toplevel(window)
        result_window.title("Hasil Cicilan")
        result_window.geometry("600x400")
        result_window.configure(background="pink")

        label_result_title = tk.Label(result_window, text="Hasil Cicilan", font=("Century Gothic", 16))
        label_result_title.pack(pady=10)

        text_result = tk.Text(result_window, height=15, width=50)
        text_result.pack(pady=10)
        text_result.insert(tk.END, "\n".join([f"Bulan {i+1}: Rp {payment}" for i, payment in enumerate(result_str)]))
        text_result.config(state="disabled")

        # Tambahkan tombol Cetak Struk
        button_receipt = tk.Button(
            result_window,
            text="Cetak Struk",
            command=lambda: print_receipt(username, loan_amount, loan_duration, result_str, mode))
        button_receipt.pack(pady=10)

        button_close = tk.Button(result_window, text="Tutup", command=result_window.destroy)
        button_close.pack(pady=10)

    except ValueError:
        messagebox.showerror("Error", "Masukkan jumlah pinjaman dan durasi yang valid!")

def safe_float(value):
    """Menghapus pemisah ribuan dari string dan mengonversinya ke float."""
    if isinstance(value, str):
        return float(value.replace(',', '').strip())
    return float(value)

# Tampilan dashboard admin
def admin_dashboard():
    global entry_duration
    for widget in window.winfo_children():
        widget.destroy()

    try:
        # Load gambar latar belakang
        import os
        from PIL import Image, ImageTk
        # Path relatif ke gambar
        file_path = os.path.join(os.path.dirname(__file__), "5.png")
        background_image = Image.open(file_path)

        # Tentukan ukuran maksimum
        max_width, max_height = 1568, 868

        # Dapatkan ukuran asli gambar
        original_width, original_height = background_image.size

        # Hitung rasio skala
        scale = min(max_width / original_width, max_height / original_height)

        # Hitung ukuran baru berdasarkan rasio
        new_width = int(original_width * scale)
        new_height = int(original_height * scale)

        # Ubah ukuran gambar
        resized_image = background_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        bg_photo = ImageTk.PhotoImage(resized_image)

        # Buat canvas sesuai ukuran gambar yang diubah
        canvas = tk.Canvas(window, width=new_width, height=new_height)
        canvas.pack(fill="both", expand=True)

        # Tampilkan gambar sebagai latar belakang
        canvas.create_image(0, 0, image=bg_photo, anchor="nw")

        # Simpan referensi gambar agar tidak dihapus oleh garbage collector
        canvas.image = bg_photo

        # Tambahkan elemen-elemen GUI di atas gambar latar belakang
        listbox_durations = tk.Listbox(window, height=10)
        canvas.create_window(770, 230, window=listbox_durations)
        for dur in durations:
            listbox_durations.insert(tk.END, dur)

        # Entry untuk durasi baru
        entry_duration = tk.Entry(window)  # Inisialisasi variabel
        canvas.create_window(770, 340, window=entry_duration)

        # Tombol Tambah Durasi
        def add_duration():
            try:
                new_duration = int(entry_duration.get())  # Menggunakan entry_duration yang terdefinisi
                if new_duration not in durations:
                    durations.append(new_duration)
                    durations.sort()
                    listbox_durations.delete(0, tk.END)
                    for dur in durations:
                        listbox_durations.insert(tk.END, dur)
                    messagebox.showinfo("Berhasil", "Durasi berhasil ditambahkan!")
                else:
                    messagebox.showwarning("Gagal", "Durasi sudah ada!")
            except ValueError:
                messagebox.showerror("Error", "Masukkan nilai durasi yang valid!")

        button_add = tk.Button(window, text="Tambah Durasi", font=("Century Gothic", 15), bg="white", fg="purple",
                               cursor="hand2", command=add_duration)
        canvas.create_window(770, 385, window=button_add)

        # Tombol Hapus Durasi
        def delete_duration():
            try:
                selected = listbox_durations.curselection()
                if selected:
                    durations.remove(int(listbox_durations.get(selected)))
                    listbox_durations.delete(selected)
                    messagebox.showinfo("Berhasil", "Durasi berhasil dihapus!")
                else:
                    messagebox.showwarning("Gagal", "Pilih durasi yang ingin dihapus!")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        button_delete = tk.Button(window, text="Hapus Durasi", font=("Century Gothic", 15), bg="white", fg="purple",
                                  cursor="hand2", command=delete_duration)
        canvas.create_window(770, 440, window=button_delete)

        # Bagian untuk mengatur suku bunga
        label_interest = tk.Label(window, text=f"Suku Bunga Saat Ini: {interest_rate:.2f}%", font=("Century Gothic", 15),
                                   bg="white", fg="purple")
        canvas.create_window(770, 490, window=label_interest)

        entry_interest = tk.Entry(window)
        canvas.create_window(770, 540, window=entry_interest)

        def update_interest():
            global interest_rate
            try:
                new_interest = float(entry_interest.get())
                interest_rate = new_interest
                label_interest.config(text=f"Suku Bunga Saat Ini: {interest_rate:.2f}%")
                messagebox.showinfo("Berhasil", "Suku bunga berhasil diubah!")
            except ValueError:
                messagebox.showerror("Error", "Masukkan nilai suku bunga yang valid!")

        button_update_interest = tk.Button(window, text="Ubah Suku Bunga", font=("Century Gothic", 15), bg="white",
                                           fg="purple", cursor="hand2", command=update_interest)
        canvas.create_window(770, 590, window=button_update_interest)

        button_logout = tk.Button(window, text="Logout", font=("Century Gothic", 15), bg="white", fg="purple",
                                  cursor="hand2", command=login_screen)
        canvas.create_window(770, 685, window=button_logout)

    except FileNotFoundError as e:
        messagebox.showerror("Error", f"Gambar tidak ditemukan: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

# Inisialisasi GUI 
window = tk.Tk()
window.title("Aplikasi Sistem Pembayaran Cicilan")
window.state=('zoomed')
window.resizable(True, True)  # Memungkinkan resize untuk horizontal dan vertikal
window.configure(background="pink")
show_cover()
window.mainloop()
