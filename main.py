import pandas

# dtype=str will treat each numbers in the file as strings not as integers
# as above may be problematic, we can select the exact column with dtype={'id':str}
df = pandas.read_csv('hotels.csv', dtype={'id': str})

# Removing the class as there is no methods for it
# class User:


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        # we are using the hotel_id to extract the hotel name from the csv file and not need to pass it during the
        # instance creation

        self.name = df.loc[df['id'] == self.hotel_id, 'name'].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df['id'] == self.hotel_id, 'available'] = 'no'
        # Write the new value in the csv file, Index=False so python will not add another index column
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
        self.customer_name = customer_name
        # Passing the name of the Hotel class as we create a hotel instance and pass it
        self.hotel = hotel_object

    def generate(self):
        # By passing the hotel object to the Reservation instance, we can access the Hotel name property
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Guest name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content


# The logic
print(df)
hotel_id = input('Enter the id of the hotel: ')
hotel = Hotel(hotel_id)

if hotel.available():
    hotel.book()
    name = input('Enter your name: ')
    reservation_ticket = Reservation(customer_name=name, hotel_object=hotel)
    print(reservation_ticket.generate())
else:
    print('Hotel is not free')
