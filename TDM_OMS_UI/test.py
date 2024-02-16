from flask import Flask, render_template, request, flash

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
        prefix_orders = request.form["prefix"]
        no_of_orders = request.form["nooforders"]
        type_of_op = request.form["filegrp"]
        print(prefix_orders)
        print(no_of_orders)
        print(type_of_op)

        rules_data = query_db()
        main(schema_path, output_path, choice_selected, rules_data,prefix_orders,no_of_orders,type_of_op)
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
        return render_template("add_rules.html")
    else:
        return render_template("add_rules.html")


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


# add init when you are done
if __name__ == "__main__":
    app.run(debug=True, port=5001)
