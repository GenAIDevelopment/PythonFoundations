"""This module will have seat information
"""

class Seat:
    """This represents a seat in any booking system

    This could represent a movie theatre seat, bus seat or train berth
    """
    def __init__(self, id, price=0.0, category='Standard', is_empty=True):
        """This is initializer for the seat

        Args:
            id (_type_): _description_
            price (_type_): _description_
            category (_type_): _description_
            is_empty (bool): _description_
        """
        self.__id = id
        self.price = price
        self.category = category
        self.__is_empty = is_empty

    def book(self, price):
        """This method books a seat
        """
        self.__is_empty = False
        self.price = price

    def get_seat_number(self):
        return self.__id