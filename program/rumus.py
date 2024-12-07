import json

# Logika Perhitungan
def calculate_fixed_payment(principal, months, interest_rate):
    interest = principal * (interest_rate / 100)
    total_payment = principal + interest
    monthly_payment = total_payment / months
    return monthly_payment

def calculate_decreasing_payment(principal, months, interest_rate):
    monthly_payments = []
    for month in range(1, months + 1):
        interest = (principal - (principal / months) * (month - 1)) * (interest_rate / 100)
        monthly_payment = (principal / months) + interest
        monthly_payments.append(monthly_payment)
    return monthly_payments

def calculate_flexible_payment(principal, months):
    bi_rate = load_bi_rate()  # Ambil BI Rate terbaru dari file
    monthly_payments = []
    for month in range(1, months + 1):
        interest = principal * (bi_rate / 100)
        monthly_payment = (principal / months) + interest
        monthly_payments.append(monthly_payment)
    return monthly_payments

def save_bi_rate(rate):
    with open('bi_rate.json', 'w') as f:
        json.dump({"bi_rate": rate}, f)

def load_bi_rate():
    try:
        with open('bi_rate.json', 'r') as f:
            return json.load(f).get("bi_rate", 6)  # Default BI Rate adalah 6 jika file tidak ada
    except FileNotFoundError:
        return 6
    
def save_durations(durations):
    with open('durations.json', 'w') as f:
        json.dump(durations, f)

def load_durations():
    try:
        with open('durations.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return [3, 6, 9, 12, 24, 36]  # Default durasi jika file tidak ada


# Fungsi Pengelolaan Data
def save_user_data(username, password):
    users = load_users()
    users[username] = {"password": password}
    with open('users.json', 'w') as f:
        json.dump(users, f)

def load_users():
    try:
        with open('users.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def load_admin():
    try:
        with open('admin.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        save_admin_data()
        return load_admin()

def save_admin_data():
    admin_data = {"username": "admin", "password": "admin123"}
    with open('admin.json', 'w') as f:
        json.dump(admin_data, f)

# Fungsi Utilitas
def safe_float(value):
    try:
        if isinstance(value, str):
            value = value.replace("Rp", "").replace(",", "").strip()
        return float(value)
    except ValueError:
        return 0.0
    
def save_installment_data(username, loan_amount, loan_duration, monthly_payments, mode):
    try:
        # Struktur data yang akan disimpan
        data = {
            "username": username,
            "loan_amount": loan_amount,
            "loan_duration": loan_duration,
            "monthly_payments": monthly_payments,
            "mode": mode,
        }

        # Muat data lama dari file JSON jika ada
        try:
            with open('installments.json', 'r') as f:
                installments = json.load(f)
        except FileNotFoundError:
            installments = []

        # Tambahkan data baru
        installments.append(data)

        # Simpan data ke file JSON
        with open('installments.json', 'w') as f:
            json.dump(installments, f, indent=4)

    except Exception as e:
        print(f"Error saving installment data: {e}")
