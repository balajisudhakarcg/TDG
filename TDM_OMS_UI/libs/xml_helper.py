import xml.etree.ElementTree as ET
import copy


class XmlHelper:
    def __init__(self):
        print("xml helper")

    def xml_update(self, rules, root, mtree, op_path):
        for b in rules:
            #print(f"{b.action} action method")
            #print(f"{b.xp} is the xpath ")
            if b.evaluate(root):
                for node in root.findall(b.xp):
                    # Extract and print all attribute values for each node
                    for attr, value in node.attrib.items():
                       # print(f"Node: {node.tag}, Attribute: {attr}, Value: {value}")
                        if attr == b.attr:
                            rvalue = b.action()
                            node.set(b.attr, rvalue)
                            del rvalue
                            print(f"{b.attr} found in schema")
            else:
                print("node not found")
        # save the modified xml
        # modified_xml = ET.tostring(root, encoding='utf-8').decode('utf-8')
        mtree.write(op_path, encoding='utf-8', xml_declaration=True)
        print("<<<<<<< Schema is updated and written to a xml file in folder output >>>>>>>>>")

    def addnodes_consolidate_op(self, rules, mno_of_orders, root, tree, op_path):
        order_lines_element = tree.find(".//API[@Name='createOrder']//OrderLines")
        # new_order_line = order_lines_element[0].copy

        for x in range(int(mno_of_orders)):
            new_order_line = copy.deepcopy(order_lines_element[0])
            #print(x)
            new_order_line.attrib['PrimeLineNo'] = str(x + 2)  # Change OrderedQty to 5.0
            # You can update other elements or attributes similarly
            order_lines_element.append(new_order_line)
            self.xml_update_multi(rules=rules, root=root, mtree=tree, op_path=op_path)
        # tree.write('your_xml_file.xml')

    def addnodes_seperate_op(self, rules, mno_of_orders, root, tree, op_path):

        for x in range(int(mno_of_orders)):
            op_path = op_path.replace(".xml", "_" + str(x) + ".xml")
            self.xml_update(rules, root, tree, op_path)

    def xml_update_multi(self, rules, root, mtree, op_path):
        # if the condition is true then use the dict xpath to update the xmls
        for b in rules:
            #print(f"{b.action} action method")
            #print(f"{b.xp} is the xpath ")
            if b.evaluate(root):
                for node in root.findall(b.xp):
                    # Extract and print all attribute values for each node
                    for attr, value in node.attrib.items():
                        #print(f"Node: {node.tag}, Attribute: {attr}, Value: {value}")
                        if attr == b.attr:
                            rvalue = b.action()
                            node.set(b.attr, rvalue)
                            del rvalue
                            print(f"{b.attr} found in schema")
            else:
                print("node not found")
        # save the modified xml
        # modified_xml = ET.tostring(root, encoding='utf-8').decode('utf-8')
        mtree.write(op_path, encoding='utf-8', xml_declaration=True)
        print("<<<<<<< Schema is updated and written to a xml file in folder output >>>>>>>>>")
