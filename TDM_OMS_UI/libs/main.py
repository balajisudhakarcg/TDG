import xml.etree.ElementTree as ET
#from libs.Faker_helper import FakerHelper
from libs.order_helper import OrderHelper
from faker import Faker
import re


def main(schema_path_p, output_path_p, m_choice_p, rules_data_p, mno_of_orders_p, mtype_of_op_p, enterprise_data_p,
         creditcard_data, item_data_p):
    # refer the rules engine
    # print(enterprise_data_p)
    oh = OrderHelper()

    # menu operations
    if m_choice_p == "order":
        oh.OrderUpdates(output_path_p, mno_of_orders_p, mtype_of_op_p, enterprise_data_p,
                        creditcard_data, item_data_p, schema_path_p, rules_data_p)
    elif m_choice_p == 'return':
        print("Quitting the application")
    # write the update xmls
