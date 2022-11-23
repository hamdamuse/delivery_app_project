from unittest.mock import patch, Mock
import sys
import sys

sys.path.append("..")
import app

import pytest


def navigate_main_menu():

    try:
        cmd = int(input("Enter input here -> "))
        if cmd == 0:
            # include save property
            exit()
        elif cmd == 1:
            return app.navigate_product_menu()
        elif cmd == 2:
            return app.navigate_courier_menu()
        elif cmd == 3:
            print("Order Menu pending")
        else:
            print("Error: Please input valid number.")
    except ValueError:
        print("Please enter a number.")


@patch("builtins.print")
def test_print_main_menu_options(mock_print):
    app.print_main_menu_options()
    mock_print.assert_called_with(
        """
Welcome to Hamda's cafe app:
MAIN MENU
Exit: 0
Product Menu: 1
Courier Menu: 2
Order Menu: 3
"""
    )


@patch("builtins.print")
def test_navigate_main_menu(mock_print):
    test_print_main_menu_options = Mock()
    test_print_main_menu_options.return_value = """
Welcome to Hamda's cafe app:
MAIN MENU
Exit: 0
Product Menu: 1
Courier Menu: 2
Order Menu: 3
"""

    with patch("builtins.input", return_value=1) as mock_cmd:
        assert input() == 1

        navigate_main_menu()
        if mock_cmd.return_value == 1:
            result = navigate_main_menu()
            expectation = app.navigate_product_menu()
            assert result == expectation
        elif mock_cmd.return_value == 2:
            result = navigate_main_menu()
            expectation = app.navigate_courier_menu()
            assert result == expectation
        elif mock_cmd.return_value == 3:
            mock_print.assert_called_with("Order Menu pending")
        else:
            mock_print.assert_called_with("Error: Please input valid number.")


@patch("builtins.print")
def test_print_product_menu_options_happy_case(mock_print):
    app.print_product_menu_options()
    mock_print.assert_called_with(
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

    print_product_options = Mock()
    print_product_options.return_value = print(
        """
PRODUCT MENU
Exit to MAIN MENU: 0
Print products: 1
Add product: 2
Update product: 3
Delete product: 4
"""
    )
    print_product_options()
    try:
        cmd = int(input("Enter input here -> "))
        if cmd == 0:
            # include save property
            app.navigate_main_menu()
        elif cmd == 1:
            print("Print products pending")
        elif cmd == 2:
            print("Add product pending")
        elif cmd == 3:
            print("Update product pending")
        elif cmd == 4:
            print("Delete product pending")
        else:
            print("Error: please input valid number.")
    except ValueError:
        print("Error: please enter a number.")

    print_product_options.assert_called_once


@patch("builtins.print")
def test_navigate_product_menu(mock_print):
    with patch("builtins.input", return_value=5) as mock_cmd:
        assert input() == 5

        navigate_product_menu()
        if mock_cmd.return_value == 0:
            app.navigate_main_menu.assert_called_with(app.navigate_main_menu())
        if mock_cmd.return_value == 1:
            mock_print.assert_called_with("Print products pending")
        elif mock_cmd.return_value == 2:
            mock_print.assert_called_with("Add product pending")
        elif mock_cmd.return_value == 3:
            mock_print.assert_called_with("Update product pending")
        elif mock_cmd.return_value == 4:
            mock_print.assert_called_with("Delete product pending")
        elif type(mock_print.return_value) == str:
            mock_print.assert_called_with("Error: please enter a number.")
        else:
            mock_print.assert_called_with("Error: please input valid number.")


@patch("builtins.print")
def test_navigate_product_menu_value_error_input(mock_print):

    with patch("builtins.input", return_value="hey") as mock_cmd:
        assert input() == "hey"
        navigate_product_menu()

        if type(mock_cmd.return_value) == str:
            mock_print.assert_called_with("Error: please enter a number.")


@patch("builtins.print")
def test_print_courier_menu_options(mock_print):
    app.print_courier_menu_options()
    mock_print.assert_called_with(
        """
COURIER MENU
Exit to MAIN MENU: 0
Print couriers: 1
Add courier: 2
Update courier: 3
Delete courier: 4
"""
    )
