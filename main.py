import pandas

# dtype=str will treat each numbers in the file as strings not as integers
# as above may be problematic, we can select the exact column with dtype={'id':str}
df = pandas.read_csv('hotels.csv', dtype={'id': str})

# dtype=str will treat each as a string, based on the value logic
# convert to dict as it is easier to check in CreditCadr.validate()
df_cards = pandas.read_csv('cards.csv', dtype=str).to_dict(orient='records')
df_cards_security = pandas.read_csv('card_security.csv', dtype=str)


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


class SpaHotel(Hotel):
    def book_spa_hotel(self):
        pass


class SpaReservation(Reservation):
    def generate(self):
        # By passing the hotel object to the Reservation instance, we can access the Hotel name property
        content = f"""
        Thank you for your reservation!
        Here are your SPA booking data:
        Guest name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content


class CreditCard:
    def __init__(self,number):
        self.number = number


    def validate(self, expiration, holder, cvc):
        card_data = {'number': self.number, 'expiration': expiration, 'holder': holder, 'cvc': cvc}
        if card_data in df_cards:
            return True
        # No need to return False as it will be automatic None if the IF statement is not valid


class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_cards_security.loc[df_cards_security['number'] == self.number, 'password'].squeeze()
        if password == given_password:
            return True


# The executable logic
print(df)
hotel_id = input('Enter the id of the hotel: ')
hotel = SpaHotel(hotel_id)

if hotel.available():
    # We are not using input() to get the data below for simplicity
    credit_card = SecureCreditCard(number='1234567890123456')
    if credit_card.validate(expiration='12/26', holder='JOHN SMITH', cvc='123'):
        if credit_card.authenticate('mypass'):
            hotel.book()
            name = input('Enter your name: ')
            reservation_ticket = Reservation(customer_name=name, hotel_object=hotel)
            print(reservation_ticket.generate())
            ask_for_spa = input('Would you like a SPA package? ')
            if ask_for_spa == 'yes':
                spa_ticket = SpaReservation(customer_name=name, hotel_object=hotel)
                print(spa_ticket.generate())
        else:
            print('Credit card authentication failed')
    else:
        print('There was a problem with your payment')
else:
    print('Hotel is not free')
