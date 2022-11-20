from unittest.mock import patch, mock_open

import csv
from io import StringIO



def test_load_products():
    product_list = []
    with patch('builtins.open', mock_open(read_data=
"""name,price
coke zero, 0.8
7up, 0.8""")) as m:
        with open("mock_products_csv", "r") as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                product_list.append(row)
    result = product_list
    expectation = [{'name': 'coke zero', 'price': ' 0.8'}, {'name': '7up', 'price': ' 0.8'}]
    assert result == expectation

def test_load_couriers():
    courier_list = []
    with patch('builtins.open', mock_open(read_data=
"""name,phone_number
Bob,0789887889
Jane,0783458075
""")) as mocked_couriers:
        with open("mock_products_csv", "r") as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                courier_list.append(row)
    result = courier_list
    expectation = [{'name': 'Bob', 'phone_number': '0789887889'}, {'name': 'Jane', 'phone_number': '0783458075'}]
    assert result == expectation


def test_save_products_includes_exception_handling():
    mock_product_list = [{"name": "fanta","price": 0.8}, {"name": "coke", "price":0.8}]
    try:
        with patch("builtins.open", mock_open) as mocked_open:
            with open("mock_products", "w",newline="") as file:
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
        expectation = ["name,price\r\n","fanta,0.8\r\n","coke,0.8\r\n"]


def test_save_products_using_string_IO_object():
    mock_product_list = [{"name": "fanta","price": 0.8}, {"name": "coke", "price":0.8}]
    mock_products_csv = StringIO()
    mock_products_csv.seek(0)
    fieldnames = ["name", "price"]
    writer= csv.DictWriter(mock_products_csv, fieldnames=fieldnames)
    writer.writeheader()
    for product in mock_product_list:
        writer.writerow(product)
    mock_products_csv.seek(0)
    result = mock_products_csv.readlines()
    expectation = ['name,price\r\n', 'fanta,0.8\r\n','coke,0.8\r\n']
    assert result ==expectation

def test_save_products_includes_exception_handling():
    mock_product_list = [{"name": "fanta","price": 0.8}, {"name": "coke", "price":0.8}]
    try:
        with patch("builtins.open", mock_open) as mocked_open:
            with open("mock_products", "w",newline="") as file:
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
        expectation = ["name,price\r\n","fanta,0.8\r\n","coke,0.8\r\n"]