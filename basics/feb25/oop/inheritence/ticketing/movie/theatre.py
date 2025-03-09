from ticketing.base.bookable import Bookable

class MovieTheatre(Bookable):
    """This represents a Movie Ticke

    Args:
        Bookable (_type_): _description_
    """
    
    # overriding
    def book_ticket(self, seat_number, price):
        print("This is movie ticket")
        return super().book_ticket(seat_number, price)
    
