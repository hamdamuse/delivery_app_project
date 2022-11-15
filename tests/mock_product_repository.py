from unittest.mock import Mock, patch, mock_open
from io import StringIO
import csv

class AbstractRepository:
    pass

class TestMockProductRepository(AbstractRepository):
    
    def test_add_single_product(self):
        mock_products_csv = StringIO()
        mock_products_csv.seek(0)
        fieldnames = ["name", "price"]
        writer = csv.DictWriter(mock_products_csv, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({"name": "coke zero", "price": 0.8})
        mock_products_csv.seek(0)
        result = mock_products_csv.readlines()
        expected = ['name,price\r\n', 'coke zero,0.8\r\n']
        assert result == expected

    def test_add_multiple_products(self):
        mock_products_csv = StringIO()
        mock_products_csv.seek(0)
        fieldnames = ["name", "price"]
        writer= csv.DictWriter(mock_products_csv, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({"name": "latte", "price": 3.2})
        writer.writerow({"name": "7up", "price": 0.8})
        mock_products_csv.seek(0)
        result = mock_products_csv.readlines()
        expectation = ['name,price\r\n', 'latte,3.2\r\n','7up,0.8\r\n']
        assert result ==expectation

    def test_add_product_with_incorrect_format(self):
        pass

    def test_read_from_mock_csv(self):
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

    def test_read_non_csv_filetype(self):
        product_list = []
        try:
            with patch('builtins.open', mock_open(read_data=["name","price","coke zero", 0.8])) as mock_opened_file:
                with open("mock_products_csv", "r") as file:
                    csv_file = csv.DictReader(file)
                    for row in csv_file:
                        product_list.append(row)
                        break
        except TypeError:
            print("Type Error: Make sure input is a csv file. Product list is empty")
        result = product_list
        expectation = []
        assert result == expectation

    



        




    

    
        
    
    
    
    # def test_get_multiple_products(self):
         
    #         with patch.dict(mock_products, {"name": "Coke Zero", "price": 1.00}) as patched_products_csv:
    #             assert mock_products == {"name": "Coke Zero", "price": 1.00}
    #         assert mock_products == {}

