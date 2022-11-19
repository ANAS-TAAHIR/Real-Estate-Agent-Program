from house_purchase import HousePurchase
from house_rental import HouseRental
from appartment_rental import AppartmentRental
from appartment_purchase import AppartmentPurchase
import functions


class Agent:
    class_dict = {('house', 'rental'): HouseRental, ('house', 'purchase'): HousePurchase,
                  ('apartment', 'rental'): AppartmentRental, ('apartment', 'purchase'): AppartmentPurchase}

    def __init__(self):
        self.properties_list = []

    def add_property(self):
        property_type = functions.get_valid_input(
            'What type of property? ', ('house', 'apartment')).lower()
        payment_type = functions.get_valid_input(
            'What payment type? ', ('purchase', 'rental')).lower()
        item = None
        if property_type == 'house' and payment_type == 'purchase':
            item = HousePurchase()
        elif property_type == 'house' and payment_type == 'rental':
            item = HouseRental()
        if property_type == 'apartment' and payment_type == 'purchase':
            item = AppartmentPurchase()
        elif property_type == 'apartment' and payment_type == 'rental':
            item = AppartmentRental()
        self.properties_list.append(item)

    def show_all_properties(self):
        for i in self.properties_list:
            print(i)

    def show_match_property(self):
        property_type = input("Enter Property type: ")
        payment_type = input("Enter Payment type: ")
        obj = Agent.class_dict[(property_type, payment_type)]
        for i in self.properties_list:
            if type(i) == obj:
                print(i)

    def modify_property(self):
        property_no = int(input("Enter Property Number: "))
        if 0 > property_no or property_no >= len(self.properties_list):
            print("Invalid Property")
        else:
            self.properties_list[property_no].set_values()
