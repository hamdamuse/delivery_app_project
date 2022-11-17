# from Repository import Repository
# import csv




# class FileProductRepository(Repository):
#     #at the moment data is hard-coded as the domain layer is yet to be built


#     def save():
#         pass

    

#     def add(self):
#         try:
#             with open("data\products.csv", "a",newline='') as file:
#                 fieldnames = ["name", "price"]
#                 writer = csv.DictWriter(file, fieldnames=fieldnames)
#                 writer.writerow({"name": "fanta", "price":0.8})
#         except FileNotFoundError:
#             print("File not found, please try again.")
#         except TypeError:
#             print("TypeError: Please check input type")
#         except Exception as e:
#             print(f"Error: {str(e)}")

    
#     def list(self):
#         product_list = []
#         try:
#             with open("data\products.csv", "r") as file:
#                 csv_file = csv.DictReader(file)
#                 for row in csv_file:
#                     product_list.append(row)
#         except TypeError:
#             print("Type Error: Make sure input is a csv file. Product list is empty")
#         return product_list

#     def update():
#             products

#     def delete():
#         pass
    


# products_list = FileProductRepository()
# products_list.list()
# products_list.add()