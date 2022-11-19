from purchase import Purchase
from apprtment import Appartment


class AppartmentPurchase(Appartment, Purchase):
    def __init__(self):
        Appartment.__init__(self)
        Purchase.__init__(self)

    def set_values(self):
        Appartment.set_values(self)
        Purchase.set_values(self)

    def __str__(self):
        return Appartment.__str__(self) + Purchase.__str__(self)
