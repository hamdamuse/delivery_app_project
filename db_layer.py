import sqlite3
import pandas as pd

connection = sqlite3.connect("product.db")

cursor = connection.cursor()


def initialise_db():
    cursor.execute("CREATE TABLE product ( name TEXT, price REAL)")
    cursor.execute("Insert INTO product VALUES ('espresso', 2.50)")
    cursor.execute("Insert INTO product VALUES ('double espresso', 2.70)")
    cursor.execute("Insert INTO product VALUES ('latte', 3.00)")
    cursor.execute("Insert INTO product VALUES ('cappuccino', 2.50)")
    connection.commit()

def print_products():
    rows = cursor.execute("SELECT rowid, name, price FROM product").fetchall()
    print(rows)
    connection.commit()


def print_products_df():
    df = pd.read_sql_query("SELECT rowid, name, price from product", connection).set_index('rowid')
    print(df)


def add_product():
    name = input("Please enter product name -> ")
    price = float(input("Please enter product price -> "))
    cursor.execute("INSERT INTO product VALUES (?,?)",
    (name, price))
    connection.commit()
    
def update_product():
    pass


print_products_df()





