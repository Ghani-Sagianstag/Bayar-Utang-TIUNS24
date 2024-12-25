import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont
import json 
from rumus import (
    calculate_fixed_payment, calculate_decreasing_payment, calculate_flexible_payment, save_bi_rate, load_bi_rate, 
    save_durations, load_durations, save_user_data, load_users, load_admin, safe_float, save_installment_data)

interest_rate = 5
bi_rate = load_bi_rate()
durations = load_durations()
installments_file = "installments.json"

def show_cover(window, screen_width, screen_height):
    for widget in window.winfo_children():
        widget.destroy()
    try:
        file_path = "1.png"
        background_image = Image.open(file_path)
        resized_image = background_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
        bg_photo = ImageTk.PhotoImage(resized_image)

        canvas = tk.Canvas(window, width=screen_width, height=screen_height)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg_photo, anchor="nw")
        canvas.image = bg_photo

        button_next = tk.Button(window, text="Masuk", command=lambda: login_screen(window, screen_width, screen_height),
                                font=("Century Gothic", 14), bg="white", fg="purple", cursor="hand2", pady=10, padx=20)
        canvas.create_window(screen_width // 2.2, int(screen_height * 0.87), window=button_next)
        
        button_exit = tk.Button(window, text="Keluar", command=window.destroy,
                                font=("Century Gothic", 14), bg="white", fg="red", cursor="hand2", pady=10, padx=20)
        canvas.create_window(screen_width // 1.8, int(screen_height * 0.87), window=button_exit)

    except FileNotFoundError:
        messagebox.showerror("Error", "Gambar tidak ditemukan!")

def login_screen(window, screen_width, screen_height):
    for widget in window.winfo_children():
        widget.destroy()
    try:
        file_path = "2.png"
        background_image = Image.open(file_path)
        resized_image = background_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
        bg_photo = ImageTk.PhotoImage(resized_image)

        canvas = tk.Canvas(window, width=screen_width, height=screen_height)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg_photo, anchor="nw")
        canvas.image = bg_photo

        entry_username = tk.Entry(window)
        canvas.create_window(screen_width // 2, int(screen_height * 0.28), window=entry_username)

        entry_password = tk.Entry(window, show="*")
        canvas.create_window(screen_width // 2, int(screen_height * 0.38), window=entry_password)

        def login():
            username = entry_username.get()
            password = entry_password.get()

            users = load_users()
            admin_data = load_admin()

            if username == admin_data["username"] and password == admin_data["password"]:
                admin_dashboard(window, screen_width, screen_height)
            elif username in users and users[username]["password"] == password:
                user_dashboard(window, username, screen_width, screen_height)
            else:
                messagebox.showerror("Login Gagal", "Username atau password salah!")

        button_login = tk.Button(window, text="Login", command=login, bg="white", fg="purple", 
                                 cursor="hand2", font=("Century Gothic", 14))
        canvas.create_window(screen_width // 2, int(screen_height * 0.43), window=button_login)

        button_signup = tk.Button(window, text="Sign Up", command=lambda: signup_screen(window, screen_width, screen_height),
                                  bg="white", fg="purple", cursor="hand2", font=("Century Gothic", 14))
        canvas.create_window(screen_width // 2, int(screen_height * 0.55), window=button_signup)
        
        button_home = tk.Button(window, text="Home", font=("Century Gothic", 15), cursor="hand2", 
                                bg="white", fg="purple", command=lambda: show_cover(window, screen_width, screen_height))
        canvas.create_window(screen_width // 2, int(screen_height * 0.68), window=button_home)

    except FileNotFoundError:
        messagebox.showerror("Error", "Gambar tidak ditemukan!")

def signup_screen(window, screen_width, screen_height):
    for widget in window.winfo_children():
        widget.destroy()
    try:
        file_path = "3.png"
        background_image = Image.open(file_path)
        resized_image = background_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
        bg_photo = ImageTk.PhotoImage(resized_image)

        canvas = tk.Canvas(window, width=screen_width, height=screen_height)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg_photo, anchor="nw")
        canvas.image = bg_photo

        entry_username = tk.Entry(window)
        canvas.create_window(screen_width // 2, int(screen_height * 0.28), window=entry_username)

        entry_password = tk.Entry(window, show="*")
        canvas.create_window(screen_width // 2, int(screen_height * 0.38), window=entry_password)

        def signup():
            username = entry_username.get()
            password = entry_password.get()

            if username and password:
                save_user_data(username, password)
                messagebox.showinfo("Pendaftaran Berhasil", "Akun berhasil dibuat!")
                login_screen(window, screen_width, screen_height) 
            else:
                messagebox.showerror("Kesalahan", "Username dan password tidak boleh kosong!")

        button_signup = tk.Button(window, text="Sign Up", command=signup, bg="white", fg="purple", 
                                  cursor="hand2", font=("Century Gothic", 14))
        canvas.create_window(screen_width // 2, int(screen_height * 0.45), window=button_signup)

        button_back = tk.Button(window, text="Kembali ke Login", command=lambda: login_screen(window, screen_width, screen_height),
                                bg="white", fg="purple", cursor="hand2", font=("Century Gothic", 14))
        canvas.create_window(screen_width // 2, int(screen_height * 0.78), window=button_back)

    except FileNotFoundError:
        messagebox.showerror("Error", "Gambar tidak ditemukan!")

def user_dashboard(window, username, screen_width, screen_height):
    for widget in window.winfo_children():
        widget.destroy()

    try:
        file_path = "8.png"
        background_image = Image.open(file_path)
        resized_image = background_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
        bg_photo = ImageTk.PhotoImage(resized_image)

        canvas = tk.Canvas(window, width=screen_width, height=screen_height)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg_photo, anchor="nw")
        canvas.image = bg_photo
        
        label_welcome = tk.Label(window, text=f"{username}", font=("Century Gothic", 20), bg="pink")
        canvas.create_window(screen_width // 2, int(screen_height * 0.18), window=label_welcome)

        button_apply_loan = tk.Button(window, text="Ajukan Pinjaman", font=("Century Gothic", 16), 
                                      command=lambda: apply_loan_screen(window, username, screen_width, screen_height),
                                      bg="white", fg="purple", cursor="hand2")
        canvas.create_window(screen_width // 2, int(screen_height * 0.3), window=button_apply_loan)

        button_view_history = tk.Button(window, text="Lihat Riwayat Pinjaman", font=("Century Gothic", 16),
                                        command=lambda: view_user_loans(window, username, screen_width, screen_height),
                                        bg="white", fg="purple", cursor="hand2")
        canvas.create_window(screen_width // 2, int(screen_height * 0.38), window=button_view_history)

        button_logout = tk.Button(window, text="Logout", font=("Century Gothic", 14), 
                                  command=lambda: login_screen(window, screen_width, screen_height),
                                  bg="white", fg="purple", cursor="hand2")
        canvas.create_window(screen_width // 2, int(screen_height * 0.7), window=button_logout)

    except FileNotFoundError:
        messagebox.showerror("Error", "Gambar tidak ditemukan!")

def apply_loan_screen(window, username, screen_width, screen_height):
    for widget in window.winfo_children():
        widget.destroy()
    try:
        file_path = "4.png"
        background_image = Image.open(file_path)
        resized_image = background_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
        bg_photo = ImageTk.PhotoImage(resized_image)

        canvas = tk.Canvas(window, width=screen_width, height=screen_height)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg_photo, anchor="nw")
        canvas.image = bg_photo

        entry_loan_amount = tk.Entry(window)
        canvas.create_window(screen_width // 2, int(screen_height * 0.22), window=entry_loan_amount)

        duration_var = tk.IntVar(value=3)
        dropdown_duration = tk.OptionMenu(window, duration_var, *durations)
        canvas.create_window(screen_width // 2, int(screen_height * 0.32), window=dropdown_duration)

        mode_var = tk.StringVar(value="fixed")
        radio_fixed = tk.Radiobutton(window, text="Cicilan Tetap", variable=mode_var, value="fixed", 
                                     font=("Century Gothic", 14), bg="white", fg="purple", cursor="hand2")
        canvas.create_window(screen_width // 2, int(screen_height * 0.43), window=radio_fixed)

        radio_decreasing = tk.Radiobutton(window, text="Cicilan Menurun", variable=mode_var, value="decreasing", 
                                          font=("Century Gothic", 14), bg="white", fg="purple", cursor="hand2")
        canvas.create_window(screen_width // 2, int(screen_height * 0.48), window=radio_decreasing)

        radio_flexible = tk.Radiobutton(window, text="Cicilan Fluktuasi BI-Rate", variable=mode_var, value="flexible", 
                                        font=("Century Gothic", 14), bg="white", fg="purple", cursor="hand2")
        canvas.create_window(screen_width // 2, int(screen_height * 0.53), window=radio_flexible)

        def calculate_loan():
            try:
                principal = float(entry_loan_amount.get())
                print(f"Principal: {principal}")
                months = duration_var.get()
                print(f"Months: {months}")
                mode = mode_var.get()
                print(f"Mode: {mode}")
                if mode == "fixed":
                    payments = [calculate_fixed_payment(principal, months, interest_rate)] * months
                elif mode == "decreasing":
                    payments = calculate_decreasing_payment(principal, months, interest_rate)
                elif mode == "flexible":
                    payments = calculate_flexible_payment(principal, months)
                print(f"Payments: {payments}")
                save_installment_data(username, principal, months, payments, mode)
                print_receipt(window, username, principal, months, payments, mode, screen_width, screen_height)
            except ValueError as e:
                print(f"Error: {e}")
                messagebox.showerror("Error", "Masukkan jumlah pinjaman yang valid!")

        button_calculate = tk.Button(window, text="Hitung Cicilan", command=calculate_loan, bg="white", fg="purple", font=("Century Gothic", 14))
        canvas.create_window(screen_width // 2, int(screen_height * 0.6), window=button_calculate)
        
        button_back = tk.Button(window, text="Kembali", command=lambda: user_dashboard(window, username, screen_width, screen_height), 
                                bg="white", fg="purple", font=("Century Gothic", 14))
        canvas.create_window(screen_width // 2, int(screen_height * 0.73), window=button_back)

        button_logout = tk.Button(window, text="Logout", font=("Century Gothic", 15), bg="white", fg="purple",
                                  cursor="hand2", command=lambda: login_screen(window, screen_width, screen_height))
        canvas.create_window(screen_width // 2, int(screen_height * 0.8), window=button_logout)

    except FileNotFoundError:
        messagebox.showerror("Error", "Gambar tidak ditemukan!")

def view_user_loans(window, username, screen_width, screen_height):
    for widget in window.winfo_children():
        widget.destroy()

    try:
        file_path = "9.png"
        background_image = Image.open(file_path)
        resized_image = background_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
        bg_photo = ImageTk.PhotoImage(resized_image)

        canvas = tk.Canvas(window, width=screen_width, height=screen_height)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg_photo, anchor="nw")
        canvas.image = bg_photo

        frame_main = tk.Frame(window, bg="white")
        canvas.create_window(screen_width // 2, screen_height // 2, window=frame_main, width=screen_width * 0.8, height=screen_height * 0.6)

        canvas_scroll = tk.Canvas(frame_main, bg="white")
        canvas_scroll.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(frame_main, orient="vertical", command=canvas_scroll.yview)
        scrollbar.pack(side="right", fill="y")
        canvas_scroll.configure(yscrollcommand=scrollbar.set)

        frame_content = tk.Frame(canvas_scroll, bg="white")
        canvas_scroll.create_window((0, 0), window=frame_content, anchor="nw", width=screen_width * 0.8)

        try:
            with open(installments_file, "r") as f:
                loans = json.load(f)
            user_loans = [loan for loan in loans if loan["username"] == username]

            if user_loans:
                for loan in user_loans:
                    tk.Label(
                        frame_content,
                        text=f"Jumlah: Rp {loan['loan_amount']:,.2f}, Durasi: {loan['loan_duration']} bulan, Mode: {loan['mode']}",
                        font=("Century Gothic", 12),
                        bg="white",
                        anchor="center",
                    ).pack(fill="x", pady=2)

                    tk.Label(frame_content, text="Detail Cicilan Per Bulan:", font=("Century Gothic", 12, "bold"), bg="white", anchor="center").pack(pady=2)
                    for i, payment in enumerate(loan["monthly_payments"], 1):
                        tk.Label(
                            frame_content,
                            text=f"Bulan {i}: Rp {safe_float(payment):,.2f}",
                            font=("Century Gothic", 12),
                            bg="white",
                            anchor="center",
                        ).pack(fill="x")
                    tk.Label(frame_content, text="", bg="white").pack(pady=10) 

            else:
                tk.Label(frame_content, text="Belum ada riwayat pinjaman.", font=("Century Gothic", 14), bg="white").pack(pady=10)

            frame_content.update_idletasks()
            canvas_scroll.configure(scrollregion=canvas_scroll.bbox("all"))
        except FileNotFoundError:
            tk.Label(frame_content, text="Data pinjaman tidak ditemukan.", font=("Century Gothic", 14), bg="white").pack(pady=10)

        back_button = tk.Button(window, text="Kembali", command=lambda: user_dashboard(window, username, screen_width, screen_height),
                                font=("Century Gothic", 14), bg="white", fg="purple", cursor="hand2")
        back_button.place(relx=0.5, rely=0.9, anchor="center")

    except FileNotFoundError:
        messagebox.showerror("Error", "Gambar latar belakang tidak ditemukan!")

def print_receipt(window, username, loan_amount, loan_duration, monthly_payments, mode, screen_width, screen_height):
    try:
        formatted_payments = "\n".join(
            [f"{'Bulan':<10}{str(i+1):>3} : {'Rp':<3} {safe_float(payment):>15,.2f}" for i, payment in enumerate(monthly_payments)])

        # Isi struk
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
            "======================================")

        receipt_window = tk.Toplevel(window)
        receipt_window.title("Pratinjau Struk")
        receipt_window.geometry("400x500")

        text_receipt = tk.Text(receipt_window, wrap=tk.WORD, font=("Courier New", 10))
        text_receipt.insert(tk.END, receipt_text)
        text_receipt.config(state=tk.DISABLED)
        text_receipt.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        button_save = tk.Button(receipt_window,text="Simpan Struk",
            command=lambda: save_as_image(receipt_text, window, screen_width, screen_height),bg="white", fg="purple")
        button_save.pack(pady=10)

        button_close = tk.Button(receipt_window, text="Tutup", command=receipt_window.destroy)
        button_close.pack(pady=5)

    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

def save_as_image(receipt_text, window, screen_width, screen_height):
    try:
        # Menentukan path penyimpanan
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
            title="Simpan Struk Sebagai")
        
        if not file_path:
            return  
        
        try:
            font = ImageFont.truetype("Courier New.ttf", 16)
        except IOError:
            font = ImageFont.load_default() 

        lines = receipt_text.split("\n")
        line_height = 25
        img_width = 250 
        img_height = line_height * len(lines) + 40  
        
        img = Image.new("RGB", (img_width, img_height), color="white")
        draw = ImageDraw.Draw(img)

        y = 10 
        for line in lines:
            if "Bank Santai" in line or "Solusi Anggaran Nyaman" in line or "Tanpa Alasan rIbet" in line:
                line_width = draw.textlength(line, font=font)
                x = (img_width - line_width) // 2  
            else:
                x = 10  
            draw.text((x, y), line, fill="black", font=font)
            y += line_height

        img.save(file_path)
        messagebox.showinfo("Sukses", f"Yayy struk berhasil disimpan")

        show_thank_you_message(window, screen_width, screen_height)

    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan saat menyimpan struk: {e}")

def show_thank_you_message(window, screen_width, screen_height):
    for widget in window.winfo_children():
        widget.destroy()

    try:
        file_path = "6.png" 
        background_image = Image.open(file_path)
        resized_image = background_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
        bg_photo = ImageTk.PhotoImage(resized_image)

        canvas = tk.Canvas(window, width=screen_width, height=screen_height)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg_photo, anchor="nw")
        canvas.image = bg_photo

        button_home = tk.Button(window, text="Home", command=lambda: show_cover(window, screen_width, screen_height),
                                font=("Century Gothic", 15), bg="white", fg="purple", cursor="hand2")
        canvas.create_window(screen_width // 2, int(screen_height * 0.68), window=button_home)

        button_logout = tk.Button(window, text="Logout", command=lambda: login_screen(window, screen_width, screen_height),
                                  font=("Century Gothic", 15), bg="white", fg="purple", cursor="hand2")
        canvas.create_window(screen_width // 2, int(screen_height * 0.75), window=button_logout)

    except FileNotFoundError:
        messagebox.showerror("Error", "Gambar tidak ditemukan!")

def admin_dashboard(window, screen_width, screen_height):
    for widget in window.winfo_children():
        widget.destroy()
    try:
        file_path = "5.png"
        background_image = Image.open(file_path)
        resized_image = background_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
        bg_photo = ImageTk.PhotoImage(resized_image)

        canvas = tk.Canvas(window, width=screen_width, height=screen_height)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg_photo, anchor="nw")
        canvas.image = bg_photo

        listbox_durations = tk.Listbox(window, height=10)
        canvas.create_window(screen_width // 2, int(screen_height * 0.26), window=listbox_durations)
        for dur in durations:
            listbox_durations.insert(tk.END, dur)

        entry_duration = tk.Entry(window) 
        canvas.create_window(screen_width // 2, int(screen_height * 0.38), window=entry_duration)

        def add_duration():
            try:
                new_duration = int(entry_duration.get()) 
                if new_duration not in durations:
                    durations.append(new_duration)
                    durations.sort()
                    listbox_durations.delete(0, tk.END)
                    for dur in durations:
                        listbox_durations.insert(tk.END, dur)
                    save_durations(durations) 
                    messagebox.showinfo("Berhasil", "Durasi berhasil ditambahkan!")
                else:
                    messagebox.showwarning("Gagal", "Durasi sudah ada!")
            except ValueError:
                messagebox.showerror("Error", "Masukkan nilai durasi yang valid!")

        button_add = tk.Button(window, text="Tambah Durasi", font=("Century Gothic", 15), bg="white", fg="purple",
                               cursor="hand2", command=add_duration)
        canvas.create_window(screen_width // 2, int(screen_height * 0.43), window=button_add)

        def delete_duration():
            try:
                selected = listbox_durations.curselection()
                if selected:
                    durations.remove(int(listbox_durations.get(selected)))
                    listbox_durations.delete(selected)
                    save_durations(durations) 
                    messagebox.showinfo("Berhasil", "Durasi berhasil dihapus!")
                else:
                    messagebox.showwarning("Gagal", "Pilih durasi yang ingin dihapus!")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        button_delete = tk.Button(window, text="Hapus Durasi", font=("Century Gothic", 15), bg="white", fg="purple",
                                  cursor="hand2", command=delete_duration)
        canvas.create_window(screen_width // 2, int(screen_height * 0.485), window=button_delete)

        label_interest = tk.Label(window, text=f"Suku Bunga BI-Rate Saat Ini: {bi_rate:.2f}%", font=("Century Gothic", 15),
                                  cursor="hand2", bg="white", fg="purple")
        canvas.create_window(screen_width // 2, int(screen_height * 0.55), window=label_interest)

        entry_interest = tk.Entry(window)
        canvas.create_window(screen_width // 2, int(screen_height * 0.6), window=entry_interest)

        def update_interest():
            global bi_rate
            try:
                new_interest = float(entry_interest.get())
                bi_rate = new_interest
                save_bi_rate(bi_rate) 
                label_interest.config(text=f"Suku Bunga BI-Rate Saat Ini: {bi_rate:.2f}%")
                messagebox.showinfo("Berhasil", f"Suku bunga diperbarui menjadi {bi_rate:.2f}%")
            except ValueError:
                messagebox.showerror("Error", "Masukkan nilai suku bunga yang valid!")

        button_update = tk.Button(window, text="Perbarui Suku Bunga", command=update_interest, cursor="hand2",
                                  bg="white", fg="purple", font=("Century Gothic", 14))
        canvas.create_window(screen_width // 2, int(screen_height * 0.65), window=button_update)
    except FileNotFoundError:
        messagebox.showerror("Error", "Gambar tidak ditemukan!")    

    button_viewloan = tk.Button(window, text="Lihat Semua Pinjaman", font=("Century Gothic", 15), bg="white", fg="purple",
                            cursor="hand2", command=lambda: view_all_loans(window, screen_width, screen_height))
    canvas.create_window(screen_width // 2, int(screen_height * 0.72), window=button_viewloan)

    button_logout = tk.Button(window, text="Logout", font=("Century Gothic", 15), bg="white", fg="purple",
                          cursor="hand2", command=lambda: login_screen(window, screen_width, screen_height))
    canvas.create_window(screen_width // 2, int(screen_height * 0.85), window=button_logout)

def view_all_loans(window, screen_width, screen_height):
    for widget in window.winfo_children():
        widget.destroy()

    try:
        file_path = "7.png" 
        background_image = Image.open(file_path)
        resized_image = background_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
        bg_photo = ImageTk.PhotoImage(resized_image)

        canvas_bg = tk.Canvas(window, width=screen_width, height=screen_height)
        canvas_bg.pack(fill="both", expand=True)
        canvas_bg.create_image(0, 0, image=bg_photo, anchor="nw")
        canvas_bg.image = bg_photo

        frame_main = tk.Frame(window, bg="white")
        frame_main.place(relx=0.5, rely=0.5, anchor="center", width=screen_width * 0.8, height=screen_height * 0.6)

        canvas = tk.Canvas(frame_main, bg="white")
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(frame_main, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        frame_content = tk.Frame(canvas, bg="white")
        canvas.create_window((screen_width * 0.4, 0), window=frame_content, anchor="n")

        try:
            with open(installments_file, "r") as f:
                loans = json.load(f)

            if loans:
                for loan in loans:
                    tk.Label(frame_content, text=f"Username: {loan['username']}", font=("Century Gothic", 12), 
                             bg="white", anchor="center").pack(fill="x", pady=2)
                    tk.Label(frame_content, text=f"Jumlah: Rp {loan['loan_amount']:,.2f}, Durasi: {loan['loan_duration']} bulan, Mode: {loan['mode']}",
                             font=("Century Gothic", 12), bg="white", anchor="center").pack(fill="x", pady=2)
                    tk.Label(frame_content, text="Detail Cicilan Per Bulan:", font=("Century Gothic", 12, "bold"), 
                             bg="white", anchor="center").pack(pady=2)
                    for i, payment in enumerate(loan['monthly_payments'], 1):
                        tk.Label(frame_content, text=f"  Bulan {i}: Rp {payment:,.2f}", font=("Century Gothic", 12), 
                                 bg="white", anchor="center").pack(fill="x")
                    tk.Label(frame_content, text="", bg="white").pack(pady=10)

            else:
                tk.Label(frame_content, text="Tidak ada data pinjaman.", font=("Century Gothic", 14), bg="white").pack(pady=10)

        except FileNotFoundError:
            tk.Label(frame_content, text="File data pinjaman tidak ditemukan.", font=("Century Gothic", 14), bg="white").pack(pady=10)

        def update_canvas(event):
            canvas_width = event.width
            canvas.itemconfig(canvas_window, width=canvas_width)

        canvas_window = canvas.create_window((0, 0), window=frame_content, anchor="n", width=screen_width * 0.8)
        frame_content.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind("<Configure>", update_canvas)

    except FileNotFoundError:
        messagebox.showerror("Error", "Gambar latar belakang tidak ditemukan!")

    back_button = tk.Button(window, text="Kembali", command=lambda: admin_dashboard(window, screen_width, screen_height),
                            font=("Century Gothic", 14), bg="white", fg="purple", cursor="hand2")
    back_button.place(relx=0.5, rely=0.9, anchor="center")

def run_app():
    window = tk.Tk()
    window.title("Aplikasi Peminjaman Cicilan")

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    window.geometry(f"{screen_width}x{screen_height}")
    window.state('zoomed') 

    show_cover(window, screen_width, screen_height)
    window.mainloop()

if __name__ == "__main__":
    run_app()