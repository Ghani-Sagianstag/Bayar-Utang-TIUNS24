import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont
from rumus import (
    calculate_fixed_payment, calculate_decreasing_payment, 
    calculate_flexible_payment, save_user_data, load_users, 
    load_admin, safe_float)

interest_rate = 6
durations = [3, 6, 9, 12, 24, 36]

def show_cover(window):
    for widget in window.winfo_children():
        widget.destroy()
    try:
        file_path = "1.png"
        background_image = Image.open(file_path)
        resized_image = background_image.resize((1536, 861), Image.Resampling.LANCZOS)
        bg_photo = ImageTk.PhotoImage(resized_image)

        canvas = tk.Canvas(window, width=1536, height=837)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg_photo, anchor="nw")
        canvas.image = bg_photo

        button_next = tk.Button(window, text="Masuk", command=lambda: login_screen(window),
                                font=("Century Gothic", 14), bg="white", fg="purple", cursor="hand2", pady=10, padx=20)
        canvas.create_window(760, 750, window=button_next)
    except FileNotFoundError:
        messagebox.showerror("Error", "Gambar tidak ditemukan!")

def login_screen(window):
    for widget in window.winfo_children():
        widget.destroy()
    try:
        file_path = "2.png"
        background_image = Image.open(file_path)
        resized_image = background_image.resize((1536, 861), Image.Resampling.LANCZOS)
        bg_photo = ImageTk.PhotoImage(resized_image)

        canvas = tk.Canvas(window, width=1536, height=861)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg_photo, anchor="nw")
        canvas.image = bg_photo

        entry_username = tk.Entry(window)
        canvas.create_window(770, 240, window=entry_username)

        entry_password = tk.Entry(window, show="*")
        canvas.create_window(770, 325, window=entry_password)

        def login():
            username = entry_username.get()
            password = entry_password.get()

            users = load_users()
            admin_data = load_admin()

            if username == admin_data["username"] and password == admin_data["password"]:
                admin_dashboard(window)
            elif username in users and users[username]["password"] == password:
                user_dashboard(window, username)
            else:
                messagebox.showerror("Login Gagal", "Username atau password salah!")

        button_login = tk.Button(window, text="Login", command=login, bg="white", fg="purple", 
                                 cursor="hand2", font=("Century Gothic", 14))
        canvas.create_window(770, 370, window=button_login)

        button_signup = tk.Button(window, text="Sign Up", command=lambda: signup_screen(window),
                                  bg="white", fg="purple", cursor="hand2", font=("Century Gothic", 14))
        canvas.create_window(770, 480, window=button_signup)
        
        button_home = tk.Button(window, text="Home", font=("Century Gothic", 15), cursor="hand2", 
                                bg="white", fg="purple", command=lambda: show_cover(window))
        canvas.create_window(770, 600, window=button_home)

    except FileNotFoundError:
        messagebox.showerror("Error", "Gambar tidak ditemukan!")

def signup_screen(window):
    for widget in window.winfo_children():
        widget.destroy()
    try:
        file_path = "3.png"
        background_image = Image.open(file_path)
        resized_image = background_image.resize((1536, 861), Image.Resampling.LANCZOS)
        bg_photo = ImageTk.PhotoImage(resized_image)

        canvas = tk.Canvas(window, width=1536, height=861)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg_photo, anchor="nw")
        canvas.image = bg_photo

        entry_username = tk.Entry(window)
        canvas.create_window(770, 240, window=entry_username)

        entry_password = tk.Entry(window, show="*")
        canvas.create_window(770, 325, window=entry_password)

        def signup():
            username = entry_username.get()
            password = entry_password.get()

            if username and password:
                save_user_data(username, password)
                messagebox.showinfo("Pendaftaran Berhasil", "Akun berhasil dibuat!")
                login_screen(window)
            else:
                messagebox.showerror("Kesalahan", "Username dan password tidak boleh kosong!")

        button_signup = tk.Button(window, text="Sign Up", command=signup, bg="white", fg="purple", 
                                  cursor="hand2", font=("Century Gothic", 14))
        canvas.create_window(770, 380, window=button_signup)

        button_back = tk.Button(window, text="Kembali ke Login", command=lambda: login_screen(window),
                                bg="white", fg="purple", cursor="hand2", font=("Century Gothic", 14))
        canvas.create_window(770, 600, window=button_back)

    except FileNotFoundError:
        messagebox.showerror("Error", "Gambar tidak ditemukan!")

def user_dashboard(window, username):
    for widget in window.winfo_children():
        widget.destroy()
    try:
        file_path = "4.png"
        background_image = Image.open(file_path)
        resized_image = background_image.resize((1536, 861), Image.Resampling.LANCZOS)
        bg_photo = ImageTk.PhotoImage(resized_image)

        canvas = tk.Canvas(window, width=1536, height=861)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg_photo, anchor="nw")
        canvas.image = bg_photo

        entry_loan_amount = tk.Entry(window)
        canvas.create_window(770, 190, window=entry_loan_amount)

        duration_var = tk.IntVar(value=3)
        dropdown_duration = tk.OptionMenu(window, duration_var, *durations)
        canvas.create_window(770, 276, window=dropdown_duration)

        mode_var = tk.StringVar(value="fixed")
        radio_fixed = tk.Radiobutton(window, text="Cicilan Tetap", variable=mode_var, value="fixed", 
                                     font=("Century Gothic", 14), bg="white", fg="purple", cursor="hand2")
        canvas.create_window(770, 365, window=radio_fixed)

        radio_decreasing = tk.Radiobutton(window, text="Cicilan Menurun", variable=mode_var, value="decreasing", 
                                          font=("Century Gothic", 14), bg="white", fg="purple", cursor="hand2")
        canvas.create_window(770, 405, window=radio_decreasing)

        radio_flexible = tk.Radiobutton(window, text="Cicilan Fluktuasi BI-Rate", variable=mode_var, value="flexible", 
                                        font=("Century Gothic", 14), bg="white", fg="purple", cursor="hand2")
        canvas.create_window(770, 445, window=radio_flexible)

        def calculate_loan():
            try:
                principal = float(entry_loan_amount.get())
                months = duration_var.get()
                mode = mode_var.get()

                if mode == "fixed":
                    payments = [calculate_fixed_payment(principal, months, interest_rate)] * months
                elif mode == "decreasing":
                    payments = calculate_decreasing_payment(principal, months, interest_rate)
                elif mode == "flexible":
                    payments = calculate_flexible_payment(principal, months, interest_rate)

                # Panggil fungsi untuk mencetak struk
                print_receipt(window, username, principal, months, payments, mode)

            except ValueError:
                messagebox.showerror("Error", "Masukkan jumlah pinjaman yang valid!")

        button_calculate = tk.Button(window, text="Hitung Cicilan", command=calculate_loan, bg="white", fg="purple", font=("Century Gothic", 14))
        canvas.create_window(770, 550, window=button_calculate)
        
        button_logout = tk.Button(window, text="Logout", font=("Century Gothic", 15), bg="white", fg="purple",
                                  cursor="hand2", command=login_screen)
        canvas.create_window(770, 700, window=button_logout)  

    except FileNotFoundError:
        messagebox.showerror("Error", "Gambar tidak ditemukan!")

def print_receipt(window, username, loan_amount, loan_duration, monthly_payments, mode):
    try:
        # Format cicilan per bulan
        formatted_payments = "\n".join(
            [f"{'Bulan':<10}{str(i+1):>3} : {'Rp':<3} {safe_float(payment):>15,.2f}" for i, payment in enumerate(monthly_payments)]
        )

        # Membuat isi struk
        receipt_text = (
            "======================================\n"
            "             Bank Santai\n"
            "       Solusi Anggaran Nyaman\n"
            "         Tanpa Alasan rIbet\n"
            "======================================\n"
            f"Username          : {username}\n"
            f"Jumlah Pinjaman   : Rp {safe_float(loan_amount):,.2f}\n"
            f"Durasi Pembayaran : {loan_duration} bulan\n"
            f"Mode Cicilan      : {mode.capitalize()}\n\n"
            "Detail Cicilan Per Bulan:\n"
            f"{formatted_payments}\n\n"
            "======================================\n"
            f"Pembayaran pertama: Rp {safe_float(monthly_payments[0]):,.2f}\n\n"
            "Reminder!!!\n"
            "Jangan lupa bayar tepat waktu yaaa\n"
            "======================================"
        )

        # Jendela pratinjau struk
        receipt_window = tk.Toplevel(window)
        receipt_window.title("Pratinjau Struk")
        receipt_window.geometry("400x500")

        # Teks struk menggunakan font monospasi
        text_receipt = tk.Text(receipt_window, wrap=tk.WORD, font=("Courier New", 10))
        text_receipt.insert(tk.END, receipt_text)
        text_receipt.config(state=tk.DISABLED)
        text_receipt.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Tombol untuk menyimpan struk
        button_save = tk.Button(
            receipt_window,
            text="Simpan Struk",
            command=lambda: save_as_image(receipt_text, window),
            bg="white", fg="purple"
        )
        button_save.pack(pady=10)

        # Tombol untuk menutup jendela
        button_close = tk.Button(receipt_window, text="Tutup", command=receipt_window.destroy)
        button_close.pack(pady=5)

    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

def save_as_image(receipt_text, window):
    try:
        # Dialog untuk menentukan path penyimpanan
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
            title="Simpan Struk Sebagai"
        )
        
        if not file_path:
            return  # Jika pengguna membatalkan dialog, fungsi berhenti

        # Mengatur ukuran kanvas dan font
        try:
            font = ImageFont.truetype("Courier New.ttf", 16)  # Font monospasi
        except IOError:
            font = ImageFont.load_default()  # Fallback jika font tidak ditemukan

        lines = receipt_text.split("\n")
        line_height = 25
        img_width = 250  # Lebar struk seperti struk nyata
        img_height = line_height * len(lines) + 40  # Tambahkan margin atas/bawah

        # Membuat kanvas kosong
        img = Image.new("RGB", (img_width, img_height), color="white")
        draw = ImageDraw.Draw(img)

        # Menentukan posisi awal teks
        y = 10  # Margin atas
        for line in lines:
            # Periksa apakah baris adalah judul
            if "Bank Santai" in line or "Solusi Anggaran Nyaman" in line or "Tanpa Alasan rIbet" in line:
                line_width = draw.textlength(line, font=font)
                x = (img_width - line_width) // 2  # Rata tengah untuk judul
            else:
                x = 10  # Rata kiri untuk teks biasa
            draw.text((x, y), line, fill="black", font=font)
            y += line_height

        # Menyimpan sebagai PNG
        img.save(file_path)
        messagebox.showinfo("Sukses", f"Yayy struk berhasil disimpan")

        # Lanjutkan ke halaman "Thank You"
        show_thank_you_message(window)

    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan saat menyimpan struk: {e}")

def show_thank_you_message(window):
    for widget in window.winfo_children():
        widget.destroy()

    try:
        # Background "Thank You"
        file_path = "6.png" 
        background_image = Image.open(file_path)
        resized_image = background_image.resize((1536, 861), Image.Resampling.LANCZOS)
        bg_photo = ImageTk.PhotoImage(resized_image)

        canvas = tk.Canvas(window, width=1536, height=861)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg_photo, anchor="nw")
        canvas.image = bg_photo

        # Tombol Home
        button_home = tk.Button(window, text="Home", command=lambda: show_cover(window),
                                font=("Century Gothic", 15), bg="white", fg="purple", cursor="hand2")
        canvas.create_window(770, 590, window=button_home)

        # Tombol Logout
        button_logout = tk.Button(window, text="Logout", command=lambda: login_screen(window),
                                  font=("Century Gothic", 15), bg="white", fg="purple", cursor="hand2")
        canvas.create_window(770, 650, window=button_logout)

    except FileNotFoundError:
        messagebox.showerror("Error", "Gambar tidak ditemukan!")

def admin_dashboard(window):
    for widget in window.winfo_children():
        widget.destroy()
    try:
        file_path = "5.png"
        background_image = Image.open(file_path)
        resized_image = background_image.resize((1536, 861), Image.Resampling.LANCZOS)
        bg_photo = ImageTk.PhotoImage(resized_image)

        canvas = tk.Canvas(window, width=1536, height=861)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg_photo, anchor="nw")
        canvas.image = bg_photo

        listbox_durations = tk.Listbox(window, height=10)
        canvas.create_window(770, 230, window=listbox_durations)
        for dur in durations:
            listbox_durations.insert(tk.END, dur)

        entry_duration = tk.Entry(window) 
        canvas.create_window(770, 340, window=entry_duration)

        def add_duration():
            try:
                new_duration = int(entry_duration.get()) 
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

        label_interest = tk.Label(window, text=f"Suku Bunga Saat Ini: {interest_rate:.2f}%", font=("Century Gothic", 15),
                                  cursor="hand2", bg="white", fg="purple")
        canvas.create_window(770, 490, window=label_interest)

        entry_interest = tk.Entry(window)
        canvas.create_window(770, 540, window=entry_interest)

        def update_interest():
            global interest_rate
            try:
                new_interest = float(entry_interest.get())
                interest_rate = new_interest
                label_interest.config(text=f"Suku Bunga Saat Ini: {interest_rate:.2f}%")
                messagebox.showinfo("Berhasil", f"Suku bunga diperbarui menjadi {interest_rate:.2f}%")
            except ValueError:
                messagebox.showerror("Error", "Masukkan nilai suku bunga yang valid!")

        button_update = tk.Button(window, text="Perbarui Suku Bunga", command=update_interest, cursor="hand2",
                                  bg="white", fg="purple", font=("Century Gothic", 14))
        canvas.create_window(770, 590, window=button_update)

        button_logout = tk.Button(window, text="Logout", font=("Century Gothic", 15), bg="white", fg="purple",
                          cursor="hand2", command=lambda: login_screen(window))
        canvas.create_window(770, 685, window=button_logout)

    except FileNotFoundError:
        messagebox.showerror("Error", "Gambar tidak ditemukan!")

def run_app():
    window = tk.Tk()
    window.title("Aplikasi Sistem Pembayaran Cicilan")
    window.state=('zoomed')
    show_cover(window)
    window.mainloop()

if __name__ == "__main__":
    run_app()
