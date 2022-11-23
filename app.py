import model


def print_main_menu_options():
    print(
        (
            """
Welcome to Hamda's cafe app:
MAIN MENU
Exit: 0
Product Menu: 1
Courier Menu: 2
Order Menu: 3
"""
        )
    )


def navigate_main_menu():
    print_main_menu_options()
    while True:
        try:
            cmd = int(input("Enter input here -> "))
            if cmd == 0:
                model.save_products_to_csv()
                model.save_couriers_to_csv()
                model.save_orders_to_csv()
                exit()
            elif cmd == 1:
                navigate_product_menu()
            elif cmd == 2:
                navigate_courier_menu()
                break
            elif cmd == 3:
                navigate_order_menu()
            else:
                print("Error: Please input valid number.")
            break
        except ValueError:
            print("Please enter a number.")
            break


def print_product_menu_options():
    print(
        """
PRODUCT MENU
Exit to MAIN MENU: 0
Print products: 1
Add product: 2
Update product: 3
Delete product: 4
"""
    )


def navigate_product_menu():
    while True:
        print_product_menu_options()
        try:
            cmd = int(input("Enter input here -> "))
            if cmd == 0:
                # include save property
                navigate_main_menu()
            elif cmd == 1:
                model.print_products(model.product_list)
            elif cmd == 2:
                product_name = input("Enter new product name -> ")
                product_price = float(input("Enter new product price -> "))
                model.add_product(model.product_list, product_name, product_price)
                continue
            elif cmd == 3:
                print("Update product pending")
                break
            elif cmd == 4:
                print("Delete product pending")
                break
            else:
                print("Error: please input valid number.")
            continue
        except ValueError:
            print("Error: please enter a number")
            continue


def print_courier_menu_options():
    print(
        """
COURIER MENU
Exit to MAIN MENU: 0
Print couriers: 1
Add courier: 2
Update courier: 3
Delete courier: 4
"""
    )


def navigate_courier_menu():

    while True:
        print_courier_menu_options()
        try:
            cmd = int(input("Enter input here -> "))
            if cmd == 0:
                # include save property
                navigate_main_menu()
            elif cmd == 1:
                model.print_couriers(model.courier_list)
            elif cmd == 2:
                courier_name = input("Please enter courier name -> ")
                courier_phone = input("Please enter courier phone number -> ")
                model.add_courier(model.courier_list, courier_name, courier_phone)
            elif cmd == 3:
                print("Update courier pending")
                break
            elif cmd == 4:
                print("Delete courier pending")
                break
            else:
                print("Error: please input valid number.")
            continue
        except ValueError:
            print("Error: please enter a number")
            continue


def print_order_menu_options():
    print(
        """
    ORDER MENU
    Exit to MAIN MENU: 0
    Print orders: 1
    Add order: 2
    Update order: 3
    """
    )


def navigate_order_menu():
    while True:
        print_order_menu_options()
        try:
            cmd = int(input("Enter input here -> "))
            if cmd == 0:
                navigate_main_menu()
            elif cmd == 1:
                model.print_orders(model.order_list)
            elif cmd == 2:
                customer_name = input("Please enter customer name -> ")
                customer_address = input("Please enter customer phone addresss -> ")
                customer_phone_number = input("Please enter customer phone number ->")
                model.add_order(
                    model.order_list,
                    customer_name,
                    customer_address,
                    customer_phone_number
                )
            elif cmd == 3:
                print("Update courier pending")
                break
            elif cmd == 4:
                print("Delete courier pending")
                break
            else:
                print("Error: please input valid number.")
            continue
        except ValueError:
            print("Error: please enter a number")
            continue


if __name__ == "__main__":
    model.load_products()
    model.load_couriers()
    model.load_orders()

    navigate_main_menu()
