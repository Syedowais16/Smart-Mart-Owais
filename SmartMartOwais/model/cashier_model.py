class CashierModel:
    def __init__(self, file_path='data/cashiers.txt'):
        self.file_path = file_path

    def get_cashiers(self):
        try:
            with open(self.file_path, 'r') as f:
                return [line.strip().split(',') for line in f]
        except FileNotFoundError:
            return []

    def validate_cashier(self, username, password):
        return any(u == username and p == password for u, p in self.get_cashiers())
