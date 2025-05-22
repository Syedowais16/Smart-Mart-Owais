from view.login_view import LoginView
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Smart Mart Management System")
    app = LoginView(root)
    root.mainloop()


# Selected: MVC (Model-View-Controller)
# 🎯 Justification:
# Clear separation of concerns:
#
# Model = Data Logic (ProductModel, BillModel)
#
# View = GUI (AdminView, CashierView)
#
# Controller = Business Logic (add/delete product, checkout)
#
# Easy to test and debug each component independently
#
# Faster development for GUI-based apps like Tkinter
#
# Avoids unnecessary complexity of N-Tier for small-to-medium apps