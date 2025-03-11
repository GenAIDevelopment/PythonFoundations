"""This module will have restaurant related classes
"""
from restaurant.food import Menu

class Restaurant:
    """This represents the restaurant
    """
    def __init__(self, name):
        """Initializer

        Args:
            name (str): name
        """
        self.name = name
        self.address = None
        self.menu = Menu()
    
    def update_address(self, address):
        """Updates the address

        Args:
            address (_type_): _description_
        """
        self.address = address

    def add_food_items(self, item):
        """Add food items

        Args:
            item (_type_): _description_
        """
        self.menu.add_item(item)