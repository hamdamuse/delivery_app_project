#will contain menus

class MainMenu:
    def __init__(self):
        pass

    def print_main_menu_options(self):
        print(("""Welcome to Hamda's cafe app:
    Exit: 0
    Product Menu: 1
    Courier Menu: 2
    Order Menu: 3
    """))

    def navigate_menu(self):
        self.print_main_menu_options()
        while True:
            try:
                    cmd = int(input("Enter input here -> "))
                    if cmd == 0:
                        #include save property
                        exit()
                    elif cmd == 1:
                        run_product_menu = ProductMenu()
                        run_product_menu.navigate_menu()
                        
                    elif cmd == 2:
                        print("Courier Menu pending")
                        break
                    elif cmd == 3:
                        print("Order Menu pending")
                        break
                    
                    else: 
                        print("Error: Please input valid number.")
                    continue
            except ValueError:
                    print("Please enter a number.")
                    continue


class ProductMenu:
    def print_menu_options(self):
        print("""
    Welcome to the Product Menu.  
    Main Menu: 0
    Print Product List: 1
    Add Product: 2
    Update Product: 3
    Delete Product: 4
""")

    def navigate_menu(self):
        self.print_menu_options()
        
        while True:
            try:
                cmd = int(input("Enter input here -> "))
                if cmd == 0:
                    exit_to_main_menu = MainMenu()
                    exit_to_main_menu.navigate_menu()
                elif cmd == 1:
                    #move to user input for new product
                    print("PRINT")
                    break
                elif cmd == 2:
                    print("ADD")
                    break
                elif cmd == 3:
                    print("UPDATE")
                    break
                elif cmd == 4:
                    print("DELETE")
                    break
                else: 
                    print("Error: Please input valid number.")
                continue
            except ValueError:
                print("Please enter a number.")
                continue

    def user_input_new_product(self):
        product_name = input("Enter product name -> ")
        product_prince = float("Enter product price -> ")








    




if __name__ == "__main__":
    run_app = MainMenu()
    run_app.navigate_menu()
