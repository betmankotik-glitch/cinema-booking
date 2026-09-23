bookings = []

def book_ticket(movie_id, tickets_count):
    booking = {"id": len(bookings) + 1, "movie_id": movie_id, "tickets": tickets_count}
    bookings.append(booking)
    return booking

def get_user_bookings():
    return bookings

def cancel_booking(booking_id):
    global bookings
    bookings = [b for b in bookings if b["id"] != booking_id]
    return True

def calculate_discount(price, percent):
    return price * (1 - percent / 100)


