from purchase import Purchase
from house import House


class HousePurchase(House, Purchase):
    def __init__(self):
        House.__init__(self)
        Purchase.__init__(self)

    def set_values(self):
        House.set_values(self)
        Purchase.set_values(self)

    def __str__(self):
        return House.__str__(self) + Purchase.__str__(self)
