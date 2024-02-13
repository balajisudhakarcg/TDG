import sqlite3

db_locale = 'rules_data.db'
connie = sqlite3.connect(db_locale)
c = connie.cursor()

c.execute("""
INSERT INTO rules_table (xpath ,action ,attribute ,tag ) VALUES
(".//API[@Name='createOrder']/Input/Order[@OrderNo='11550060']","get_order_number","OrderNo",""),
(".//API[@Name='scheduleOrder']/Input/ScheduleOrder[@OrderNo='11550060']","get_order_number","OrderNo",""),
(".//API[@Name='createOrder']/Input/Order[@CustomerEMailID='da@abc.com']","get_email","CustomerEMailID",""),
(".//API[@Name='releaseOrder']/Input/ReleaseOrder[@OrderNo='11550060']","get_order_number","OrderNo","")
""")

connie.commit()
connie.close()

