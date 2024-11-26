import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import json

durations = [3, 6, 9, 12, 24, 36]  # Default pilihan durasi

# Fungsi untuk menampilkan cover depan



# Fungsi untuk menyimpan data pengguna ke dalam file JSON
def save_user_data(username, password):
    users = load_users()
    users[username] = {"password": password}
    with open('users.json', 'w') as f:
        json.dump(users, f)

# Fungsi untuk memuat data pengguna dari file JSON
def load_users():
    try:
        with open('users.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Fungsi untuk menyimpan data admin
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

# Tampilan dashboard admin
def admin_dashboard():
    for widget in window.winfo_children():
        widget.destroy()

    label_title = tk.Label(window, text="Dashboard Admin", font=("Arial", 16))
    label_title.pack(pady=20)

    # Listbox untuk menampilkan durasi yang tersedia
    label_duration = tk.Label(window, text="Durasi Cicilan (bulan):")
    label_duration.pack(pady=10)

    listbox_durations = tk.Listbox(window, height=10)
    listbox_durations.pack(pady=5)
    for dur in durations:
        listbox_durations.insert(tk.END, dur)

    # Input untuk menambah atau mengganti durasi
    entry_duration = tk.Entry(window)
    entry_duration.pack(pady=5)

    def add_duration():
        try:
            new_duration = int(entry_duration.get())
            if new_duration not in durations:
                durations.append(new_duration)
                durations.sort()
                listbox_durations.insert(tk.END, new_duration)
                messagebox.showinfo("Berhasil", "Durasi berhasil ditambahkan!")
            else:
                messagebox.showwarning("Gagal", "Durasi sudah ada!")
        except ValueError:
            messagebox.showerror("Error", "Masukkan nilai durasi yang valid!")

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

    button_add = tk.Button(window, text="Tambah Durasi", command=add_duration)
    button_add.pack(pady=5)

    button_delete = tk.Button(window, text="Hapus Durasi", command=delete_duration)
    button_delete.pack(pady=5)

    button_logout = tk.Button(window, text="Logout", command=login_screen)
    button_logout.pack(pady=10)

# Fungsi untuk mengatur suku bunga admin
def set_interest(entry):
    global interest_rate
    try:
        interest_rate = float(entry.get())
        messagebox.showinfo("Suku Bunga", f"Suku bunga berhasil diubah menjadi {interest_rate}%")
    except ValueError:
        messagebox.showerror("Error", "Masukkan nilai suku bunga yang valid!")

# Fungsi untuk mengatur durasi cicilan admin
def set_duration(entry):
    global loan_duration
    try:
        loan_duration = int(entry.get())
        messagebox.showinfo("Durasi Cicilan", f"Durasi cicilan berhasil diubah menjadi {loan_duration} bulan.")
    except ValueError:
        messagebox.showerror("Error", "Masukkan nilai durasi yang valid!")

# Tampilan dashboard user
def user_dashboard(username):
    for widget in window.winfo_children():
        widget.destroy()

    label_title = tk.Label(window, text="Dashboard User", font=("Arial", 16))
    label_title.pack(pady=20)

    label_loan_amount = tk.Label(window, text="Jumlah Pinjaman (Rp):")
    label_loan_amount.pack(pady=10)

    entry_loan_amount = tk.Entry(window)
    entry_loan_amount.pack(pady=5)

    # Dropdown untuk pilihan durasi cicilan
    label_loan_duration = tk.Label(window, text="Durasi Cicilan (bulan):")
    label_loan_duration.pack(pady=10)

    duration_var = tk.IntVar(value=durations[0])  # Pilihan awal
    dropdown_duration = tk.OptionMenu(window, duration_var, *durations)
    dropdown_duration.pack(pady=5)

    label_payment_mode = tk.Label(window, text="Pilih Mode Cicilan:")
    label_payment_mode.pack(pady=10)

    mode_var = tk.StringVar(value="fixed")
    radio_fixed = tk.Radiobutton(window, text="Cicilan Tetap", variable=mode_var, value="fixed")
    radio_fixed.pack()

    radio_decreasing = tk.Radiobutton(window, text="Cicilan Menurun", variable=mode_var, value="decreasing")
    radio_decreasing.pack()

    radio_flexible = tk.Radiobutton(window, text="Cicilan Fluktuasi BI-Rate", variable=mode_var, value="flexible")
    radio_flexible.pack()

    button_calculate = tk.Button(
    window,
    text="Hitung Cicilan",
    command=lambda: calculate_loan(entry_loan_amount, duration_var, mode_var.get())
    )
    button_calculate.pack(pady=20)

    button_logout = tk.Button(window, text="Logout", command=login_screen)
    button_logout.pack(pady=10)
    
# Fungsi untuk menghitung cicilan berdasarkan mode yang dipilih
def calculate_loan(loan_amount_entry, loan_duration_entry, mode):
    try:
        loan_amount = float(loan_amount_entry.get())
        loan_duration = int(loan_duration_entry.get())

        # Hitung cicilan berdasarkan mode
        if mode == "fixed":
            monthly_payment = calculate_fixed_payment(loan_amount, loan_duration, interest_rate)
            result = [f"Bulan {i+1}: Rp {monthly_payment:,.2f}" for i in range(loan_duration)]
        elif mode == "decreasing":
            result = calculate_decreasing_payment(loan_amount, loan_duration, interest_rate)
            result = [f"Bulan {i+1}: Rp {payment:,.2f}" for i, payment in enumerate(result)]
        elif mode == "flexible":
            result = calculate_flexible_payment(loan_amount, loan_duration, interest_rate)
            result = [f"Bulan {i+1}: Rp {payment:,.2f}" for i, payment in enumerate(result)]

        # Buat jendela baru untuk menampilkan hasil
        result_window = tk.Toplevel(window)
        result_window.title("Hasil Cicilan")
        result_window.geometry("1000x1000")

        label_result_title = tk.Label(result_window, text="Hasil Cicilan", font=("Arial", 16))
        label_result_title.pack(pady=10)

        text_result = tk.Text(result_window, height=20, width=50, state="normal")
        text_result.pack(pady=50)

        # Tampilkan hasil di jendela baru
        text_result.insert(tk.END, "\n".join(result))
        text_result.config(state="disabled")

        button_close = tk.Button(result_window, text="Tutup", command=result_window.destroy)
        button_close.pack(pady=10)

    except ValueError:
        messagebox.showerror("Error", "Masukkan jumlah pinjaman dan durasi yang valid!")

# Tampilan login
# Tampilan login
def login_screen():
    for widget in window.winfo_children():
        widget.destroy()

    label_title = tk.Label(window, text="Login", font=("Times New Roman", 30))
    label_title.pack(pady=20)

    label_username = tk.Label(window, text="Username:")
    label_username.pack(pady=5)

    global entry_username
    global entry_password

    entry_username = tk.Entry(window)
    entry_username.pack(pady=5)

    label_password = tk.Label(window, text="Password:")
    label_password.pack(pady=5)

    entry_password = tk.Entry(window, show="*")
    entry_password.pack(pady=5)

    button_login = tk.Button(window, text="Login", command=login)
    button_login.pack(pady=20)

    label_signup_prompt = tk.Label(window, text="Apabila belum memiliki akun, silahkan Sign Up")
    label_signup_prompt.pack(pady=5)

    button_to_signup = tk.Button(window, text="Sign Up", command=signup_screen)
    button_to_signup.pack(pady=10)

# Tampilan sign-up
def signup_screen():
    for widget in window.winfo_children():
        widget.destroy()

    label_title = tk.Label(window, text="Sign Up", font=("Times New Roman", 30))
    label_title.pack(pady=20)

    label_username = tk.Label(window, text="Username:")
    label_username.pack(pady=5)

    global entry_username
    global entry_password

    entry_username = tk.Entry(window)
    entry_username.pack(pady=5)

    label_password = tk.Label(window, text="Password:")
    label_password.pack(pady=5)

    entry_password = tk.Entry(window, show="*")
    entry_password.pack(pady=5)

    button_signup = tk.Button(window, text="Sign Up", command=signup)
    button_signup.pack(pady=20)

    button_to_login = tk.Button(window, text="Kembali ke Login", command=login_screen)
    button_to_login.pack(pady=10)

def signup():
    username = entry_username.get()
    password = entry_password.get()

    if username and password:
        save_user_data(username, password)
        messagebox.showinfo("Pendaftaran Berhasil", "Akun berhasil dibuat!")
        login_screen()
    else:
        messagebox.showerror("Kesalahan", "Username dan password tidak boleh kosong!")


# Inisialisasi GUI
window = tk.Tk()
window.title("Aplikasi Sistem Pembayaran Cicilan")
window.geometry("1920x1080")


def show_cover():
    try:
        # Gunakan raw string literal untuk mencegah error unicode escape
        file_path = r"c:\Users\asus\AppData\Local\Temp\e2c9bc3f-ea44-4cd1-a9ee-323fa45026a1_Teks paragraf Anda (3840 x 2160 piksel) (3).zip.6a1\1.png"
        background_image = Image.open(file_path)
        bg_photo = ImageTk.PhotoImage(background_image)

        # Tambahkan Canvas untuk gambar background
        canvas = tk.Canvas(window, width=background_image.width, height=background_image.height)
        canvas.pack(fill="both", expand=True)

        # Tampilkan gambar pada Canvas
        canvas.create_image(0, 0, image=bg_photo, anchor="nw")

        # Simpan referensi gambar agar tidak dihapus oleh garbage collector
        canvas.image = bg_photo

        # Tambahkan tombol di atas background
        button_next = tk.Button(window, text="Next", command=login_screen, font=("Arial", 14), pady=10, padx=20)
        button_next_window = canvas.create_window(760, 750, anchor="center", window=button_next)

    except FileNotFoundError as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", f"Gambar tidak ditemukan: {e}")
    except Exception as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")
    
# Panggil fungsi cover saat aplikasi dimulai
show_cover()


# Default suku bunga dan durasi cicilan
interest_rate = 6  # Suku bunga default adalah 6% sesuai dengan BI-Rate
loan_duration = 12  # Durasi cicilan default adalah 12 bulan

show_cover()

window.mainloop()
