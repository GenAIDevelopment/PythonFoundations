from ticketing.bus.bus import Bus
from ticketing.movie.theatre import MovieTheatre

if __name__ == "__main__":
    bus = Bus('TSRTC', 'lahari', 'TS09Z1234')
    bus.set_seats(10, 4)
    bus.book_ticket("1_1", 250)

    gokul_theatre = MovieTheatre('Gokul', 'Gokul', 'id12345')
    gokul_theatre.set_seats(20, 20)
    gokul_theatre.book_ticket(2_10, 150)