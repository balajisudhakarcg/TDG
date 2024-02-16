from libs.xml_helper import XmlHelper


class OrderHelper:
    def __init__(self):
        self.xh = XmlHelper()

    def OrderUpdates(self,up_rules, root, tree, output_path, mno_of_orders, mtype_of_op):
        print("<<<<<<<<< Creating a order xml updates >>>>>>>>>>>>>>")
        # loop through the dict and evaluate the rules against the xml
        if mno_of_orders == "1":
            # add the orderno prefix
            self.xh.xml_update(up_rules, root, tree, output_path)

        elif mno_of_orders != "1" and mtype_of_op == "Consolidated output":
            self.xh.addnodes_consolidate_op(up_rules, mno_of_orders, root, tree, output_path)

        elif mno_of_orders != "1" and mtype_of_op == "Separate files":
            self.xh.addnodes_seperate_op(up_rules, mno_of_orders, root, tree, output_path)
            # add logic for number of file

            # update the xml update method to update all based on xpaths
            # split the files for differnt files
