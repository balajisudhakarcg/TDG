import xml.etree.ElementTree as ET
import copy
# from libs.Faker_helper import FakerHelper

from libs import rules
from libs.class1 import Class1
from libs.rules import RulesEngine, RulesDefinition


class XmlHelper:
    def __init__(self):
        print("xml helper")
        self.share_attr = None
        self.obj_pk = None
        self.p_cnt = 0

    def add_nodes_consolidate_op(self, mno_of_orders_x, op_path_x, schema_path_x, rules_data_pn, enterprise_data_pn,
                                 creditcard_data_pn, item_data_xn):
        # parse the xml
        tree_m_1 = self.parse_xml(schema_path_x)
        # copy order lines based on the no of rec
        updated_m_tree_1 = self.copy_order_lines(tree_m_1, mno_of_orders_x)
        # method to apply the rules
        updated_m_tree_2 = self.mul_record_updates(updated_m_tree_1, rules_data_pn, enterprise_data_pn,
                                                   creditcard_data_pn, item_data_xn)


        # code to add overall total ???
        # write the updated xml
        updated_m_tree_2.write(op_path_x, encoding='utf-8', xml_declaration=True)

    # ===========method to apply the rules ===================
    @staticmethod
    def mul_record_updates(tree_2, rules_data_p, enterprise_data_p, creditcard_data_p, item_data_x):
        root_2 = tree_2.getroot()
        # xml_doc = ET.tostring(root_2, encoding="unicode")
        # print(xml_doc)

        order_lines = root_2.findall('.//Item')
        for i, order_line in enumerate(order_lines):
            print(f"increment -- {i}")
            # loop through the rules
            engine_i = RulesEngine()
            up_rules_i = RulesDefinition(rules_data_p, enterprise_data_p, creditcard_data_p, item_data_x)
            # add the rules
            engine_i.add_rules(up_rules_i)
            for b in up_rules_i:

                if b.tag == 'attr' and i == 0:
                    print(f"{root_2.attrib}")
                    for attr, value in root_2.attrib.items():
                        # print(f"Node: {node.tag}, Attribute: {attr}, Value: {value}")
                        if attr == b.attr:
                            rvalue = b.action()
                            print("______________________________________")
                            print(f"{rvalue} is the output from faker method")
                            print("______________________________________")
                            root_2.set(b.attr, rvalue)
                            del rvalue
                            print(f"{b.attr} found in schema")

                elif b.tag == 'child':
                    print(f"{order_line.attrib} == order line")
                    s = b.attr
                    rvalue = b.action()
                    if "," in s:  #
                        my_list = s.split(',')
                        list_length = len(my_list)
                        for x in my_list:
                            print(f"{x} is the value of x")
                            if "ItemID" in s:
                                y = my_list.index(x) + 1
                            else:
                                y = my_list.index(x)
                            get_node_attrs = root_2.findall(b.xp)

                            if get_node_attrs is not None:
                                print("multi node success")
                                for k, node in enumerate(get_node_attrs):
                                    if k == i:
                                        print("multi node success in for with seperator")
                                        # Extract and print all attribute values for each node
                                        for attr, value in node.attrib.items():
                                            print(f"====Node: {node.tag}, Attribute: {attr}, Value: {value}===")
                                            if attr == x:
                                                rvalue = b.action()
                                                print("______________________________________")
                                                print(f"{rvalue[y]} is the output from faker method for separator/child")
                                                print("______________________________________")
                                                node.set(str(x), str(rvalue[y]))
                                                #del rvalue
                                                print(f"{x} found in schema")

                    elif "," not in s:
                        print("child no sepr")
                        get_node_attrs = root_2.findall(b.xp)
                        get_node_disc = root_2.findall('Promotions') # use this logic to set retail price
                        if get_node_attrs is not None:
                            print("multi node success")
                            for j, node in enumerate(get_node_attrs):
                                if j == i:
                                    print("multi node success in for")
                                    # Extract and print all attribute values for each node
                                    for attr, value in node.attrib.items():
                                        # print(f"Node: {node.tag}, Attribute: {attr}, Value: {value}")
                                        if attr == b.attr:
                                            rvalue = b.action()
                                            print("______________________________________")
                                            print(f"{rvalue[0]} is the output from faker method")
                                            print("______________________________________")
                                            node.set(b.attr, rvalue[0])
                                            del rvalue
                                            print(f"{b.attr} found in schema")
                        elif get_node_disc is not None:
                            print("multi node success")
                            for j, node in enumerate(get_node_attrs):
                                if j == i:
                                    print("multi node success in for")
                                    # Extract and print all attribute values for each node
                                    for attr, value in node.attrib.items():
                                        # print(f"Node: {node.tag}, Attribute: {attr}, Value: {value}")
                                        if attr == b.attr:
                                            rvalue = b.action()
                                            print("______________________________________")
                                            print(f"{rvalue[0]} is the output from faker method")
                                            print("______________________________________")
                                            node.set(b.attr, rvalue[0])
                                            del rvalue
                                            print(f"{b.attr} found in schema")


        #xml_doc = ET.tostring(root_2, encoding="unicode")
        #print(xml_doc)
        return tree_2

    # =====copy order lines based on the no of rec and return the xml tree====

    def copy_order_lines(self, mtree, mno_of_orders_x):
        root = mtree.getroot()

        # Find the <OrderLines> element
        order_lines = root.find('.//OrderLines')

        # Find the <OrderLine> element to copy
        original_order_line = order_lines.find('.//OrderLine')

        # Create copies of the <OrderLine> element and append them
        for i in range(int(mno_of_orders_x)):
            copy_order_line = copy.deepcopy(original_order_line)
            order_lines.append(copy_order_line)
        return mtree

    def xml_update(self, op_path, rules_data_p, enterprise_data_p,
                   creditcard_data_p, item_data_x, schema_path_x, no_of_rec):
        # parse the xml
        tree_1 = self.parse_xml(schema_path_x)
        # loop over the rules to init them
        updated_tree = self.one_record_updates(rules_data_p, enterprise_data_p, creditcard_data_p,
                                               item_data_x, tree_1)
        updated_tree.write(op_path, encoding='utf-8', xml_declaration=True)
        print("<<<<<<< Schema is updated and written to a xml file in folder output >>>>>>>>>")

    # ======== init the rules engine and apply the action methods===========
    @staticmethod
    def one_record_updates(rules_data_p, enterprise_data_p, creditcard_data_p,
                           item_data_x, tree_o_r):
        root_o_r = tree_o_r.getroot()
        engine = RulesEngine()
        up_rules = RulesDefinition(rules_data_p, enterprise_data_p, creditcard_data_p, item_data_x)
        # add the rules
        engine.add_rules(up_rules)
        for b in up_rules:
            if b.tag == 'attr':
                get_node_attr = root_o_r.get(b.attr)
                if get_node_attr is not None:
                    rvalue = b.action()
                    root_o_r.set(b.attr, rvalue)  # update the root element attr
                    del rvalue
                    print(f"{b.attr} found in schema")
                else:
                    print(f"{b.attr} not found in schema")
            elif b.tag == 'child':
                s = b.attr
                rvalue = b.action()
                if "," in s:
                    my_list = s.split(',')
                    list_length = len(my_list)
                    print(list_length)
                    for x in my_list:
                        print(f"{x} is the value of x")
                        get_node = root_o_r.find(b.xp).get(x)
                        if get_node is not None:
                            # print("success for tags logic")
                            # print(f"{rvalue} is the output from lambda")
                            y = my_list.index(x) + 1
                            print(f"{rvalue[y]} is the rs output from lambda update_child_attr")
                            root_o_r.find(b.xp).set(str(x), rvalue[y])
                        else:
                            print(f" {str(x)} node not found")
        return tree_o_r

    # ===============parse xml==========
    def parse_xml(self, xml_string_p):
        tree = ET.parse(xml_string_p)
        return tree
