import sqlite3

db_locale = 'rules_data.db'
connie = sqlite3.connect(db_locale)
c = connie.cursor()

c.execute("""

CREATE TABLE rules_table 
(id INTEGER PRIMARY KEY AUTOINCREMENT,
xpath TEXT,
action TEXT,
attribute TEXT,
tag TEXT
)
""")

connie.commit()
connie.close()

