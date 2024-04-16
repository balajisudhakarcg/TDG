from faker import Faker
from datetime import datetime, timezone


class FakerHelper:

    def __init__(self, prefix):
        self.fake = Faker()
        self.prefix = prefix
        # Generate a random 9-digit number

    def get_email(self):
        return self.fake.email()

    def get_order_number(self):
        number = str(self.fake.random_number(digits=9))
        number = self.prefix + number
        # print(number)
        # number_as_string = "{}".format(number)
        return number

    def get_order_date(self):
        # Format the date and time as per the specified format
        # Generate a random date and time
        random_date_time = self.fake.date_time_this_year(tzinfo=timezone.utc)
        formatted_date_time = random_date_time.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        return formatted_date_time

    def get_nick_name(self):
        # personal info nick name
        nick_name = self.fake.name()
        return nick_name
        # building no 1

    def get_building_no1(self):
        # building no 1
        building1 = self.fake.building_number()
        return building1

    # Street number 1
    def get_street_no1(self):
        # Street number 1
        street1 = self.fake.street_address()
        st_no = street1
        st_ret = str(st_no)
        return st_ret

    # city 1
    def get_city1(self):
        # city 1
        city_us1 = self.fake.city()
        return city_us1

    # day phone 1
    def get_phone1(self):
        # day phone 1
        ph1 = self.fake.phone_number()
        return ph1

    # email id 2
    def get_email1(self):
        # email id 2
        email_address1 = self.fake.email()
        return email_address1

    # first name
    def get_firstname1(self):
        # first name
        fn1 = self.fake.first_name()
        return fn1

    # second name
    def get_lastname1(self):
        # second name
        ln1 = self.fake.last_name()
        return ln1

    # zip code
    def get_postcode(self):
        # zip code
        zc1 = self.fake.postcode()
        return zc1

    # building no 1
    def get_building2(self):
        # building no 1
        building2 = self.fake.building_number()
        return building2

    # Street number 1
    def get_street2(self):
        # Street number 1
        street2 = self.fake.street_address()
        return street2

    # city 1
    def get_city2(self):
        # city 1
        city_us2 = self.fake.city()
        return city_us2

    # day phone 1
    def get_ph2(self):
        # day phone 1
        ph2 = self.fake.phone_number()
        return ph2

    # email id 2
    def get_email2(self):
        # email id 2
        email_address2 = self.fake.email()
        return email_address2

    # first name
    def get_firstname2(self):
        # first name
        fn2 = self.fake.first_name()
        return fn2

    # second name
    def get_lastname2(self):
        # second name
        ln2 = self.fake.last_name()
        return ln2

    # zip code
    def get_zipcode2(self):
        # zip code
        zc2 = self.fake.postcode()
        return zc2

    def get_state1(self):
        # state
        state_us1 = self.fake.state()
        return state_us1
