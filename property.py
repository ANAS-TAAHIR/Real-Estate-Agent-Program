class Property:
    def __init__(self):
        self.square_feet = input("Enter Square Feet: ")
        self.no_of_bedrooms = input(
            "Enter Number of Bedrooms: ")
        self.no_of_bathrooms = input(
            "Enter Number of Bathrooms: ")

    def set_values_p(self):
        self.square_feet = input("Enter Square Feet: ")
        self.no_of_bedrooms = input(
            "Enter Number of Bedrooms: ")
        self.no_of_bathrooms = input(
            "Enter Number of Bathrooms: ")

    def __str__(self):
        return f"=================\nPROPERTY DETAILS\n=================\nSquare Feet {self.square_feet}\nNumber of Bedrooms {self.no_of_bedrooms}\nNumber of Bathrooms {self.no_of_bathrooms}\n"


if __name__ == "__main__":
    p = Property()
    print(p)
