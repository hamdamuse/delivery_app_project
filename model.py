
from csv_layer import load,products_file_path,couriers_file_path,orders_file_path,save_couriers,save_orders,save_products


def load_products():
    product_list = load(products_file_path)
    formatted_product_list = [{"name": product["name"], "price": float(product['price'])} for product in product_list]
    return formatted_product_list

product_list = load_products()

def load_couriers():
    courier_list = load(couriers_file_path)
    return courier_list

courier_list = load_couriers()


def load_orders():
    order_list = load(orders_file_path)
    return order_list

order_list = load_orders()

def save_products_to_csv():
    save_products(product_list)

def save_couriers_to_csv():
    save_couriers(courier_list)

def save_orders_to_csv():
    save_orders(order_list)

def print_products(product_list):
    for product in product_list:
        print(f"Name: {product['name']}, Price: {product['price']:.2f}")

def print_couriers(courier_list):
    for courier in courier_list:
        print(f"Courier name: {courier['name']}, Phone number: {courier['phone_number']}")


def add_product(product_list, name, price):
    new_product= {'name': name, 'price': price}
    product_list.append(new_product)
    return product_list

def add_courier(courier_list, name, phone):
    new_courier = {'name': name, 'phone_number': phone}
    courier_list.append(new_courier)
    return courier_list

def add_order(order_list):
    pass

