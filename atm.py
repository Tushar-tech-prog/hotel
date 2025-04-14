import tkinter as tk
from tkinter import messagebox, scrolledtext
from datetime import datetime

# Global variables for user data and balance
user_data = {"name": "", "fname": "", "acc": "", "pin": ""}
account_balance = 0  # Starting balance
transactions = []  # Stores transaction history

# Function to handle registration
def submit_registration():
    if name.get() and fname.get() and acc.get():
        user_data["name"] = name.get()
        user_data["fname"] = fname.get()
        user_data["acc"] = acc.get()
        setup_pin()  # Proceed to PIN setup
    else:
        messagebox.showerror("Error", "Please fill out all fields!")

# Function for PIN setup
def setup_pin():
    pin_window = tk.Toplevel()
    pin_window.title("Set PIN")
    pin_window.configure(bg="#d1e7dd")
    
    tk.Label(pin_window, text="Set Up Your PIN", font=("Helvetica", 16, "bold"), bg="#51b39e", fg="white", pady=10).grid(row=0, column=0, columnspan=2)
    tk.Label(pin_window, text="Enter New PIN:", font=("Arial", 12), bg="#d1e7dd").grid(row=1, column=0, pady=10)
    new_pin_entry = tk.Entry(pin_window, font=("Arial", 12), show="*", relief="flat", bg="#f8f9fa")
    new_pin_entry.grid(row=1, column=1, pady=10, padx=10)
    
    tk.Label(pin_window, text="Confirm PIN:", font=("Arial", 12), bg="#d1e7dd").grid(row=2, column=0, pady=10)
    confirm_pin_entry = tk.Entry(pin_window, font=("Arial", 12), show="*", relief="flat", bg="#f8f9fa")
    confirm_pin_entry.grid(row=2, column=1, pady=10, padx=10)

    def submit_pin():
        new_pin = new_pin_entry.get()
        confirm_pin = confirm_pin_entry.get()
        if new_pin == confirm_pin and new_pin:
            user_data["pin"] = new_pin
            messagebox.showinfo("PIN Setup Complete", "Your PIN has been set successfully!")
            pin_window.destroy()
            welcome_message()  # Show welcome message
        else:
            messagebox.showerror("Error", "PINs do not match or are invalid!")
    
    tk.Button(pin_window, text="Submit", command=submit_pin, font=("Arial", 12), bg="#51b39e", fg="white", relief="flat").grid(row=3, column=1, pady=10)

# Function for welcome message and PIN verification
def welcome_message():
    messagebox.showinfo("Welcome", f"Welcome, {user_data['name']}! Please verify your PIN to access the ATM menu.")
    verify_pin()  # Prompt user to verify PIN

def verify_pin():
    verify_window = tk.Toplevel()
    verify_window.title("Verify PIN")
    verify_window.configure(bg="#fff3cd")
    
    tk.Label(verify_window, text="Enter Your PIN", font=("Helvetica", 16, "bold"), bg="#ffc107", fg="black", pady=10).grid(row=0, column=0, columnspan=2)
    tk.Label(verify_window, text="PIN:", font=("Arial", 12), bg="#fff3cd").grid(row=1, column=0, pady=10)
    pin_entry = tk.Entry(verify_window, font=("Arial", 12), show="*", relief="flat", bg="#f8f9fa")
    pin_entry.grid(row=1, column=1, pady=10)

    def check_pin():
        entered_pin = pin_entry.get()
        if entered_pin == user_data["pin"]:
            messagebox.showinfo("Access Granted", "PIN verified successfully! Accessing ATM menu.")
            verify_window.destroy()
            open_atm_menu()  # Open ATM menu if PIN is correct
        else:
            messagebox.showerror("Access Denied", "Incorrect PIN. Please try again.")

    tk.Button(verify_window, text="Submit", command=check_pin, font=("Arial", 12), bg="#ffc107", fg="black", relief="flat").grid(row=2, column=1, pady=10)

# Function to open ATM menu
def open_atm_menu():
    atm_menu = tk.Toplevel()
    atm_menu.title("ATM Menu")
    atm_menu.configure(bg="#e3f2fd")

    # Logout icon in top-right corner
    logout_icon = tk.Button(atm_menu, text="Logout", command=lambda: logout(atm_menu), font=("Arial", 10), bg="#d32f2f", fg="white", relief="flat")
    logout_icon.place(relx=0.9, rely=0.02)

    def deposit():
        global account_balance
        amount = amount_entry.get()
        if amount.isdigit():
            account_balance += int(amount)
            transactions.append((datetime.now().strftime("%Y-%m-%d %H:%M:%S"), f"Deposited ₹{amount}"))
            messagebox.showinfo("Deposit Successful", f"Deposited ₹{amount}. Current Balance: ₹{account_balance}")
        else:
            messagebox.showerror("Error", "Invalid amount.")
        amount_entry.delete(0, tk.END)

    def view_balance():
        messagebox.showinfo("Account Balance", f"Current Balance: ₹{account_balance}")

    def view_history():
        history_window = tk.Toplevel()
        history_window.title("Transaction History")
        history_window.configure(bg="#fff3e0")
        history_text = scrolledtext.ScrolledText(history_window, width=50, height=15, font=("Arial", 10), bg="#ffe0b2")
        history_text.pack(pady=10)
        for timestamp, transaction in transactions:
            history_text.insert(tk.END, f"{timestamp} - {transaction}\n")
        history_text.config(state="disabled")

    def request_loan():
        loan_window = tk.Toplevel()
        loan_window.title("Loan Application")
        loan_window.configure(bg="#fbe9e7")

        tk.Label(loan_window, text="Loan Application Form", font=("Helvetica", 16, "bold"), bg="#ff7043", fg="white", pady=10).grid(row=0, column=0, columnspan=2, sticky="ew")
        tk.Label(loan_window, text="Name:", font=("Arial", 12), bg="#fbe9e7").grid(row=1, column=0, pady=5)
        name_entry = tk.Entry(loan_window, font=("Arial", 12), relief="flat", bg="#ffffff")
        name_entry.insert(0, user_data["name"])
        name_entry.grid(row=1, column=1, pady=5)

        tk.Label(loan_window, text="Father's Name:", font=("Arial", 12), bg="#fbe9e7").grid(row=2, column=0, pady=5)
        fname_entry = tk.Entry(loan_window, font=("Arial", 12), relief="flat", bg="#ffffff")
        fname_entry.insert(0, user_data["fname"])
        fname_entry.grid(row=2, column=1, pady=5)

        tk.Label(loan_window, text="Reason for Loan:", font=("Arial", 12), bg="#fbe9e7").grid(row=3, column=0, pady=5)
        reason_entry = tk.Entry(loan_window, font=("Arial", 12), relief="flat", bg="#ffffff")
        reason_entry.grid(row=3, column=1, pady=5)

        tk.Label(loan_window, text="Loan Amount:", font=("Arial", 12), bg="#fbe9e7").grid(row=4, column=0, pady=5)
        loan_amount_entry = tk.Entry(loan_window, font=("Arial", 12), relief="flat", bg="#ffffff")
        loan_amount_entry.grid(row=4, column=1, pady=5)

        def submit_loan():
            if name_entry.get() and fname_entry.get() and reason_entry.get() and loan_amount_entry.get().isdigit():
                transactions.append((datetime.now().strftime("%Y-%m-%d %H:%M:%S"), f"Loan Applied: ₹{loan_amount_entry.get()} for {reason_entry.get()}"))
                messagebox.showinfo("Loan Submitted", "Your loan application has been submitted successfully!")
                loan_window.destroy()
            else:
                messagebox.showerror("Error", "Please complete all fields correctly.")

        tk.Button(loan_window, text="Submit", command=submit_loan, font=("Arial", 12), bg="#ff7043", fg="white", relief="flat").grid(row=5, column=1, pady=10)

    tk.Label(atm_menu, text="ATM Menu", font=("Helvetica", 18, "bold"), bg="#2196f3", fg="white", pady=10).grid(row=0, column=0, columnspan=2, sticky="ew")
    tk.Label(atm_menu, text="Enter amount:", font=("Arial", 12), bg="#e3f2fd").grid(row=1, column=0, pady=5, padx=10)
    amount_entry = tk.Entry(atm_menu, font=("Arial", 12), relief="flat", bg="#f8f9fa")
    amount_entry.grid(row=1, column=1, pady=5)

    # Buttons for ATM Features
    btn_style = {"font": ("Arial", 12), "relief": "flat", "bg": "#90caf9", "fg": "white", "activebackground": "#1976d2"}
    tk.Button(atm_menu, text="Deposit", command=deposit, **btn_style).grid(row=2, column=0, pady=10, padx=10)
    tk.Button(atm_menu, text="View Balance", command=view_balance, **btn_style).grid(row=2, column=1, pady=10, padx=10)
    tk.Button(atm_menu, text="Transaction History", command=view_history, **btn_style).grid(row=3, column=0, pady=10, padx=10)
    tk.Button(atm_menu, text="Request Loan", command=request_loan, **btn_style).grid(row=3, column=1, pady=10, padx=10)

# Function to log out and return to registration
def logout(window):
    messagebox.showinfo("Logout", "You have been logged out.")
    window.destroy()
    registration_window.deiconify()

# Registration Window
registration_window = tk.Tk()
registration_window.title("Registration")
registration_window.configure(bg="#ffebee")

# Input fields for registration
name = tk.StringVar()
fname = tk.StringVar()
acc = tk.StringVar()

tk.Label(registration_window, text="Registration Form", font=("Helvetica", 18, "bold"), bg="#d32f2f", fg="white", pady=10).grid(row=0, column=0, columnspan=2, sticky="ew")
tk.Label(registration_window, text="Name:", font=("Arial", 12), bg="#ffebee").grid(row=1, column=0, pady=5)
tk.Entry(registration_window, textvariable=name, font=("Arial", 12), relief="flat", bg="#f8f9fa").grid(row=1, column=1, pady=5)

tk.Label(registration_window, text="Father's Name:", font=("Arial", 12), bg="#ffebee").grid(row=2, column=0, pady=5)
tk.Entry(registration_window, textvariable=fname, font=("Arial", 12), relief="flat", bg="#f8f9fa").grid(row=2, column=1, pady=5)

tk.Label(registration_window, text="Account Number:", font=("Arial", 12), bg="#ffebee").grid(row=3, column=0, pady=5)
tk.Entry(registration_window, textvariable=acc, font=("Arial", 12), relief="flat", bg="#f8f9fa").grid(row=3, column=1, pady=5)

tk.Button(registration_window, text="Submit", command=submit_registration, font=("Arial", 12), bg="#d32f2f", fg="white", relief="flat").grid(row=4, column=1, pady=10)

# Main loop to run the application
registration_window.mainloop()
