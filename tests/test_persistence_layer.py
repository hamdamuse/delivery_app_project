from unittest.mock import patch, mock_open

import csv
from io import StringIO


def test_load_products():
    product_list = []
    with patch(
        "builtins.open",
        mock_open(
            read_data="""name,price
coke zero, 0.8
7up, 0.8"""
        ),
    ) as m:
        with open("mock_products_csv", "r") as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                product_list.append(row)
    result = product_list
    expectation = [
        {"name": "coke zero", "price": " 0.8"},
        {"name": "7up", "price": " 0.8"},
    ]
    assert result == expectation
    return product_list


def test_load_couriers():
    courier_list = []
    with patch(
        "builtins.open",
        mock_open(
            read_data="""name,phone_number
Bob,0789887889
Jane,0783458075
"""
        ),
    ) as mocked_couriers:
        with open("mock_couriers_csv", "r") as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                courier_list.append(row)
    result = courier_list
    expectation = [
        {"name": "Bob", "phone_number": "0789887889"},
        {"name": "Jane", "phone_number": "0783458075"},
    ]
    assert result == expectation
    return courier_list


def test_load_orders():
    orders_list = []
    with patch(
        "builtins.open",
        mock_open(
            read_data="""customer_name,customer_address,customer_phone,courier,status,items
John,"Unit 2, 12 Main Street, LONDON, WH1 2ER",0789887334,2,preparing,"0,1"
"""
        ),
    ) as mocked_couriers:
        with open("mock_orders_csv", "r") as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                orders_list.append(row)
    result = orders_list
    expectation = [
        {
            "customer_name": "John",
            "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
            "customer_phone": "0789887334",
            "courier": "2",
            "status": "preparing",
            "items": "0,1",
        }
    ]
    assert result == expectation
    return orders_list


def test_save_products_includes_exception_handling():
    mock_product_list = [
        {"name": "fanta", "price": 0.8},
        {"name": "coke", "price": 0.8},
    ]
    try:
        with patch("builtins.open", mock_open) as mocked_open:
            with open("mock_products", "w", newline="") as file:
                fieldnames = ["name", "price"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for product in mock_product_list:
                    writer.writerow(product)
    except FileNotFoundError:
        print("File not found, please try again.")
    except TypeError:
        print("TypeError: Please check input type")
    except Exception as e:
        print(f"Error: {str(e)}")
        result = file.readlines()
        expectation = ["name,price\r\n", "fanta,0.8\r\n", "coke,0.8\r\n"]


def test_save_products_using_string_IO_object():
    mock_product_list = [
        {"name": "fanta", "price": 0.8},
        {"name": "coke", "price": 0.8},
    ]
    mock_products_csv = StringIO()
    mock_products_csv.seek(0)
    fieldnames = ["name", "price"]
    writer = csv.DictWriter(mock_products_csv, fieldnames=fieldnames)
    writer.writeheader()
    for product in mock_product_list:
        writer.writerow(product)
    mock_products_csv.seek(0)
    result = mock_products_csv.readlines()
    expectation = ["name,price\r\n", "fanta,0.8\r\n", "coke,0.8\r\n"]
    assert result == expectation


def test_save_products_includes_exception_handling():
    mock_product_list = [
        {"name": "fanta", "price": 0.8},
        {"name": "coke", "price": 0.8},
    ]
    try:
        with patch("builtins.open", mock_open) as mocked_open:
            with open("mock_products", "w", newline="") as file:
                fieldnames = ["name", "price"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for product in mock_product_list:
                    writer.writerow(product)
    except FileNotFoundError:
        print("File not found, please try again.")
    except TypeError:
        print("TypeError: Please check input type")
    except Exception as e:
        print(f"Error: {str(e)}")
        result = file.readlines()
        expectation = ["name,price\r\n", "fanta,0.8\r\n", "coke,0.8\r\n"]


def test_save_couriers():
    mock_courier_list = [
        {"name": "Bruce", "phone": "0789887889"},
        {"name": "Helen", "phone": "0783458075"},
    ]
    try:
        with patch("builtins.open", mock_open) as mocked_open:
            with open("mock_couriers", "w", newline="") as file:
                fieldnames = ["name", "phone"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for courier in mock_courier_list:
                    writer.writerow(courier)
    except FileNotFoundError:
        print("File not found, please try again.")
    except TypeError:
        print("TypeError: Please check input type")
    except Exception as e:
        print(f"Error: {str(e)}")
        result = file.readlines()
        expectation = ["name,phone\r\n", "Bruce,0789887889\r\n", "Helen,0783458075\r\n"]
        assert result == expectation


def test_save_orders():
    mock_order_list = [
        {
            "customer_name": "Jim",
            "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
            "customer_phone": "0723455889",
            "courier": 1,
            "status": "preparing",
            "items": "0,1",
        },
        {
            "customer_name": "Jane",
            "customer_address": "Unit 3, 12 Main Street, LONDON, WH1 2ER",
            "customer_phone": "0738475029",
            "courier": 1,
            "status": "preparing",
            "items": "0,1",
        },
    ]
    try:
        with patch("builtins.open", mock_open) as mocked_open:
            with open("mock_couriers", "w", newline="") as file:
                fieldnames = [
                    "customer_name",
                    "customer_address",
                    "customer_phone",
                    "courier",
                    "status",
                    "items",
                ]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for order in mock_order_list:
                    writer.writerow(order)
    except FileNotFoundError:
        print("File not found, please try again.")
    except TypeError:
        print("TypeError: Please check input type")
    except Exception as e:
        print(f"Error: {str(e)}")
        result = file.readlines()
        expectation = [
            "customer_name,customer_address,customer_phone,courier,status,items\r\n",
            'Jim,"Unit 2,12 Main Street LONDON, WH1 2ER",0723455889,1,preparing,"0,1"\r\n',
            'Helen,"Unit 3,12 Main Street LONDON, WH1 2ER",0738475029,1,preparing,"0,1"\r\n',
        ]
        assert result == expectation
