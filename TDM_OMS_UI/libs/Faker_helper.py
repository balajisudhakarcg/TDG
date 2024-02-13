from faker import Faker
from datetime import datetime, timezone


class FakerHelper:

    def __init__(self):
        self.fake = Faker()
        self.email_address = self.fake.email()
        # Generate a random 9-digit number
        self.order_no = self.fake.random_number(digits=9)
        self.email_address = self.fake.email()
        # Generate a random date and time
        self.random_date_time = self.fake.date_time_this_year(tzinfo=timezone.utc)
        # personal info nick name
        self.nick_name = self.fake.name()
        # building no 1
        self.building1 = self.fake.building_number()
        # Street number 1
        self.street1 = self.fake.street_address()
        # city 1
        self.city_us1 = self.fake.city()
        #state
        self.state_us1 = self.fake.state()
        # day phone 1
        self.ph1 = self.fake.phone_number()
        # email id 2
        self.email_address1 = self.fake.email()
        # first name
        self.fn1 = self.fake.first_name()
        # second name
        self.ln1 = self.fake.last_name()
        # zip code
        self.zc1 = self.fake.postcode()
        # building no 1
        self.building2 = self.fake.building_number()
        # Street number 1
        self.street2 = self.fake.street_address()
        # city 1
        self.city_us2 = self.fake.city()

        # day phone 1
        self.ph2 = self.fake.phone_number()
        # email id 2
        self.email_address2 = self.fake.email()
        # first name
        self.fn2 = self.fake.first_name()
        # second name
        self.ln2 = self.fake.last_name()
        # zip code
        self.zc2 = self.fake.postcode()

    def get_email(self):
        return self.email_address

    def get_order_number(self):
        number = str(self.order_no)
        # print(number)
        # number_as_string = "{}".format(number)
        return number

    def get_order_date(self):
        # Format the date and time as per the specified format
        formatted_date_time = self.random_date_time.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        return formatted_date_time

    def get_nick_name(self):
        return self.nick_name
        # building no 1

    def get_building_no1(self):
        return self.building1

    # Street number 1
    def get_street_no1(self):
        #print(str(self.street1))
        st_no = self.street1
        st_ret = str(st_no)
        return st_ret

    # city 1
    def get_city1(self):
        return self.city_us1

    # day phone 1
    def get_phone1(self):
        return self.ph1

    # email id 2
    def get_email1(self):
        return self.email_address1

    # first name
    def get_firstname1(self):
        return self.fn1

    # second name
    def get_lastname1(self):
        return self.ln1

    # zip code
    def get_postcode(self):
        return self.zc1

    # building no 1
    def get_building2(self):
        return self.building2

    # Street number 1
    def get_street2(self):
        return self.street2

    # city 1
    def get_city2(self):
        return self.city_us2

    # day phone 1
    def get_ph2(self):
        return self.ph2

    # email id 2
    def get_email2(self):
        return self.email_address2

    # first name
    def get_firstname2(self):
        return self.fn2

    # second name
    def get_lastname2(self):
        return self.ln2

    # zip code
    def get_zipcode2(self):
        return self.zc2

    def get_state1(self):
        # state
        return self.state_us1