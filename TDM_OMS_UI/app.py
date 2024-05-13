from flask import Flask, render_template, request, flash, redirect, url_for

from libs.main import main
import sqlite3

app = Flask(__name__)
app.config["SECRET_KEY"] = "myapplication123"
db_locale = 'rules_data.db'


@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        schema_path = request.form["schema_path"]
        output_path = request.form["op_path"]
        choice_selected = request.form["process"]
        prefix_orders = request.form["ecode"]
        no_of_orders = request.form["nooforders"]
        type_of_op = request.form["filegrp"]
        #print(prefix_orders)
        #print(no_of_orders)
        #print(type_of_op)

        rules_data = query_db()
        co_data = query_codata_db(prefix_orders)
        cc_data = query_db_creditcard()
        it_data = query_db_item_data()

        #print(f"{co_data} is the enterprise data")
        main(schema_path_p=schema_path, output_path_p=output_path, m_choice_p=choice_selected,
             rules_data_p=rules_data, mno_of_orders_p=no_of_orders, mtype_of_op_p=type_of_op,
             enterprise_data_p=co_data, creditcard_data=cc_data ,item_data_p=it_data)

        flash("Your process is completed successfully,please check the output location !!!! ", "success")
    return render_template("home.html")


@app.route("/rules", methods=["GET", "POST"])
def rules():
    rules_data = query_db()
    return render_template("rules.html", rules_data=rules_data)


@app.route("/add_rules", methods=["GET", "POST"])
def add_rules():
    if request.method == "POST":
        rules_details = (
            request.form['input_xpath'],
            request.form['input_action'],
            request.form['input_attr'],
            request.form['input_tag']
        )
        add_rules_to_db(rules_details)
        flash("Your Rules had been added successfully,check the rules table for entries!!!! ", "success")
        return render_template("add_rules.html")
    else:
        return render_template("add_rules.html")


@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect(db_locale)
    c = conn.cursor()
    c.execute("DELETE FROM rules_table WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('rules'))


def add_rules_to_db(rules_details):
    connie = sqlite3.connect(db_locale)
    c = connie.cursor()
    sql_execute_str = 'INSERT INTO rules_table (xpath, action, attribute, tag) VALUES (?, ?, ?, ?)'
    c.execute(sql_execute_str, rules_details)
    connie.commit()
    connie.close()


def query_db():
    connie = sqlite3.connect(db_locale)
    c = connie.cursor()
    c.execute("""
    SELECT * FROM rules_table    
    """)
    r_data = c.fetchall()
    return r_data


def query_codata_db(kw):
    connie = sqlite3.connect(db_locale)
    c = connie.cursor()
    c.execute("""
    SELECT * FROM co_data WHERE kw=?   
    """, (kw,))
    r_data = c.fetchone()
    return r_data


def query_db_creditcard():
    connie = sqlite3.connect(db_locale)
    c = connie.cursor()
    c.execute("""
    SELECT * FROM credit_card_data    
    """)
    r_data_cc = c.fetchall()
    return r_data_cc


def query_db_item_data():
    connie = sqlite3.connect(db_locale)
    c = connie.cursor()
    c.execute("""
    SELECT * FROM item_data    
    """)
    r_data_cc = c.fetchall()
    return r_data_cc


# add init when you are done
if __name__ == "__main__":
    app.run(debug=True, port=5001)
