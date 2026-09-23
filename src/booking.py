bookings = []

def book_ticket(movie_id, tickets_count):
    booking = {"id": len(bookings) + 1, "movie_id": movie_id, "tickets": tickets_count}
    bookings.append(booking)
    return booking

def get_user_bookings():
    return bookings

