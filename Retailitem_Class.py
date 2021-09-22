class Retailitem:


    def __init__(self,item_description,units_inventory,price):
        self.__item = item_description
        self.__units_inventory = units_inventory
        self.__price = price 

    def set_description(self,item_description):
        self.__item = item_description

    def set_units(self,units_inventory):
        self.__units_inventory = units_inventory

    def set_price(self,price):
        self.__price = price

    
    def get_description(self):
        return self.__item

    def get_units(self):
        return self.__units_inventory

    def get_price(self):
        return self.__price

    





