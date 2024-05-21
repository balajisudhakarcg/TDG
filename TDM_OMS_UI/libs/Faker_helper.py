import sqlite3

from faker import Faker
from datetime import datetime, timezone
# from libs.xml_helper import XmlHelper

import random
from libs.class1 import Class1
from libs.class2 import Class2


# from libs.xml_helper import XmlHelper


class FakerHelper:

    def __init__(self, rs, rs_cc, rs_it):
        self.fake = Faker()
        # self.xml_h = XmlHelper()
        self.rs = rs
        self.rs_cc = rs_cc
        self.rs_it = rs_it
        self.selected_values = []
        self.db_locale = 'rules_data.db'
        # self.item = None
        # self.objR = Class1()
        # Generate a random 9-digit number

    def get_email(self):
        return self.fake.email()

    # new framework
    def get_order_number(self):
        if self.rs is not None:

            # Access the value from the result tuple (assuming a single column query)
            column_value = self.rs[2]
            # print("Value:", column_value)
            number = str(self.fake.random_number(digits=9))
            number = column_value + number
            # print(number)
            # number_as_string = "{}".format(number)
            return number
        else:
            print("No value found for the given condition.")

    def get_seller_org(self):
        if self.rs is not None:
            # print(f"{self.rs} data from faker class")
            # Access the value from the result tuple (assuming a single column query)
            column_value = self.rs[3]
            # print("Value:", column_value)

            # print(number)
            # number_as_string = "{}".format(number)
            return column_value
        else:
            print("No value found for the given condition.")

    def get_enterprise_code(self):
        if self.rs is not None:
            # print(f"{self.rs} data from faker class")
            # Access the value from the result tuple (assuming a single column query)
            column_value = self.rs[1]
            # print("Value:", column_value)
            # print(number)
            # number_as_string = "{}".format(number)
            return column_value
        else:
            print("No value found for the given condition.")

    def get_item_attr_db(self):
        ir = self.get_unique_random()
        i_ids = 'abcde'
        print("Value retrieved from Class3:", ir)
        if self.rs_it is not None:
            i_ids = self.match_shared_var_return_rs_value(self.rs_it, ir)
            print("Value retrieved for PK:", str(i_ids[1]))
            c_1 = Class1()
            c_1.set_shared_variable(str(i_ids[1]))
            # self.item = i_ids[1]
        else:
            print("No value found for the given condition.")
        return i_ids

    def get_item_order_qty_db(self):
        i_oq = '11'
        # v_pk = self.xml_h.update_pk()
        c_2 = Class2()
        v_pk = c_2.print_shared_variable()
        # r_value = obj_c2.print_shared_variable()
        print("Value retrieved from self faker:", v_pk)
        if self.rs_it is not None:
            # i_oq = self.match_shared_var_return_one_rs_value_by_row(self.rs_it, v_pk, 4)
            i_oq = self.query_order_qty_db_fh(v_pk)
            i_oq = str(i_oq[0])
            print("Value retrieved for order qty:", i_oq)
        else:
            print("No value found for the given condition.")
        return i_oq

    def get_linepriceinfo_db(self):
        i_lpo = 'NA'
        # v_pk = self.xml_h.update_pk()
        c_2 = Class2()
        v_pk_1 = c_2.print_shared_variable()
        # r_value = obj_c2.print_shared_variable()
        print("Value retrieved from self faker:", v_pk_1)
        rs_lp = self.query_item_data_db_fh(v_pk_1)
        if rs_lp is not None:
            # desired_columns = ['itemid', 'listprice', 'retailprice', 'unitprice']
            # i_lpo = self.match_shared_var_return_one_rs_value_by_row_cols(self.rs_it, v_pk_1, desired_columns)
            print("Value retrieved for line price info:", rs_lp)
            return rs_lp

        else:
            print("No value found for the given condition.")

    # get the discount information and update the lineprice info too
    def get_discount_info(self):
        i_ldo = 'NA'
        # v_pk = self.xml_h.update_pk()
        c_2 = Class2()
        v_pk_1 = c_2.print_shared_variable()
        # r_value = obj_c2.print_shared_variable()
        print("Value retrieved from self faker:", v_pk_1)
        rs_d = self.query_discount_data(v_pk_1)
        if rs_d is not None:
            # desired_columns = ['itemid', 'listprice', 'retailprice', 'unitprice']
            # i_lpo = self.match_shared_var_return_one_rs_value_by_row_cols(self.rs_it, v_pk_1, desired_columns)
            print("Value retrieved for line price info:", rs_d)
            return rs_d

        else:
            print("No value found for the given condition.")

    # single method to update the discounted retail price
    def get_discounted_retail_price(self):
        i_ldo = 'NA'
        # v_pk = self.xml_h.update_pk()
        c_2 = Class2()
        v_pk_1 = c_2.print_shared_variable()
        # r_value = obj_c2.print_shared_variable()
        print("Value retrieved from self faker:", v_pk_1)
        rs_d = self.query_discount_retail_price(v_pk_1)
        if rs_d is not None:
            # desired_columns = ['itemid', 'listprice', 'retailprice', 'unitprice']
            # i_lpo = self.match_shared_var_return_one_rs_value_by_row_cols(self.rs_it, v_pk_1, desired_columns)
            print("Value retrieved for line price info:", rs_d)
            return rs_d

        else:
            print("No value found for the given condition.")

    def match_shared_var_return_one_rs_value_by_row_cols(self, rs, row_value, desired_columns):
        desired_columns_1 = desired_columns  # Subset of columns you want to retrieve

        print("Value retrieved from self faker for itemid:", row_value)
        criteria = {'itemid': row_value}

        result = self.fetch_subset_of_columns_and_match_row(rs, desired_columns_1, criteria)
        if result:
            print("Matched Row:", result)
        else:
            print("No matching row found.")
        return result
        # new framework ends

    def get_unique_random(self):
        while True:
            value = random.randint(1, 9)
            if value not in self.selected_values:
                self.selected_values.append(value)
            return value

        # def update_pk(self):
        #     test_val_pk = self.item  # Update global variable
        #     # print(f"inside method {test_val}")
        #     return test_val_pk

    def fetch_subset_of_columns_and_match_row(self, rows, columns, match_criteria):
        print(f"matching criteria : {match_criteria}")
        subset = [{col: row[i] for i, col in enumerate(columns)} for row in rows]
        print(f"subset : {subset}")
        matched_rows = [row for row in subset if all(row[key] == value for key, value in match_criteria.items())]
        print(f"matched rows =>{matched_rows}")
        return matched_rows

    @staticmethod
    def match_shared_var_return_rs_value(rs, shared_value):
        i = 0
        rs_value = 0
        for row in rs:
            if shared_value == i:
                rs_value = row
                print(f"{row} is the DB data from match_shared_var_return_rs_value")
            i = i + 1
        return rs_value

    @staticmethod
    def match_shared_var_return_one_rs_value_by_row(rs, row_value, col_index):
        rs_value = 'test'
        print(f"{row_value} is the value set under match_shared_var_return_one_rs_value_by_row")
        for row in rs:
            if row[1] == row_value:
                rs_value = row[col_index]
                # print(f"{row} is the DB data")
        return rs_value

    def query_item_data_db_fh(self, itemid):
        connie = sqlite3.connect(self.db_locale)
        c = connie.cursor()
        c.execute("""
        SELECT listprice, retailprice, unitprice FROM item_data WHERE itemid=?   
        """, (itemid,))
        r_data = c.fetchone()
        return r_data

    def query_order_qty_db_fh(self, itemid):
        connie = sqlite3.connect(self.db_locale)
        c = connie.cursor()
        c.execute("""
        SELECT orderedqty FROM item_data WHERE itemid=?   
        """, (itemid,))
        r_data = c.fetchone()
        return r_data

    # method to retrieve the discount , unit price for an item
    def query_discount_data(self, itemid):
        connie = sqlite3.connect(self.db_locale)
        c = connie.cursor()
        c.execute("""
                SELECT chargecategory,chargeperline,chargeperunit,chargename FROM item_data WHERE itemid=?   
                """, (itemid,))
        r_data = c.fetchone()
        return r_data

    def query_discount_retail_price(self, itemid):
        connie = sqlite3.connect(self.db_locale)
        c = connie.cursor()
        c.execute("""
                   SELECT retailprice_d FROM item_data WHERE itemid=?   
                   """, (itemid,))
        r_data = c.fetchone()
        return r_data
