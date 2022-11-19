from rental import Renatal
from apprtment import Appartment


class AppartmentRental(Appartment, Renatal):
    def __init__(self):
        Appartment.__init__(self)
        Renatal.__init__(self)

    def set_values(self):
        Appartment.set_values()
        Renatal.set_values()

    def __str__(self):
        return Appartment.__str__(self) + Renatal.__str__(self)
