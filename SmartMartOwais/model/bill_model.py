import os
from datetime import datetime

class BillModel:
    def __init__(self, file_path='data/bills.txt'):
        self.file_path = file_path

    def save_bill(self, cart_items, total_amount, payment_method):
        """
        cart_items = [
            {'name': 'Coke', 'price': 60.0, 'qty': 2},
            {'name': 'Chips', 'price': 30.0, 'qty': 1}
        ]
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.file_path, 'a') as f:
            f.write(f"--- Bill @ {timestamp} ---\n")
            for item in cart_items:
                name = item['name']
                qty = item['qty']
                price = item['price']
                subtotal = price * qty
                f.write(f"{name} x {qty} = Rs. {subtotal:.2f}\n")
            f.write(f"Payment Method: {payment_method}\n")
            f.write(f"Total: Rs. {total_amount:.2f}\n\n")

    def get_all_bills(self):
        """
        Returns the entire content of the bill file as string.
        """
        if not os.path.exists(self.file_path):
            return ""
        with open(self.file_path, 'r') as f:
            return f.read()
