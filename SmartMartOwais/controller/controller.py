from model.admin_model import AdminModel
from model.cashier_model import CashierModel
from model.product_model import ProductModel

class Controller:
    def __init__(self):
        self.admin_model = AdminModel()
        self.cashier_model = CashierModel()
        self.product_model = ProductModel()

    def login_admin(self, username, password):
        return self.admin_model.validate_admin(username, password)

    def login_cashier(self, username, password):
        return self.cashier_model.validate_cashier(username, password)

    def get_products(self):
        return self.product_model.get_products()

    def add_product(self, category, name, price):
        self.product_model.add_product(category, name, price)

    def delete_product(self, name):
        self.product_model.delete_product(name)
