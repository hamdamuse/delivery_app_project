import sys
sys.path.append("..")
import file_handlers.csv_layer as csv_layer

def load_products():
    product_list = csv_layer.load(csv_layer.products_file_path)
    formatted_product_list = [{"name": product["name"], "price": float(product['price'])} for product in product_list]
    return formatted_product_list

product_list = load_products()

def load_couriers():
    courier_list = csv_layer.load(csv_layer.couriers_file_path)
    #formatted_courier_list = [{}]
    return courier_list

courier_list = load_couriers()


def load_orders():
    order_list = csv_layer.load(csv_layer.orders_file_path)
    return order_list

order_list = load_orders()

def save_products():
    csv_layer.save_products(product_list)

def save_couriers():
    csv_layer.save_couriers(courier_list)

def save_orders():
    csv_layer.save_orders(order_list)

def print_products(product_list):
    pass


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

print(courier_list)



print(product_list)
print(order_list)