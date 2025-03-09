from .seat import Seat

class Bookable:
    """This is a parent class for where booking seats in involved
    """
    def __init__(self, operator, name, registration_number):
        """This is initializer for the bus

        Args:
            operator (str): bus operator like APSRTC, TSRTC, Orange
            name (str): vehicle number
            registration_number (str): registration number
        """
        self.operator = operator
        self.name = name
        self.registration_number = registration_number
        self.seats = dict()

    def set_seats(self, rows,columns):
        """This creates the default seat structure

        Args:
            count (_type_): _description_
            rows (_type_): _description_
            columns (_type_): _description_
        """
        for row_index in range(1,rows+1):
            for col_index in range(1, columns+1):
                seat = Seat(
                    id=f"{row_index}_{col_index}"                  
                )
                self.seats[seat.get_seat_number()] = seat
    
    def book_ticket(self, seat_number, price):
        """_summary_

        Args:
            seat_number (_type_): _description_
            price (_type_): _description_
        """
        self.seats.get(seat_number).book(price)
