from rental import Renatal
from house import House


class HouseRental(House, Renatal):
    def __init__(self):
        House.__init__(self)
        Renatal.__init__(self)

    def set_values(self):
        House.set_values(self)
        Renatal.set_values(self)

    def __str__(self):
        return House.__str__(self) + Renatal.__str__(self)
