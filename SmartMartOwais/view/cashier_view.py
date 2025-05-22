# import tkinter as tk
# from tkinter import messagebox
# from model.product_model import ProductModel
# from model.bill_model import BillModel
#
# class CashierView:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Smart Mart - Cashier Panel")
#         self.cart = []
#
#         # Use model classes
#         self.product_model = ProductModel()
#         self.bill_model = BillModel()
#
#         self.products = self.product_model.get_products_by_category()
#
#         self.category_var = tk.StringVar()
#         self.product_var = tk.StringVar()
#         self.quantity_var = tk.StringVar(value='1')  # Default quantity
#
#         self.build_gui()
#
#     def build_gui(self):
#         tk.Label(self.root, text="Category:").pack()
#         self.category_menu = tk.OptionMenu(self.root, self.category_var, *self.products.keys(), command=self.update_products)
#         self.category_menu.pack()
#
#         tk.Label(self.root, text="Product:").pack()
#         self.product_menu = tk.OptionMenu(self.root, self.product_var, "")
#         self.product_menu.pack()
#
#         tk.Label(self.root, text="Quantity:").pack()
#         tk.Entry(self.root, textvariable=self.quantity_var).pack()
#
#         tk.Button(self.root, text="Add to Cart", command=self.add_to_cart).pack()
#
#         self.cart_display = tk.Text(self.root, height=10, width=50)
#         self.cart_display.pack()
#
#         tk.Button(self.root, text="Checkout (Cash)", command=lambda: self.checkout("Cash")).pack()
#         tk.Button(self.root, text="Checkout (Card)", command=lambda: self.checkout("Card")).pack()
#
#     def update_products(self, category):
#         self.product_var.set("")
#         menu = self.product_menu["menu"]
#         menu.delete(0, "end")
#         for item in self.products.get(category, []):
#             menu.add_command(label=item["name"], command=tk._setit(self.product_var, item["name"]))
#
#     def add_to_cart(self):
#         try:
#             category = self.category_var.get()
#             product_name = self.product_var.get()
#             quantity = int(self.quantity_var.get())
#
#             if not category or not product_name:
#                 raise Exception("Please select a product.")
#
#             if quantity <= 0:
#                 raise ValueError("Quantity must be greater than 0.")
#
#             for product in self.products.get(category, []):
#                 if product["name"] == product_name:
#                     self.cart.append({
#                         "name": product_name,
#                         "price": float(product["price"]),
#                         "qty": quantity
#                     })
#                     self.update_cart_display()
#                     break
#         except Exception as e:
#             messagebox.showerror("Error", str(e))
#
#     def update_cart_display(self):
#         self.cart_display.delete("1.0", tk.END)
#         total = 0
#         for item in self.cart:
#             subtotal = item['price'] * item['qty']
#             line = f"{item['name']} x {item['qty']} = Rs. {subtotal:.2f}\n"
#             total += subtotal
#             self.cart_display.insert(tk.END, line)
#         self.cart_display.insert(tk.END, f"\nTotal: Rs. {total:.2f}")
#
#     def checkout(self, method):
#         if not self.cart:
#             messagebox.showwarning("Cart Empty", "No items in cart.")
#             return
#
#         total = sum(item['price'] * item['qty'] for item in self.cart)
#
#         if method == "Card":
#             total *= 0.9  # 10% discount for card payments
#
#         self.bill_model.save_bill(self.cart, total, method)
#         messagebox.showinfo("Payment Received", f"Total Paid ({method}): Rs. {round(total, 2)}")
#
#         self.cart = []
#         self.update_cart_display()
import tkinter as tk
from tkinter import messagebox
from model.product_model import ProductModel
from model.bill_model import BillModel

class CashierView:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Mart - Cashier POS")
        self.root.geometry("1000x600")
        self.root.configure(bg="#ecf0f1")

        self.cart = []
        self.product_model = ProductModel()
        self.bill_model = BillModel()

        self.products = self.product_model.get_products_by_category()

        self.category_var = tk.StringVar()
        self.product_var = tk.StringVar()
        self.quantity_var = tk.StringVar(value='1')

        self.build_gui()

    def build_gui(self):
        # Sidebar
        sidebar = tk.Frame(self.root, bg="#2c3e50", width=200)
        sidebar.pack(side="left", fill="y")

        tk.Label(sidebar, text="Cashier Panel", bg="#2c3e50", fg="white", font=("Helvetica", 16, "bold")).pack(pady=20)

        # Main Panel
        main_panel = tk.Frame(self.root, bg="#ecf0f1")
        main_panel.pack(side="left", fill="both", expand=True, padx=20, pady=20)

        title = tk.Label(main_panel, text="Point of Sale (POS)", font=("Helvetica", 20, "bold"), fg="#2c3e50", bg="#ecf0f1")
        title.grid(row=0, column=0, columnspan=2, pady=10)

        # Dropdowns and Entry Fields
        self.create_label(main_panel, "Select Category", 1)
        self.category_menu = tk.OptionMenu(main_panel, self.category_var, *self.products.keys(), command=self.update_products)
        self.style_option_menu(self.category_menu)
        self.category_menu.grid(row=1, column=1, pady=10, sticky="ew")

        self.create_label(main_panel, "Select Product", 2)
        self.product_menu = tk.OptionMenu(main_panel, self.product_var, "")
        self.style_option_menu(self.product_menu)
        self.product_menu.grid(row=2, column=1, pady=10, sticky="ew")

        self.create_label(main_panel, "Quantity", 3)
        quantity_entry = tk.Entry(main_panel, textvariable=self.quantity_var, font=("Helvetica", 12), bg="white", bd=1, relief="solid")
        quantity_entry.grid(row=3, column=1, pady=10, sticky="ew")

        add_btn = self.create_button(main_panel, "Add to Cart", "#1abc9c", self.add_to_cart)
        add_btn.grid(row=4, column=0, columnspan=2, pady=20, ipadx=10, ipady=5)

        # Cart Display Panel
        cart_frame = tk.Frame(main_panel, bg="white", bd=2, relief="groove")
        cart_frame.grid(row=0, column=2, rowspan=6, padx=20, sticky="nsew")

        tk.Label(cart_frame, text="Cart", font=("Helvetica", 16, "bold"), bg="white", fg="#2c3e50").pack(pady=10)

        self.cart_display = tk.Text(cart_frame, height=20, width=40, font=("Courier New", 10), bg="#f8f9fa")
        self.cart_display.pack(padx=10, pady=5)

        # Checkout Buttons
        checkout_frame = tk.Frame(main_panel, bg="#ecf0f1")
        checkout_frame.grid(row=6, column=0, columnspan=3, pady=20)

        self.create_button(checkout_frame, "Checkout - Cash", "#27ae60", lambda: self.checkout("Cash")).pack(side="left", padx=10, ipadx=10, ipady=5)
        self.create_button(checkout_frame, "Checkout - Card (10% OFF)", "#2980b9", lambda: self.checkout("Card")).pack(side="left", padx=10, ipadx=10, ipady=5)

    def create_label(self, parent, text, row):
        label = tk.Label(parent, text=text, font=("Helvetica", 12), bg="#ecf0f1", anchor="w")
        label.grid(row=row, column=0, sticky="w", padx=5)

    def style_option_menu(self, menu):
        menu.config(font=("Helvetica", 12), bg="white", width=20)

    def create_button(self, parent, text, color, command):
        return tk.Button(
            parent,
            text=text,
            font=("Helvetica", 12, "bold"),
            bg=color,
            fg="white",
            command=command,
            bd=0,
            activebackground=color,
            activeforeground="white"
        )

    def update_products(self, category):
        self.product_var.set("")
        menu = self.product_menu["menu"]
        menu.delete(0, "end")
        for item in self.products.get(category, []):
            menu.add_command(label=item["name"], command=tk._setit(self.product_var, item["name"]))

    def add_to_cart(self):
        try:
            category = self.category_var.get()
            product_name = self.product_var.get()
            quantity = int(self.quantity_var.get())

            if not category or not product_name:
                raise Exception("Please select a product.")

            if quantity <= 0:
                raise ValueError("Quantity must be greater than 0.")

            for product in self.products.get(category, []):
                if product["name"] == product_name:
                    self.cart.append({
                        "name": product_name,
                        "price": float(product["price"]),
                        "qty": quantity
                    })
                    self.update_cart_display()
                    break
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_cart_display(self):
        self.cart_display.delete("1.0", tk.END)
        total = 0
        for item in self.cart:
            subtotal = item['price'] * item['qty']
            total += subtotal
            line = f"{item['name']:<20} x{item['qty']}  Rs.{subtotal:>6.2f}\n"
            self.cart_display.insert(tk.END, line)
        self.cart_display.insert(tk.END, f"\n{'-'*40}\nTOTAL: Rs. {total:.2f}")

    def checkout(self, method):
        if not self.cart:
            messagebox.showwarning("Cart Empty", "No items in cart.")
            return

        total = sum(item['price'] * item['qty'] for item in self.cart)

        if method == "Card":
            total *= 0.9  # 10% discount

        self.bill_model.save_bill(self.cart, total, method)
        messagebox.showinfo("Payment Complete", f"Total Paid with {method}: Rs. {round(total, 2)}")

        self.cart = []
        self.update_cart_display()
