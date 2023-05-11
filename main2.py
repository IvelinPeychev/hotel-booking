import pandas
# import Abstract Base Class
from abc import ABC, abstractmethod


# dtype=str will treat each numbers in the file as strings not as integers
# as above may be problematic, we can select the exact column with dtype={'id':str}
df = pandas.read_csv('hotels.csv', dtype={'id': str})


class Hotel:
    # Class variable
    watermark = 'The Real Estate Company'

    def __init__(self, hotel_id):
        # Instance variable
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

    # When we need a method related to the class but nof to the instance
    @classmethod
    def get_hotel_count(cls, data):
        return len(data)

    # Magic methods are the python build in methods, they can be overwritten
    # Magic method are placed at the end of the class
    # other keyword is given for the second variable
    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
            return True


class Ticket(ABC):
    # Every child class MUST implement the generate method
    @abstractmethod
    def generate(self):
        pass

class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        # Passing the name of the Hotel class as we create a hotel instance and pass it
        self.hotel = hotel_object

    def generate(self):
        # By passing the hotel object to the Reservation instance, we can access the Hotel name property
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Guest name: {self.the_customer_name}
        Hotel name: {self.hotel.name}
        """
        return content

    # property, usually the method name is not a verb but a variable
    # We don't place the code under __init__ method as it will not be organized.
    # The property method is called like a variable, not like a method with () brackets.
    # We use the property when the value that the property returns looks like
    # more of the instance value, but we need some processing on it.
    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name

    # like a function, so it is not has references to the class (cls) or the instance (self)
    @staticmethod
    def convert(amount):
        return amount * 1.2


class DigitalTicket(Ticket):
    # Not a good practice to override the parent method - better to create an Abstract class from which the normal
    # classes will inherit
    def generate(self):
        return 'Hello, this is your digital ticket'

    def download(self):
        pass

# hotel1 = Hotel(hotel_id='188')
# hotel2 = Hotel(hotel_id='134')
#
# print(hotel1.name)
# print(hotel2.name)
#
# print(hotel1.watermark)
# print(hotel2.watermark)
#
# print(Hotel.watermark)
#
# print(Hotel.get_hotel_count(data=df))
# print(hotel1.get_hotel_count(data=df))
#
# ticket = Reservation(customer_name='john smith ', hotel_object=hotel1)
# print(ticket.the_customer_name)
# print(ticket.generate())
#
# converted = Reservation.convert(10)
# print(converted)