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

def calculate_flexible_payment(principal, months, bi_rate):
    monthly_payments = []
    for month in range(1, months + 1):
        interest = principal * (bi_rate / 100)
        monthly_payment = (principal / months) + interest
        monthly_payments.append(monthly_payment)
    return monthly_payments

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
