from csv_layer import (
    load,
    products_file_path,
    couriers_file_path,
    orders_file_path,
    save_couriers,
    save_orders,
    save_products,
)


def load_products():
    product_list = load(products_file_path)
    formatted_product_list = [
        {"name": product["name"], "price": float(product["price"])}
        for product in product_list
    ]
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



def print_products_with_indexes(product_list):
    print("\tProducts with their indexes:")
    for index, product in enumerate(product_list):
        print(f"""\tIndex: {index}, Name: {product['name']}, Price: {product['price']}""")



def print_couriers_with_indexes(courier_list):
    print("\tCouriers with their indexes:")
    for index, courier in enumerate(courier_list):
        print(f"""Index: {index}, Name: {courier['name']}, {courier['phone_number']}""")


def print_couriers(courier_list):
    for courier in courier_list:
        print(
            f"Courier name: {courier['name']}, Phone number: {courier['phone_number']}"
        )


def print_orders(order_list):
    for order in order_list:
        print(
            f"""
        Customer name: {order['customer_name']},
        Customer address: {order['customer_address']},
        Customer phone: {order['customer_phone']},
        Courier: {order['courier']},
        Status: {order['status']},
        Items: {order['items']}"""
        )


def add_product(product_list, name, price):
    new_product = {"name": name, "price": price}
    product_list.append(new_product)
    return product_list


def add_courier(courier_list, name, phone):
    new_courier = {"name": name, "phone_number": phone}
    courier_list.append(new_courier)
    return courier_list


def add_order(order_list, customer_name, customer_address, customer_phone):
    print_products_with_indexes(product_list)
    product_index_values = str(
        input(
            """    
Please enter indexes of products,separated by commas, to add to order -> """).replace(" ", ""))
    print_couriers_with_indexes(courier_list)
    courier = input("Please enter index of courier to add to order -> ")
    new_order = {
        "customer_name": customer_name,
        "customer_address": customer_address,
        "customer_phone": customer_phone,
        "courier": courier,
        "status": "preparing",
        "items": product_index_values
    }
    order_list.append(new_order)
    return order_list

def update_product(products):
    print_products_with_indexes(product_list)
    while True: 
        product_index = int(input("Please enter index of product to update -> "))
        product_name = input("Please enter updated product name -> ")
        product_price = input("Please enter updated product price -> ")
        if product_name:
            product_list[product_index]['name'] = product_name
        if product_price:
            try:
                float(product_price)
            except ValueError:
                print("Error: please enter a number")
                continue
    
            product_list[product_index]['price'] = product_price
            return product_list
    

def update_courier(couriers):
    print_couriers_with_indexes(courier_list)   
    courier_index = int(input("Please enter index of courier to update -> "))
    courier_name = input("Please enter updated courier name -> ")
    courier_phone = input("Please enter updated courier phone ->")
    if courier_name:
        courier_list[courier_index]['name'] = courier_name
    if courier_phone:
        courier_list[courier_index]['phone_number'] = courier_phone
    return product_list


