# import tkinter as tk
# from tkinter import messagebox
# from controller.controller import Controller
# from view.admin_view import AdminView
# from view.cashier_view import CashierView
#
# class LoginView:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("500x400")
#         self.controller = Controller()
#
#         bg = tk.PhotoImage(file='assets/background.png')
#         bg_label = tk.Label(root, image=bg)
#         bg_label.image = bg
#         bg_label.place(relwidth=1, relheight=1)
#
#         self.frame = tk.Frame(root, bg='white', bd=2)
#         self.frame.place(relx=0.3, rely=0.3, relwidth=0.4, relheight=0.4)
#
#         self.username = tk.Entry(self.frame)
#         self.username.pack(pady=5)
#         self.password = tk.Entry(self.frame, show='*')
#         self.password.pack(pady=5)
#
#         tk.Button(self.frame, text="Login as Admin", command=self.login_admin).pack(pady=5)
#         tk.Button(self.frame, text="Login as Cashier", command=self.login_cashier).pack(pady=5)
#
#     def login_admin(self):
#         u = self.username.get()
#         p = self.password.get()
#         if self.controller.login_admin(u, p):
#             self.frame.destroy()
#             AdminView(self.root)
#         else:
#             messagebox.showerror("Error", "Invalid Admin Credentials")
#
#     def login_cashier(self):
#         u = self.username.get()
#         p = self.password.get()
#         if self.controller.login_cashier(u, p):
#             self.frame.destroy()
#             CashierView(self.root)
#         else:
#             messagebox.showerror("Error", "Invalid Cashier Credentials")

import tkinter as tk
from tkinter import messagebox
from controller.controller import Controller
from view.admin_view import AdminView
from view.cashier_view import CashierView

class LoginView:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Mart Login")
        self.root.geometry("700x500")
        self.root.configure(bg="#f0f2f5")
        self.root.resizable(False, False)

        self.controller = Controller()

        # Background image
        try:
            self.bg_img = tk.PhotoImage(file='assets/background.png')
            bg_label = tk.Label(self.root, image=self.bg_img)
            bg_label.place(relwidth=1, relheight=1)
        except Exception:
            self.root.configure(bg="#dff9fb")  # fallback color if image not found

        # Main frame with shadow
        self.frame = tk.Frame(self.root, bg='white', bd=0, highlightthickness=4, highlightbackground="#1abc9c")
        self.frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=300)

        tk.Label(self.frame, text="Welcome to Smart Mart", font=("Helvetica", 20, "bold"), bg="white", fg="#1abc9c").pack(pady=20)

        # Username
        tk.Label(self.frame, text="Username", font=("Helvetica", 12), bg="white", anchor="w").pack(fill='x', padx=40)
        self.username = tk.Entry(self.frame, font=("Helvetica", 12), bd=1, relief="solid")
        self.username.pack(padx=40, pady=(0, 10), fill='x')

        # Password
        tk.Label(self.frame, text="Password", font=("Helvetica", 12), bg="white", anchor="w").pack(fill='x', padx=40)
        self.password = tk.Entry(self.frame, font=("Helvetica", 12), show='*', bd=1, relief="solid")
        self.password.pack(padx=40, pady=(0, 20), fill='x')

        # Buttons
        login_admin_btn = tk.Button(
            self.frame, text="Login as Admin", font=("Helvetica", 12, "bold"),
            bg="#1abc9c", fg="white", bd=0, height=2, command=self.login_admin
        )
        login_admin_btn.pack(padx=40, pady=(0, 10), fill='x')

        login_cashier_btn = tk.Button(
            self.frame, text="Login as Cashier", font=("Helvetica", 12, "bold"),
            bg="#3498db", fg="white", bd=0, height=2, command=self.login_cashier
        )
        login_cashier_btn.pack(padx=40, fill='x')

    def login_admin(self):
        u = self.username.get().strip()
        p = self.password.get().strip()
        if self.controller.login_admin(u, p):
            self.frame.destroy()
            AdminView(self.root)
        else:
            messagebox.showerror("Error", "Invalid Admin Credentials")

    def login_cashier(self):
        u = self.username.get().strip()
        p = self.password.get().strip()
        if self.controller.login_cashier(u, p):
            self.frame.destroy()
            CashierView(self.root)
        else:
            messagebox.showerror("Error", "Invalid Cashier Credentials")
