from pathlib import Path
import csv


def load(file_name):
    item_list = []
    try:
        with open(file_name, "r") as file:
            if Path(file_name).suffix == ".csv":
                csv_file = csv.DictReader(file)
                for row in csv_file:
                    item_list.append(row)
                return item_list
            else:
                print("Incorrect file extension. Please make sure file is csv.")
    except FileNotFoundError:
        print("File not found, please try again.")
    if not item_list:
        print("List empty. Please add items.")
        # TODO: direct to add products


products_file_path = r"C:\Users\Owner\OneDrive\Documents\generation\mini project\draft\delivery_app_project\data\products.csv"
couriers_file_path = r"C:\Users\Owner\OneDrive\Documents\generation\mini project\draft\delivery_app_project\data\couriers.csv"
orders_file_path = r"C:\Users\Owner\OneDrive\Documents\generation\mini project\draft\delivery_app_project\data\orders.csv"


def save_products(product_list):
    # data hardcoded as model isn't finished
    try:
        with open(products_file_path, "w", newline="") as file:
            fieldnames = ["name", "price"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for product in product_list:
                writer.writerow(product)
            
    except FileNotFoundError:
        print("File not found, please try again.")
    except TypeError:
        print("TypeError: Please check input type")
    except Exception as e:
        print(f"Error: {str(e)}")


def save_couriers(courier_list):
    # hardcoded as model yet to be written
    courier_list = [
        {"name": "Bob", "phone_number": "0789887889"},
        {"name": "Jane", "phone_number": "0783458075"},
    ]
    try:
        with open(couriers_file_path, "w", newline="") as file:
            if Path(couriers_file_path).suffix == ".csv":
                fieldnames = ["name", "phone_number"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for courier in courier_list:
                    writer.writerow(courier)
            else:
                print("Incorrect file extension. Please make sure file is csv.")
    except FileNotFoundError:
        print("File not found, please try again.")
    except TypeError:
        print("TypeError: Please check input type")
    except Exception as e:
        print(f"Error: {str(e)}")


def save_orders(order_list):
    # order_list hardcoded as functionality is limited at present.
    order_list = [
        {
            "customer_name": "Jim",
            "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
            "customer_phone": "0723455889",
            "courier": 1,
            "status": "preparing",
            "items": "0,1",
        },
        {
            "customer_name": "Jane",
            "customer_address": "Unit 3, 12 Main Street, LONDON, WH1 2ER",
            "customer_phone": "0738475029",
            "courier": 1,
            "status": "preparing",
            "items": "0,1",
        },
    ]
    try:
        with open(orders_file_path, "w", newline="") as file:
            if Path(orders_file_path).suffix == ".csv":
                fieldnames = [
                    "customer_name",
                    "customer_address",
                    "customer_phone",
                    "courier",
                    "status",
                    "items",
                ]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for order in order_list:
                    writer.writerow(order)
            else:
                print("Incorrect file extension. Please make sure file is csv.")
    except FileNotFoundError:
        print("File not found, please try again.")
    except TypeError:
        print("TypeError: Please check input type")
    except Exception as e:
        print(f"Error: {str(e)}")
