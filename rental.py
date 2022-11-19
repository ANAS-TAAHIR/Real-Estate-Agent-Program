import functions


class Renatal:
    is_furnished = ("yes", "no")

    def __init__(self):
        self.furnished = functions.get_valid_input(
            "Is Furnished", Renatal.is_furnished)
        self.rent = input("Enter Rent: ")
        self.utilities = input("Enter Utilities: ")

    def set_values(self):
        self.furnished = functions.get_valid_input(
            "Furnished", Renatal.is_furnished)
        if self.furnished == 'yes':
            self.furnished = "YES"
        else:
            self.furnished = "NO"
        self.rent = input("Enter Rent: ")
        self.utilities = input("Enter Utilities: ")

    def __str__(self):
        return f"=================\nRENTAL DETAILS\n=================\nFurnished: {self.furnished}\nRent: {self.rent}\nUtilities {self.utilities}\n"
