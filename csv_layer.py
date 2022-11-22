from pathlib import Path
import csv

products_file_path = r"data\products.csv"
couriers_file_path = r"data\couriers.csv"
orders_file_path = r"data\orders.csv"

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
            fieldnames = ["name", "phone_number"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for courier in courier_list:
                writer.writerow(courier)
    except FileNotFoundError:
        print("File not found, please try again.")
    except TypeError:
        print("TypeError: Please check input type")
    except Exception as e:
        print(f"Error: {str(e)}")


def save_orders(order_list):
    
    try:
        with open(orders_file_path, "w", newline="") as file:
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
