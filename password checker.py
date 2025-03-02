import random
import string
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = any(char in string.punctuation for char in password)
    common_passwords = ["password", "12345678", "qwweerty", "abc12mk3", "password1"]
    if len(password) < 8:
        return "length insufficient" 
    
    if password in common_passwords:
        return "Very Weak (Common Password)"
    
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])
    
    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Medium"
    else:
        return "Weak"

def generate_strong_password(length=12):
    if length < 8:
        messagebox.showerror("Error", "Password length should be at least 8 characters for security.")
        return None
    
    all_chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(all_chars) for _ in range(length))

def check_password():
    password = entry.get()
    strength = check_password_strength(password)
    messagebox.showinfo("Password Strength", f"Password: {password}\nStrength: {strength}")

def generate_password():
    new_password = generate_strong_password()
    if new_password:
        entry.delete(0, tk.END)
        entry.insert(0, new_password)

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")

tk.Label(root, text="Enter Password:").pack(pady=5)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

tk.Button(root, text="Check Strength", command=check_password).pack(pady=5)
tk.Button(root, text="Generate Strong Password", command=generate_password).pack(pady=5)

root.mainloop()