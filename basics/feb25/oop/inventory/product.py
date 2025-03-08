"""This module has classes around product"""


class Product:
    """This class defines a Product
    members:
      id
      name
      price
      quantity
    methods:
      describe
      purchase
      sale
    """

    def __init__(self, id, name, price, quantity):
        """_summary_

        Args:
            id (int): product id
            name (str): name of the product
            price (float): price of the product
            quantity (int): quanity available
        """
        # The below values are members
        # representation or private
        self.__id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def sale(self, count):
        """This method defines the sale of product and updates
        the quantity

        Args:
            count (int): number of items sold
        """
        self.quantity -= count

    def purchase(self, count):
        """This methods defines the purchase and updates the quanity

        Args:
            count (int): number of items purchased
        """
        self.quantity += count
    
    def get_product_id(self):
        """Get the product id
        """
        return self.__id
    
    def set_product_id(self, id):
        self.__id = id
