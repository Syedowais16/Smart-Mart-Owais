class AdminModel:
    def __init__(self, file_path='data/admin.txt'):
        self.file_path = file_path

    def validate_admin(self, username, password):
        try:
            with open(self.file_path, 'r') as f:
                for line in f:
                    u, p = line.strip().split(',')
                    if u == username and p == password:
                        return True
        except FileNotFoundError:
            print("Admin file not found.")
        return False
