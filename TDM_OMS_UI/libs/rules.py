from libs.Faker_helper import FakerHelper


class Rule:
    def __init__(self, condition, action, xp, attr, tag):
        self.condition = condition
        self.action = action
        self.xp = xp
        self.attr = attr
        self.tag = tag

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


def RulesDefinition(rules_data, enterprise_data_rs, creditcard_data, item_data_p):
    # fh = FakerHelper()

    # print(rules_data)
    # print(enterprise_data_rs)
    m_rules = []
    for xd in rules_data:
        #print(xd)

        # Suppose you have a string containing the method name
        method_name = xd[2]
        print(f"{method_name} is the method name from rules data")
        # Create an instance of the class
        my_instance = FakerHelper(enterprise_data_rs, creditcard_data, item_data_p)
        # my_instance = Faker()
        # Get the method using getattr and call it
        method_to_run = getattr(my_instance, method_name)
        m_rules.append(Rule(lambda x: x.get(xd[1]) is not None, method_to_run, xd[1], xd[3], xd[4]))

    return m_rules
