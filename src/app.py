import os

def main_menu():
    main_options = int(input(""" 
Exit: 0
Continue: 1
"""))
    while main_options !=0:
        sub_menu()
    exit()


def sub_menu():
    option = int(input("""
Welcome to the product and courier menu.
Main menu: 0
Print list: 1
Add to product/courier list: 2
Update product/courier list: 3
Delete product/courier: 4:
"""))

    if option < 0 or option > 4:
        raise ValueError("Please enter a number between 0 and 4.")
    while option != 0:
        if option ==1:
            print_menu()
        elif option == 2:
            create_item()
        elif option == 3:
            update_item()
        elif option == 4:
            delete_item()

def print_menu():
    which_file = int(input("""
Which menu would you like to access?
Product: 1
Courier: 2
"""))
    if which_file == 1:
        try:
            with open(r"mini project products list.txt", "r") as product:
                product_list = product.readlines()
                formatted_product_list = [i.strip("\n") for i in product_list]
                print(f"Products: {formatted_product_list}")
        except Exception as e:
            print(f"Error: {str(e)}.")
            os.system("clear")
        return sub_menu()
    elif which_file == 2:
        try:
            with open(r"mini project courier list.txt", "r") as courier:
                courier_list = courier.readlines()
                formatted_courier_list = [i.strip("\n") for i in courier_list]
                print(f"Couriers: {formatted_courier_list}")
        except Exception as e:
            print(f"Error: {str(e)}.")
        return sub_menu

def create_item():
    which_file = int(input("""
Which menu would you like to access?
Product: 1
Courier: 2
"""))
    if which_file == 1:
        new_item = input("Enter new product:\n")
        try:
            with open(r"mini project products list.txt","a") as products:
                products.write("\n" + new_item)
        except Exception as e:
            print(f"Error: {str(e)}")
        return sub_menu()
    elif which_file == 2:
        new_item = input("Enter new courier:\n")
        try:
            with open(r"mini project courier list.txt","a") as courier:
                courier.write("\n"+ new_item)
        except Exception as e:
            print(f"Error: {str(e)}")
        return sub_menu()

if __name__ == "__main__":
    main_menu()