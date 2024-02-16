import xml.etree.ElementTree as ET
from libs.Faker_helper import FakerHelper
from libs.order_helper import OrderHelper


def main(schema_path, output_path, m_choice, rules_data, mprefix_orders, mno_of_orders, mtype_of_op):
    # refer the rules engine
    oh = OrderHelper()
    engine = RulesEngine()
    up_rules = RulesDefinition(rules_data, mprefix_orders)
    # add the rules
    engine.add_rules(up_rules)
    # parse the xml
    tree = ET.parse(schema_path)
    root = tree.getroot()
    # menu operations
    if m_choice == "order":
        oh.OrderUpdates(up_rules, root, tree, output_path, mno_of_orders, mtype_of_op)
    elif m_choice == 'return':
        print("Quitting the application")
    # write the update xmls


class Rule:
    def __init__(self, condition, action, xp, attr):
        self.condition = condition
        self.action = action
        self.xp = xp
        self.attr = attr

    def evaluate(self, value):
        return self.condition(value)

    def ret_xp(self):
        return self.xp


class RulesEngine:
    def __init__(self):
        self.rules = []

    def add_rules(self, rule):
        self.rules.append(rule)

    def evaluate(self, value):
        errors = []
        for rule in self.rules:
            if not rule.evaluate(value):
                errors.append(rule.message)
        return errors


def RulesDefinition(rules_data, mprefix_orders):
    # fh = FakerHelper()

    # print(rules_data)
    m_rules = []
    for xd in rules_data:
        # print(xd)

        # Suppose you have a string containing the method name
        method_name = xd[2]

        # Create an instance of the class
        my_instance = FakerHelper(mprefix_orders)

        # Get the method using getattr and call it
        method_to_run = getattr(my_instance, method_name)
        m_rules.append(Rule(lambda x: x.find(xd[1]) is not None, method_to_run, xd[1], xd[3]))

    return m_rules
