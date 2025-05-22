import os

class ProductModel:
    def __init__(self, file_path='data/products.txt'):
        self.file_path = file_path

    def get_products_by_category(self):
        """
        Returns a dictionary like:
        {
            "Beverages": [{"name": "Coke", "price": 60}, {"name": "Pepsi", "price": 55}],
            "Snacks": [{"name": "Chips", "price": 30}]
        }
        """
        products = {}
        if not os.path.exists(self.file_path):
            return products

        with open(self.file_path, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    category, name, price = parts
                    if category not in products:
                        products[category] = []
                    products[category].append({
                        'name': name,
                        'price': float(price)
                    })
        return products

    def add_product(self, category, name, price):
        """
        Adds a new product in format: Category,Name,Price
        """
        with open(self.file_path, 'a') as f:
            f.write(f"{category},{name},{price}\n")

    def update_product(self, old_name, new_name, new_price):
        """
        Updates a product's name and price
        """
        lines = []
        updated = False
        with open(self.file_path, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    category, name, price = parts
                    if name == old_name:
                        lines.append(f"{category},{new_name},{new_price}\n")
                        updated = True
                    else:
                        lines.append(line)
        if updated:
            with open(self.file_path, 'w') as f:
                f.writelines(lines)

    def delete_product(self, name_to_delete):
        """
        Deletes a product by name
        """
        lines = []
        deleted = False
        with open(self.file_path, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    category, name, price = parts
                    if name != name_to_delete:
                        lines.append(line)
                    else:
                        deleted = True
        if deleted:
            with open(self.file_path, 'w') as f:
                f.writelines(lines)
