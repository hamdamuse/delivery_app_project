import test_persistence_layer
from unittest.mock import patch
import pytest
from file_handlers import model


def test_load_products_from_persistence_layer():
    product_list = test_persistence_layer.test_load_products()
    result = product_list
    expectation = [{'name': 'coke zero', 'price': ' 0.8'}, {'name': '7up', 'price': ' 0.8'}]
    assert result == expectation
    return product_list

product_list = test_load_products_from_persistence_layer()

def test_format_products(product_list):
    formatted_product_list = []
    for product in product_list:
        product["price"] = float(product["price"])
        formatted_product_list.append(product)
    result = formatted_product_list
    expectation = [{'name': 'coke zero', 'price': 0.8}, {'name': '7up', 'price': 0.8}]
    assert result == expectation
    


def test_enumerate_product_list(product_list):
    enumerated_list = []
    for index, product in enumerate(product_list):
        enumerated_list.append(f"Index: {index}, product: {product['name']}")
    result = "\n".join(enumerated_list)
    expectation = "Index: 0, product: coke zero\nIndex: 1, product: 7up"
    assert result == expectation
    return result


def test_load_couriers_from_persistence_layer():
    courier_list = test_persistence_layer.test_load_couriers()
    result = courier_list
    expectation = [{'name': 'Bob', 'phone_number': '0789887889'}, {'name': 'Jane', 'phone_number': '0783458075'}]
    assert result == expectation
    return courier_list

courier_list = test_load_couriers_from_persistence_layer()

def test_load_orders_from_persistence_layer():
    order_list = test_persistence_layer.test_load_orders()
    result = order_list
    expectation = [
        {
            "customer_name": "John",
            "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
            "customer_phone": "0789887334",
            "courier": "2",
            "status": "preparing",
            "items": "0,1"
    }]
    assert result == expectation
    return order_list

order_list = test_load_orders_from_persistence_layer()


def test_add_product():
    product_list = [{'name': 'coke zero', 'price': ' 0.8'}, {'name': '7up', 'price': ' 0.8'}]
    with patch("builtins.input", return_value = "latte") as mock_product_name:
        with patch("builtins.input", return_value = 3.2) as mock_product_price:
            new_product = {"name": mock_product_name.return_value, "price": mock_product_price.return_value}
            product_list.append(new_product)
    result = product_list
    expectation = [
        {'name': 'coke zero', 'price': ' 0.8'},
        {'name': '7up', 'price': ' 0.8'},
        {'name': 'latte', 'price':3.2}
        ]
    assert result == expectation
    return product_list

@pytest.fixture
def product_name():
    return "cappuccino"

@pytest.fixture
def product_price():
    return 3.4

@pytest.fixture
def product_list():
    return [
        {'name': 'coke zero', 'price':  0.8},
        {'name': '7up', 'price': 0.8}
        ]

def test_add_product_including_fixtures(product_name, product_price):
    model.add_product(product_list, product_name, product_price)
    result = product_list()
    expectation = [
        {'name': 'coke zero', 'price': ' 0.8'},
        {'name': '7up', 'price': ' 0.8'},
        {'name': "cappucino", 'price': 3.4}
        ]
    assert result == expectation

    

print(product_list)
