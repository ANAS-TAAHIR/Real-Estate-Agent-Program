class Purchase:
    def __init__(self):
        self.price = input("Enter price: ")
        self.taxes = input("Enter tax: ")

    def set_values(self):
        self.price = input("Enter price: ")
        self.taxes = input("Enter tax: ")

    def __str__(self):
        return f'=================\nPURCHASE DETAILS\n=================\nPrice {self.price}\nTax {self.taxes}'
