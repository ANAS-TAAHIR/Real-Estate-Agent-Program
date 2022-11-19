from property import Property
import functions


class Appartment(Property):
    valid_laundries = ("coin", "ensuite", "none")
    valid_balcony = ("yes", "no", "solarium")

    def __init__(self):
        super().__init__()
        self.laundries = functions.get_valid_input(
            "Laundary: ", Appartment.valid_laundries)
        self.balcony = functions.get_valid_input(
            "Balcony: ", Appartment.valid_balcony)

    def set_values(self):
        super().set_values_p()
        self.laundries = functions.get_valid_input(
            "Lundary: ", Appartment.valid_laundries)
        self.balcony = functions.get_valid_input(
            "Balcony: ", Appartment.valid_balcony)

    def __str__(self):
        return super().__str__()+f"=================\nAPPARTMENT DETAILS\n=================\nLaundary: {self.laundries}\nBalcony: {self.balcony}\n"
