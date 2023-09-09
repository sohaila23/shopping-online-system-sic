import tkinter as tk
from tkinter import ttk, messagebox
from classes import *


class RegisterPage:
    def __init__(self, root, user_data, login_page):
        self.name_entry = None
        self.phone_entry = None
        self.email_entry = None
        self.gender_combobox = None
        self.governorate_entry = None
        self.password_entry = None
        self.age_combobox = None
        self.national_id_entry = None
        self.root = root
        self.user_data = user_data
        self.login_page = login_page
        self.create_register_page()

    def create_register_page(self):
        self.clear_screen()

        register_label = tk.Label(self.root, text="Register")
        register_label.pack(padx=5, pady=5)

        self.name_entry = self.create_input_field("Name:")
        self.phone_entry = self.create_input_field("Phone Number:")
        self.email_entry = self.create_input_field("Email:")

        genders = ["Male", "Female"]
        label_3 = tk.Label(self.root, text="Gender:")
        label_3.pack(padx=5, pady=5)
        self.gender_combobox = ttk.Combobox(self.root, values=genders)
        self.gender_combobox.pack(padx=5, pady=5)

        self.governorate_entry = self.create_input_field("Governorate:")
        self.password_entry = self.create_input_field("Password:", show="*")

        age_options = [str(i) for i in range(1, 101)]
        self.age_combobox = tk.Label(self.root, text="Age:")
        self.age_combobox.pack(padx=5, pady=5)
        self.age_combobox = ttk.Combobox(self.root, values=age_options)
        self.age_combobox.pack(padx=5, pady=5)
        self.age_combobox.set(age_options[0])

        self.national_id_entry = self.create_input_field("National ID:")

        register_button = tk.Button(self.root, text="Register", command=self.save_user_data)
        register_button.pack(padx=5, pady=5)

        back_button = tk.Button(self.root, text="Back to Login", command=self.switch_to_login_page)
        back_button.pack(padx=5, pady=5)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_input_field(self, label_text, show=None):
        label = tk.Label(self.root, text=label_text, font=('Arial', 15))
        label.pack(padx=5, pady=5)
        entry = tk.Entry(self.root, show=show)
        entry.pack(padx=5, pady=5)
        return entry

    def save_user_data(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        gender = self.gender_combobox.get()
        governorate = self.governorate_entry.get()
        password = self.password_entry.get()
        age = self.age_combobox.get()
        national_id = self.national_id_entry.get()

        user_info = User(name, phone, email, gender, governorate, password, age, national_id)

        for existing_user in self.user_data:
            if existing_user.email == email:
                messagebox.showerror("Registration Error", "User with this email already exists!")
                return

        self.user_data.append(user_info)
        print("List of registered users:")
        for user in self.user_data:
            print(user.__dict__)

        messagebox.showinfo("Registration Success", "User data has been registered successfully!")
        self.switch_to_login_page()

    def switch_to_login_page(self):
        self.clear_screen()
        self.login_page()
