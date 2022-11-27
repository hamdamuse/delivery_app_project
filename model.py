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

def print_products(product_list):
    for product in product_list:
        print(f"Name: {product['name']}, Price: {product['price']:.2f}")
    



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
    courier = input("Please enter index of courier to add to order -> ") #TODO: sort out user input type
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

def print_products_with_indexes(products):
    print("\n\tProducts with their indexes:")
    for index, product in enumerate(product_list):
        print(f"""\tIndex: {index}, Name: {product['name']}, Price: {product['price']}""")


def print_couriers_with_indexes(couriers):
    print("\n\tCouriers with their indexes:")
    for index, courier in enumerate(courier_list):
        print(f"""Index: {index}, Name: {courier['name']}, Phone: {courier['phone_number']}""")


def update_product(products):
    print_products_with_indexes(product_list)
    while True:
        try: 
            product_index = int(input("Please enter index of product to update -> "))
            product_name = input("Please enter updated product name -> ").strip()
            product_price = float(input("Please enter updated product price -> "))
            if product_name:
                product_list[product_index]['name'] = product_name
            if product_price:
                product_list[product_index]['price'] = product_price
                return product_list
        except ValueError:
                print("Error: please enter a number")
                continue
    

def update_courier(couriers):
    print_couriers_with_indexes(courier_list)   
    courier_index = int(input("Please enter index of courier to update -> "))
    courier_name = input("Please enter updated courier name -> ").strip()
    courier_phone = input("Please enter updated courier phone ->").strip()
    if courier_name:
        courier_list[courier_index]['name'] = courier_name
    if courier_phone:
        courier_list[courier_index]['phone_number'] = courier_phone
    return product_list


def update_order(orders):
    while True:
        try:
            print_orders_with_indexes(order_list)
            order_index = int(input("Please enter index of order to update -> "))
            customer_name = input("Please enter updated customer name -> ").strip()
            customer_address = input("Please enter updated customer address -> ").strip()
            print_couriers_with_indexes(courier_list)
            courier = int(input("Please enter updated courier index -> "))
            print_order_status_options_with_indexes()
            order_status_index = int(input("Please enter index of updated order status-> "))
        except ValueError:
            print("please enter a number ")
            continue
        items = input("Please enter updated product indices, separated by commas -> ").replace(" ", "")
        if customer_name:
            order_list[order_index]['customer_name'] = customer_name
        if customer_address:
            order_list[order_index]['customer_address'] = customer_address
        if courier:
            order_list[order_index]['courier'] = courier
        if order_status_index:
            order_list[order_index]['status'] = order_status_list[order_status_index]
        if items:
            order_list[order_index]['items'] = items
        return order_list


def print_order_status_options_with_indexes():
    order_statuses = ["PREPARING","OUT FOR DELIVERY","DELIVERED"]
    for order_status in enumerate(order_statuses):
        print("\n\t Order statuses with indexes:")
        print(f"Index: {order_status}")
    return order_statuses

order_status_list = print_order_status_options_with_indexes()


def print_orders_with_indexes(orders):
    print("\tOrders with their indexes:")
    for index, order in enumerate(order_list):
        print(f"""
        Index: {index},
        Customer name: {order['customer_name']},
        Customer address: {order['customer_address']},
        Customer phone{order['customer_phone']}, 
        Courier: {order['courier']}
        Status: {order['status']},
        Items: {order['items']}
        """)


def delete_product(products):
    print_products_with_indexes(product_list)
    try:
        index = int(input("Please enter index of product to remove -> "))
        product_list.pop(index)
    except ValueError:
        print("Please enter a number.")


def delete_courier(couriers):
    print_couriers_with_indexes(courier_list)
    try:
        index = int(input("Please enter index of courier to remove -> "))
        courier_list.pop(index)
    except ValueError:
        print("Please enter a number.")


def delete_order(orders):
    print_orders_with_indexes(order_list)
    try:
        index = int(input("Please enter index of order to remove -> "))
        order_list.pop(index)
    except ValueError:
        print("Please enter a number.")


def save_products_to_csv():
    save_products(product_list)


def save_couriers_to_csv():
    save_couriers(courier_list)


def save_orders_to_csv():
    save_orders(order_list)
