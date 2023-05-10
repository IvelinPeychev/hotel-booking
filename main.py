import pandas

# dtype=str will treat each numbers in the file as strings not as integers
# as above may be problematic, we can select the exact column with dtype={'id':str}
df = pandas.read_csv('hotels.csv', dtype={'id': str})

# Removing the class as there is no methods for it
# class User:


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df['id'] == self.hotel_id, 'available'] = 'no'
        # Index=False so python will not add another index column
        df.to_csv('hotels.csv', index=False)

    def view(self):
        pass

    def available(self):
        """ Check if the hotel is available"""
        # Using pandas to check the available column in hotels.csv
        availability = df.loc[df['id'] == self.hotel_id, 'available'].squeeze()
        if availability == 'yes':
            return True
        else:
            return False


class Reservation:
    def __init__(self, customer_name, hotel_object):
        pass

    def generate(self):
        pass


# The logic
print(df)
hotel_id = input('Enter the id of the hotel: ')
hotel = Hotel(hotel_id)

if hotel.available():
    hotel.book()
    name = input('Enter your name: ')
    reservation_ticket = Reservation(name, hotel)
    print(reservation_ticket.generate())
else:
    print('Hotel is not free')