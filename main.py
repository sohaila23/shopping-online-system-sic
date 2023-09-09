import tkinter as tk
from tkinter import messagebox
from classes import *
from RegisterPage import RegisterPage


class OnlineShoppingSystem:
    def __init__(self, root):
        self.entry_search = None
        self.email_entry = None
        self.password_entry = None
        self.root = root
        self.user_data = []
        self.shopping_cart = ShoppingCart()
        self.login_page()
        self.categories = []
        self.cart_items = []

        electronics = Category("electronics")
        electronics.add_item(Item("Laptop", 800, "BrandA", "2023"))
        electronics.add_item(Item("Phone", 500, "BrandB", "2023"))
        self.categories.append(electronics)

        home_appliances = Category("home appliances")
        home_appliances.add_item(Item("Washing Machine", 600, "BrandX", "2023"))
        home_appliances.add_item(Item("Refrigerator", 700, "BrandY", "2023"))
        self.categories.append(home_appliances)
        self.login_page()

        books = Category("books")
        books.add_item(Item("Wonder", 150, "brand b", "2000"))
        books.add_item(Item("Harry Potter and the Sorcerer's Stone", 300, 'brand a', "2010"))
        self.categories.append(books)

        sports = Category("sports")
        sports.add_item(Item("skate board", 600, "brand s", "2023"))
        sports.add_item(Item("dumbbells", 1000, "brand a", "2020"))
        self.categories.append(sports)

        fashion = Category("fashion")
        fashion.add_item(Item("dress", 800, "max", "2023"))
        fashion.add_item(Item("heels", 700, "max", "2023"))
        self.categories.append(fashion)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def login_page(self):
        self.clear_screen()
        email_label = tk.Label(self.root, text="Email:", font=('Arial', 15))
        email_label.pack(padx=10, pady=10)

        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack(padx=10, pady=10)

        password_label = tk.Label(self.root, text="Password:", font=('Arial', 15))
        password_label.pack(padx=10, pady=10)

        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(padx=10, pady=10)

        login_button = tk.Button(self.root, text="Login", command=self.login)
        login_button.pack(padx=10, pady=10)

        register_button = tk.Button(self.root, text="Register", command=self.open_register_page)
        register_button.pack(padx=10, pady=10)

    def open_register_page(self):
        RegisterPage(self.root, self.user_data, self.login_page)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        is_valid_user = self.validate_user(email, password)

        if is_valid_user:
            messagebox.showinfo("Login Successful", "You are logged in as a user.")
            self.show_home_page_user()

        elif email == "admin" and password == "123":
            messagebox.showinfo("Admin Login", "You are logged in as an admin.")
            self.show_home_page_admin()
        else:
            messagebox.showerror("Login Error", "Invalid email or password")

    def create_home_page(self):
        pass

    def validate_user(self, email, password):
        for existing_user in self.user_data:
            if existing_user.email == email and existing_user.password == password:
                return True
        return False

    def show_home_page_admin(self):
        self.clear_screen()
        admin_label = tk.Label(self.root, text="Admin")
        admin_label.pack(padx=5, pady=5)
        self.root.title("Admin Page")

        button_cart = tk.Button(self.root, text="View Cart", command=self.create_cart_page)
        button_cart.pack(padx=10, pady=10)
        button_logout = tk.Button(self.root, text="Logout", command=self.logout)
        button_logout.pack(padx=10, pady=10)

        button_add_item = tk.Button(self.root, text="Add New Item", command=self.create_add_item_page)
        button_add_item.pack(padx=10, pady=10)

        button_update_item = tk.Button(self.root, text="Update Item", command=self.create_update_item_page)
        button_update_item.pack(padx=10, pady=10)

        button_apply_discount = tk.Button(self.root, text="Apply Discounts", command=self.create_discounts_page)
        button_apply_discount.pack(padx=10, pady=10)

        for category in self.categories:
            button = tk.Button(self.root, text=category.name,
                               command=lambda cat=category.name: self.create_category_page_admin(cat))
            button.pack(padx=10, pady=10)

        button_back = tk.Button(self.root, text="Back", command=self.show_home_page_admin)
        button_back.pack(padx=10, pady=10)

    def create_add_item_page(self):
        self.clear_screen()
        add_item_label = tk.Label(self.root, text="Add New Item")
        add_item_label.pack(padx=5, pady=5)
        self.root.title("Add New Item")

        name_label = tk.Label(self.root, text="Item Name:")
        name_label.pack(padx=5, pady=5)
        name_entry = tk.Entry(self.root)
        name_entry.pack(padx=5, pady=5)

        price_label = tk.Label(self.root, text="Item Price:")
        price_label.pack(padx=5, pady=5)
        price_entry = tk.Entry(self.root)
        price_entry.pack(padx=5, pady=5)

        brand_label = tk.Label(self.root, text="Item Brand:")
        brand_label.pack(padx=5, pady=5)
        brand_entry = tk.Entry(self.root)
        brand_entry.pack(padx=5, pady=5)

        year_label = tk.Label(self.root, text="Item Year:")
        year_label.pack(padx=5, pady=5)
        year_entry = tk.Entry(self.root)
        year_entry.pack(padx=5, pady=5)

        save_button = tk.Button(self.root, text="Save Item", command=lambda: self.save_new_item(name_entry.get(),
                                                                                                price_entry.get(),

                                                                                                brand_entry.get(),
                                                                                                year_entry.get()))
        save_button.pack(padx=10, pady=10)


        button_back = tk.Button(self.root, text="Back", command=self.show_home_page_admin)
        button_back.pack(padx=10, pady=10)



    def save_new_item(self, name, price, brand, year):
        category_name = "electronics"
        new_item = Item(name, int(price), brand, year)
        for category in self.categories:
            if category.name == category_name:
                category.add_item(new_item)
                break
        messagebox.showinfo("Data Saved", "User data has been saved.")

    def create_update_item_page(self):
        self.clear_screen()
        update_item_label = tk.Label(self.root, text="Update Item")
        update_item_label.pack(padx=5, pady=5)
        self.root.title("Update Item")

        item_name_label = tk.Label(self.root, text="Item Name to Update:")
        item_name_label.pack(padx=5, pady=5)
        item_name_entry = tk.Entry(self.root)
        item_name_entry.pack(padx=5, pady=5)

        search_button = tk.Button(self.root, text="Search",
                                  command=lambda: self.search_item_to_update(item_name_entry.get()))
        search_button.pack(padx=10, pady=10)

        button_back = tk.Button(self.root, text="Back", command=self.show_home_page_admin)
        button_back.pack(padx=10, pady=10)


    def search_item_to_update(self, item_name):
        category_name = "electronics"
        for category in self.categories:
            if category.name == category_name:
                item = category.get_item_by_name(item_name)
                if item:
                    self.display_update_item_page(item)
                    break

    def display_update_item_page(self, item):
        self.clear_screen()
        update_item_label = tk.Label(self.root, text="Update Item")
        update_item_label.pack(padx=5, pady=5)
        self.root.title("Update Item")

        name_label = tk.Label(self.root, text="Item Name:")
        name_label.pack(padx=5, pady=5)
        name_entry = tk.Entry(self.root)
        name_entry.insert(0, item.name)
        name_entry.pack(padx=5, pady=5)

        price_label = tk.Label(self.root, text="Item Price:")
        price_label.pack(padx=5, pady=5)
        price_entry = tk.Entry(self.root)
        price_entry.insert(0, item.price)
        price_entry.pack(padx=5, pady=5)

        brand_label = tk.Label(self.root, text="Item Brand:")
        brand_label.pack(padx=5, pady=5)
        brand_entry = tk.Entry(self.root)
        brand_entry.insert(0, item.brand)
        brand_entry.pack(padx=5, pady=5)

        year_label = tk.Label(self.root, text="Item Year:")
        year_label.pack(padx=5, pady=5)
        year_entry = tk.Entry(self.root)
        year_entry.insert(0, item.year)
        year_entry.pack(padx=5, pady=5)

        save_button = tk.Button(self.root, text="Save Changes",
                                command=lambda: self.save_updated_item(item, name_entry.get(),
                                                                       price_entry.get(), brand_entry.get(),
                                                                       year_entry.get()))
        save_button.pack(padx=10, pady=10)

        button_back = tk.Button(self.root, text="Back", command=self.show_home_page_admin)
        button_back.pack(padx=10, pady=10)

    def save_updated_item(self, item, new_name, new_price, new_brand, new_year):
        item.name = new_name
        item.price = int(new_price)
        item.brand = new_brand
        item.year = new_year

        self.show_home_page_admin()

    def create_discounts_page(self):
        self.clear_screen()
        discounts_label = tk.Label(self.root, text="Apply Discounts")
        discounts_label.pack(padx=5, pady=5)
        self.root.title("Apply Discounts")

        search_label = tk.Label(self.root, text="Item Name to Apply Discount:")
        search_label.pack(padx=5, pady=5)
        search_entry = tk.Entry(self.root)
        search_entry.pack(padx=5, pady=5)

        search_button = tk.Button(self.root, text="Search",
                                  command=lambda: self.search_item_to_apply_discount(search_entry.get()))
        search_button.pack(padx=10, pady=10)

        discount_label = tk.Label(self.root, text="Discount Percentage:")
        discount_label.pack(padx=5, pady=5)
        discount_entry = tk.Entry(self.root)
        discount_entry.pack(padx=5, pady=5)

        apply_discount_button = tk.Button(self.root, text="Apply Discount",
                                          command=lambda: self.apply_discount(discount_entry.get()))
        apply_discount_button.pack(padx=10, pady=10)

        button_back = tk.Button(self.root, text="Back to Admin Page", command=self.show_home_page_admin)
        button_back.pack(padx=10, pady=10)

    def search_item_to_apply_discount(self, item_name):
        category_name = "electronics"
        for category in self.categories:
            if category.name == category_name:
                item = category.get_item_by_name(item_name)
                if item:
                    self.display_apply_discount_page(item)
                    break

    def display_apply_discount_page(self, item):
        self.clear_screen()
        apply_discount_label = tk.Label(self.root, text=f"Apply Discount to {item.name}")
        apply_discount_label.pack(padx=5, pady=5)
        self.root.title("Apply Discounts")

        name_label = tk.Label(self.root, text=f"Item Name: {item.name}")
        name_label.pack(padx=5, pady=5)

        price_label = tk.Label(self.root, text=f"Item Price: {item.price}")
        price_label.pack(padx=5, pady=5)

        discount_label = tk.Label(self.root, text="New Discount Percentage:")
        discount_label.pack(padx=5, pady=5)
        new_discount_entry = tk.Entry(self.root)
        new_discount_entry.pack(padx=5, pady=5)

        save_discount_button = tk.Button(self.root, text="Save Discount",
                                         command=lambda: self.save_discount(item, new_discount_entry.get()))
        save_discount_button.pack(padx=10, pady=10)

        button_back = tk.Button(self.root, text="Back to Discounts Page", command=self.create_discounts_page)
        button_back.pack(padx=10, pady=10)

    def save_discount(self, item, new_discount_percentage):
        item.apply_discount(float(new_discount_percentage))

        self.create_discounts_page()

    def apply_discount(self, discount_percentage):
        category_name = "electronics"
        for category in self.categories:
            if category.name == category_name:
                for item in category.items:
                    item.apply_discount(float(discount_percentage))
                break

    def create_category_page(self, category_name):
        self.clear_screen()
        category = None

        for cat in self.categories:
            if cat.name == category_name:
                category = cat
                break
        if category:
            label1 = tk.Label(self.root, text=category.name)
            label1.pack(padx=10, pady=10)

            button_search = tk.Button(self.root, text="Search", command=lambda: self.search_item(category))
            button_search.pack(padx=10, pady=10)

            self.entry_search = tk.Entry(self.root)
            self.entry_search.pack(padx=10, pady=10)

            button_sort_asc = tk.Button(self.root, text="Sort by Price (Asc)",
                                        command=lambda: self.sort_items(category, True))
            button_sort_asc.pack(padx=10, pady=10)

            button_sort_desc = tk.Button(self.root, text="Sort by Price (Desc)",
                                         command=lambda: self.sort_items(category, False))
            button_sort_desc.pack(padx=10, pady=10)

            for item in category.items:
                tk.Label(self.root, text=f"Name: {item.name} | Price: {item.price} | brand:{item.brand}"
                                         f" | year_model:{item.year}").pack()
                tk.Button(self.root, text="Add to Cart", command=lambda i=item: self.add_to_cart(i)).pack()

            button_back = tk.Button(self.root, text="Back", command=self.show_home_page_admin)
            button_back.pack(padx=10, pady=10)

    def create_category_page_admin(self, category_name):
        self.clear_screen()
        category = None

        for cat in self.categories:
            if cat.name == category_name:
                category = cat
                break
        if category:
            label1 = tk.Label(self.root, text=category.name)
            label1.pack(padx=10, pady=10)

            button_search = tk.Button(self.root, text="Search", command=lambda: self.search_item(category))
            button_search.pack(padx=10, pady=10)

            self.entry_search = tk.Entry(self.root)
            self.entry_search.pack(padx=10, pady=10)

            button_sort_asc = tk.Button(self.root, text="Sort by Price (Asc)",
                                        command=lambda: self.sort_items(category, True))
            button_sort_asc.pack(padx=10, pady=10)

            button_sort_desc = tk.Button(self.root, text="Sort by Price (Desc)",
                                         command=lambda: self.sort_items(category, False))
            button_sort_desc.pack(padx=10, pady=10)

            for item in category.items:
                tk.Label(self.root, text=f"Name: {item.name} | Price: {item.price} |brand:{item.brand}"
                                         f" |year_model:{item.year}").pack()
                tk.Button(self.root, text="Add to Cart", command=lambda i=item: self.add_to_cart(i)).pack()

            button_back = tk.Button(self.root, text="Back", command=self.show_home_page_admin)
            button_back.pack(padx=10, pady=10)

    def add_to_cart(self, item):
        self.cart_items.append(item)
        messagebox.showinfo("Item Added", f"{item.name} added to the cart.")

    def sort_items(self, category, ascending=True):
        category.sort_items_by_price(ascending)
        self.create_category_page(category.name)

    def search_item(self, category):
        search_term = self.entry_search.get()
        found_items = []

        for item in category.items:
            if search_term.lower() in item.name.lower():
                found_items.append(item)

        self.clear_screen()
        label1 = tk.Label(self.root, text=category.name)
        label1.pack(padx=10, pady=10)

        for item in found_items:
            tk.Label(self.root, text=f"Name: {item.name} | Price: {item.price} |brand:{item.brand}"
                                     f" |year_model:{item.year}").pack()
            tk.Button(self.root, text="Add to Cart", command=lambda i=item: self.add_to_cart(i)).pack()

        button_back = tk.Button(self.root, text="Back", command=self.show_home_page_admin)
        button_back.pack(padx=10, pady=10)

    def create_cart_page(self):
        self.clear_screen()

        label_cart = tk.Label(self.root, text="Cart")
        label_cart.pack()

        total_price = 0

        for item in self.cart_items:
            total_price += item.price
            label_item = tk.Label(self.root, text=f"Name: {item.name}, Price: {item.price},")
            label_item.pack()

        total_price_label = tk.Label(self.root, text=f"Total Price: {total_price}")
        total_price_label.pack()

        button_clear_cart = tk.Button(self.root, text="Clear Cart", command=self.clear_cart)
        button_clear_cart.pack()

        button_go_back = tk.Button(self.root, text="Go Back", command=self.show_home_page_admin)
        button_go_back.pack()

    def logout(self):
        self.create_login_page()

    def create_login_page(self):
        self.login_page()

    def clear_cart(self):
        self.cart_items.clear()
        self.shopping_cart.clear()
        self.create_cart_page()

    # ---------------------------------------------------------

    def show_home_page_user(self):
        self.clear_screen()
        home_label = tk.Label(self.root, text="Home Page")
        home_label.pack()
        self.root.title("User Page")

        button_cart = tk.Button(self.root, text="View Cart", command=self.create_cart_page)
        button_cart.pack(padx=10, pady=10)
        button_logout = tk.Button(self.root, text="Logout", command=self.logout)
        button_logout.pack(padx=10, pady=10)

        button1 = tk.Button(self.root, text="electronics",
                            command=lambda cat="electronics": self.create_category_page(cat))
        button1.pack(padx=10, pady=10)
        button2 = tk.Button(self.root, text="home appliances",
                            command=lambda cat="home appliances": self.create_category_page(cat))
        button2.pack(padx=10, pady=10)
        button3 = tk.Button(self.root, text="books", command=lambda cat="books": self.create_category_page(cat))
        button3.pack(padx=10, pady=10)
        button4 = tk.Button(self.root, text="sports", command=lambda cat="sports": self.create_category_page(cat))
        button4.pack(padx=10, pady=10)
        button5 = tk.Button(self.root, text="fashion", command=lambda cat="fashion": self.create_category_page(cat))
        button5.pack(padx=10, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = OnlineShoppingSystem(root)
    root.title("Online Shopping System")
    root.geometry("800x500")
    root.mainloop()
