import pandas

df = pandas.read_csv('hotels.csv')

# Removing the class as there is no methods for it
# class User:

class Hotel:
    def __init__(self, id):
        pass

    def book(self):
        pass

    def view(self):
        pass

    def available(self):
        pass


class Reservation:
    def __init__(self, customer_name, hotel_object):
        pass

    def generate(self):
        pass

# The logic
print(df)
id = input('Enter the id of the hotel: ')
hotel = Hotel(id)
if hotel.available():
    hotel.book()
    name = input('Enter your name:')
    reservation_ticket = Reservation(name, hotel)
    print(reservation_ticket.generate())
else:
    print('Hotel is not free')