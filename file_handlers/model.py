import csv_layer


def load_products():
    product_list = csv_layer.load(r"data\products.csv")
    formatted_product_list = [{"name": product["name"], "price": float(product['price'])} for product in product_list]
    return formatted_product_list

product_list = load_products()

def load_couriers():
    courier_list = csv_layer.load(r"data\couriers.csv")
    #formatted_courier_list = [{}]
    return courier_list

courier_list = load_couriers()

def load_orders():
    order_list = csv_layer.load(r"data\orders.csv")
    return order_list


def add_product(product_list,name,price):
    pass


print(product_list)