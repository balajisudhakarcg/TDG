from libs.xml_helper import XmlHelper


class OrderHelper:
    def __init__(self):
        self.xh = XmlHelper()

    def OrderUpdates(self, output_path, mno_of_orders, mtype_of_op, enterprise_data_p,
                     creditcard_data, item_data_p, schema_path_p, rules_data_o):
        print("<<<<<<<<< Creating a order xml updates >>>>>>>>>>>>>>")
        # loop through the dict and evaluate the rules against the xml
        if mno_of_orders == "1" and mtype_of_op != "Consolidated output":
            # add the orderno prefix
            self.xh.xml_update(op_path=output_path, enterprise_data_p=enterprise_data_p,
                               creditcard_data_p=creditcard_data, item_data_x=item_data_p,
                               schema_path_x=schema_path_p, rules_data_p=rules_data_o)

        elif mno_of_orders != "1" and mtype_of_op == "Consolidated output":
            self.xh.add_nodes_consolidate_op(mno_of_orders_x=mno_of_orders, op_path_x=output_path,
                                             schema_path_x=schema_path_p, enterprise_data_pn=enterprise_data_p,
                                             creditcard_data_pn=creditcard_data, item_data_xn=item_data_p,
                                             rules_data_pn=rules_data_o)

        elif mno_of_orders != "1" and mtype_of_op == "Separate files":
            self.xh.add_nodes_separate_op(op_path_a=output_path, enterprise_data_p_a=enterprise_data_p,
                                          creditcard_data_p_a=creditcard_data, item_data_x_a=item_data_p,
                                          schema_path_x_a=schema_path_p, rules_data_p_a=rules_data_o,
                                          no_of_rec=mno_of_orders)
            # add logic for number of file

            # update the xml update method to update all based on xpaths
            # split the files for differnt files
