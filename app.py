import tkinter as tk
from tkinter import messagebox

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cart = Cart()

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        if quantity <= product.quantity:
            self.items.append((product, quantity))
            product.quantity -= quantity
            return True
        else:
            return False

    def view_cart(self):
        cart_contents = ""
        for item, quantity in self.items:
            cart_contents += f"{item.name}: {quantity} @ Rp{item.price} each\n"
        return cart_contents
    
    def checkout(self):
        total = sum(item.price * quantity for item, quantity in self.items)
        self.items = []
        return total

class HandCarry:
    def __init__(self, root):
        self.root = root
        self.root.title("HandCarry")
        self.root.geometry("600x600")

        self.users = {}
        self.products = [
            Product("361 AG4 SE", 1900000, 3),
            Product("Wade Flash", 1500000, 4),
            Product("ANTA Kai 1", 2300000, 3),
            Product("Wade Fission 9", 1500000, 3),
            Product("WOW 10", 2700000, 3),
            Product("ANTA KT 9", 2000000, 2)
        ]
        self.current_user = None

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.create_widgets()

    def create_widgets(self):
        self.clear_frame()

        self.title_label = tk.Label(self.frame, text="HandCarry", font=("Arial", 24, "bold"), fg="#2c3e50")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20)

        self.register_button = tk.Button(self.frame, text="Register", command=self.register, bg="#3498db", fg="white", font=("Arial", 12, "bold"))
        self.register_button.grid(row=1, column=0, pady=10, padx=10)

        self.login_button = tk.Button(self.frame, text="Login", command=self.login, bg="#2ecc71", fg="white", font=("Arial", 12, "bold"))
        self.login_button.grid(row=1, column=1, pady=10, padx=10)

    def register(self):
        self.clear_frame()
        self.title_label = tk.Label(self.frame, text="Register", font=("Arial", 24, "bold"), fg="#2c3e50")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20)

        self.username_label = tk.Label(self.frame, text="Username:", font=("Arial", 12))
        self.username_label.grid(row=1, column=0, pady=5)
        self.username_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.username_entry.grid(row=1, column=1, pady=5)

        self.password_label = tk.Label(self.frame, text="Password:", font=("Arial", 12))
        self.password_label.grid(row=2, column=0, pady=5)
        self.password_entry = tk.Entry(self.frame, show="*", font=("Arial", 12))
        self.password_entry.grid(row=2, column=1, pady=5)

        self.register_submit_button = tk.Button(self.frame, text="Register", command=self.register_user, bg="#e67e22", fg="white", font=("Arial", 12, "bold"))
        self.register_submit_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.back_button = tk.Button(self.frame, text="Back", command=self.go_back, bg="#95a5a6", fg="white", font=("Arial", 12, "bold"))
        self.back_button.grid(row=4, column=0, columnspan=2, pady=10)

    def register_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username in self.users:
            messagebox.showerror("Error", "Username already exists.")
        else:
            self.users[username] = User(username, password)
            messagebox.showinfo("Success", "User registered successfully!")
            self.go_back()

    def login(self):
        self.clear_frame()
        self.title_label = tk.Label(self.frame, text="Login", font=("Arial", 24, "bold"), fg="#2c3e50")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20)

        self.username_label = tk.Label(self.frame, text="Username:", font=("Arial", 12))
        self.username_label.grid(row=1, column=0, pady=5)
        self.username_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.username_entry.grid(row=1, column=1, pady=5)

        self.password_label = tk.Label(self.frame, text="Password:", font=("Arial", 12))
        self.password_label.grid(row=2, column=0, pady=5)
        self.password_entry = tk.Entry(self.frame, show="*", font=("Arial", 12))
        self.password_entry.grid(row=2, column=1, pady=5)

        self.login_submit_button = tk.Button(self.frame, text="Login", command=self.login_user, bg="#e67e22", fg="white", font=("Arial", 12, "bold"))
        self.login_submit_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.back_button = tk.Button(self.frame, text="Back", command=self.go_back, bg="#95a5a6", fg="white", font=("Arial", 12, "bold"))
        self.back_button.grid(row=4, column=0, columnspan=2, pady=10)

    def login_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username in self.users and self.users[username].password == password:
            self.current_user = self.users[username]
            messagebox.showinfo("Success", "User logged in successfully!")
            self.show_main_menu()
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def show_main_menu(self):
        self.clear_frame()
        self.title_label = tk.Label(self.frame, text="Main Menu", font=("Arial", 24, "bold"), fg="#2c3e50")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20)

        self.list_products_button = tk.Button(self.frame, text="List Products", command=self.list_products, bg="#3498db", fg="white", font=("Arial", 12, "bold"))
        self.list_products_button.grid(row=1, column=0, pady=10, padx=10)

        self.view_cart_button = tk.Button(self.frame, text="View Cart", command=self.view_cart, bg="#2ecc71", fg="white", font=("Arial", 12, "bold"))
        self.view_cart_button.grid(row=1, column=1, pady=10, padx=10)

        self.checkout_button = tk.Button(self.frame, text="Checkout", command=self.checkout, bg="#e67e22", fg="white", font=("Arial", 12, "bold"))
        self.checkout_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.logout_button = tk.Button(self.frame, text="Logout", command=self.logout, bg="#e74c3c", fg="white", font=("Arial", 12, "bold"))
        self.logout_button.grid(row=3, column=0, columnspan=2, pady=10)

    def list_products(self):
        self.clear_frame()
        self.title_label = tk.Label(self.frame, text="Products", font=("Arial", 24, "bold"), fg="#2c3e50")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20)

        for i, product in enumerate(self.products):
            product_label = tk.Label(self.frame, text=f"{product.name}: Rp{product.price} (Stock: {product.quantity})", font=("Arial", 12))
            product_label.grid(row=i+1, column=1, padx=10, pady=10)

        self.product_name_label = tk.Label(self.frame, text="Product name:", font=("Arial", 12))
        self.product_name_label.grid(row=len(self.products)+1, column=0, pady=5)
        self.product_name_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.product_name_entry.grid(row=len(self.products)+1, column=1, pady=5)

        self.quantity_label = tk.Label(self.frame, text="Quantity:", font=("Arial", 12))
        self.quantity_label.grid(row=len(self.products)+2, column=0, pady=5)
        self.quantity_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.quantity_entry.grid(row=len(self.products)+2, column=1, pady=5)

        self.add_to_cart_button = tk.Button(self.frame, text="Add to Cart", command=self.add_to_cart, bg="#e67e22", fg="white", font=("Arial", 12, "bold"))
        self.add_to_cart_button.grid(row=len(self.products)+3, column=0, columnspan=2, pady=10)

        self.back_button = tk.Button(self.frame, text="Back", command=self.show_main_menu, bg="#95a5a6", fg="white", font=("Arial", 12, "bold"))
        self.back_button.grid(row=len(self.products)+4, column=0, columnspan=2, pady=10)

    def add_to_cart(self):
        product_name = self.product_name_entry.get()
        try:
            quantity = int(self.quantity_entry.get())
            if quantity <= 0:
                messagebox.showerror("Error", "Please enter a valid quantity.")
                return
            for product in self.products:
                if product.name == product_name:
                    if self.current_user.cart.add_product(product, quantity):
                        messagebox.showinfo("Success", f"{quantity} of {product.name} added to the cart.")
                    else:
                        messagebox.showerror("Error", f"Not enough {product.name} in stock.")
                    return
            messagebox.showerror("Error", "Product not found.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid quantity.")

    def view_cart(self):
        self.clear_frame()
        self.title_label = tk.Label(self.frame, text="Your Cart", font=("Arial", 24, "bold"), fg="#2c3e50")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20)

        cart_contents = self.current_user.cart.view_cart()
        self.cart_label = tk.Label(self.frame, text=cart_contents, font=("Arial", 12))
        self.cart_label.grid(row=1, column=0, columnspan=2, pady=10)

        self.back_button = tk.Button(self.frame, text="Back", command=self.show_main_menu, bg="#95a5a6", fg="white", font=("Arial", 12, "bold"))
        self.back_button.grid(row=2, column=0, columnspan=2, pady=10)

    def checkout(self):
        total = self.current_user.cart.checkout()
        messagebox.showinfo("Checkout", f"Total amount: Rp{total}. Thank you for your purchase!")
        self.show_main_menu()

    def logout(self):
        self.current_user = None
        messagebox.showinfo("Logout", "Logged out successfully.")
        self.go_back()

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def go_back(self):
        self.clear_frame()
        self.create_widgets()

if __name__ == "__main__":
    root = tk.Tk()
    app = HandCarry(root)
    root.mainloop()
