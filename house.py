from property import Property
import functions


class House(Property):
    valid_garage = ("attached", "detached", "no")
    valid_fence = ("yes", "no")

    def __init__(self):
        Property.__init__(self)
        self.garage = functions.get_valid_input("Garage ", House.valid_garage)
        self.fence = functions.get_valid_input("Fenced ", House.valid_fence)
        self.stories = input("Number of stories: ")

    def set_values(self):
        super().set_values_p()
        self.garage = functions.get_valid_input("Garage ", House.valid_garage)
        self.fence = functions.get_valid_input("Fenced ", House.valid_fence)
        self.stories = input("Number of stories: ")

    def __str__(self):
        return Property.__str__(self)+f"=================\nHOUSE DETAILS\n=================\nNumber of stories: {self.stories}\nGarage: {self.garage}\nFenced: {self.fence}\n"


if __name__ == "__main__":
    p = House()
    print(p)
