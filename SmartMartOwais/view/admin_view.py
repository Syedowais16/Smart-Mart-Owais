# import tkinter as tk
# from controller.controller import Controller
#
# class AdminView:
#     def __init__(self, root):
#         self.root = root
#         self.controller = Controller()
#
#         tk.Label(root, text="Admin Panel", font=("Arial", 18)).pack(pady=10)
#
#         self.category = tk.Entry(root)
#         self.category.insert(0, "Category")
#         self.category.pack()
#
#         self.product = tk.Entry(root)
#         self.product.insert(0, "Product Name")
#         self.product.pack()
#
#         self.price = tk.Entry(root)
#         self.price.insert(0, "Price")
#         self.price.pack()
#
#         tk.Button(root, text="Add Product", command=self.add_product).pack()
#         tk.Button(root, text="Delete Product", command=self.delete_product).pack()
#
#     def add_product(self):
#         c = self.category.get()
#         n = self.product.get()
#         p = self.price.get()
#         try:
#             price = float(p)
#             self.controller.add_product(c, n, price)
#         except ValueError:
#             print("Invalid price.")
#
#     def delete_product(self):
#         name = self.product.get()
#         self.controller.delete_product(name)
import tkinter as tk
from tkinter import messagebox
from controller.controller import Controller

class AdminView:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Mart - Admin Panel")
        self.root.geometry("800x500")
        self.root.configure(bg="#ecf0f1")
        self.controller = Controller()

        # Sidebar panel
        self.sidebar = tk.Frame(self.root, bg="#2c3e50", width=200)
        self.sidebar.pack(side="left", fill="y")

        tk.Label(self.sidebar, text="Admin Panel", font=("Helvetica", 16, "bold"), fg="white", bg="#2c3e50", pady=20).pack()

        # Main content panel
        self.content = tk.Frame(self.root, bg="white")
        self.content.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        tk.Label(self.content, text="Manage Products", font=("Helvetica", 18, "bold"), bg="white", fg="#2c3e50").pack(pady=10)

        self.category = self.create_entry("Category")
        self.product = self.create_entry("Product Name")
        self.price = self.create_entry("Price")

        self.add_btn = self.create_button("Add Product", "#1abc9c", self.add_product)
        self.del_btn = self.create_button("Delete Product", "#e74c3c", self.delete_product)

    def create_entry(self, placeholder):
        frame = tk.Frame(self.content, bg="white")
        frame.pack(pady=10, fill="x", padx=100)

        label = tk.Label(frame, text=placeholder, font=("Helvetica", 12), bg="white", anchor="w")
        label.pack(fill="x")

        entry = tk.Entry(frame, font=("Helvetica", 12), bd=1, relief="solid", bg="#f8f9fa")
        entry.pack(fill="x", pady=5)
        return entry

    def create_button(self, text, color, command):
        btn = tk.Button(
            self.content,
            text=text,
            font=("Helvetica", 12, "bold"),
            bg=color,
            fg="white",
            bd=0,
            padx=10,
            pady=10,
            command=command,
            activebackground=color,
            activeforeground="white",
        )
        btn.pack(pady=10, fill="x", padx=100)
        return btn

    def add_product(self):
        c = self.category.get().strip()
        n = self.product.get().strip()
        p = self.price.get().strip()

        if not c or not n or not p:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            price = float(p)
            self.controller.add_product(c, n, price)
            messagebox.showinfo("Success", f"{n} added successfully.")
            self.clear_fields()
        except ValueError:
            messagebox.showerror("Invalid Input", "Price must be a valid number.")

    def delete_product(self):
        n = self.product.get().strip()
        if not n:
            messagebox.showwarning("Warning", "Please enter a product name to delete.")
            return

        success = self.controller.delete_product(n)
        if success:
            messagebox.showinfo("Deleted", f"{n} deleted successfully.")
            self.clear_fields()
        else:
            messagebox.showerror("Not Found", f"Product '{n}' not found.")

    def clear_fields(self):
        self.category.delete(0, tk.END)
        self.product.delete(0, tk.END)
        self.price.delete(0, tk.END)
