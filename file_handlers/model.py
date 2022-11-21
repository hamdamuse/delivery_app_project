import csv_layer


def load_products():
    product_list = csv_layer.load("data\products.csv")
    formatted_product_list = [{"name": product["name"], "price": float(product['price'])} for product in product_list]
    return formatted_product_list

product_list = load_products()

def load_couriers():
    courier_list = csv_layer.load("data\couriers.csv")
    return courier_list

courier_list = load_couriers()

def load_orders():
    order_list = csv_layer.load("data\orders.csv")
    return order_list



print(product_list)
