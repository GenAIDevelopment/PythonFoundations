"""This module will have the entry point of the application
"""
from models.product import Product, OutOfStockException

inventory = dict()


def add_item_to_inventory(product: Product) -> None:
    inventory[product.id] = product

def create_inventory(add_item_to_inventory):
    while True:
        print("Enter the items to be added to inventory")
        id = input("Enter the product id: ")
        name = input("Enter the product name: ")
        price = float(input("Enter the product price: "))
        quantity = int(input("Enter the product quantity: "))
        product = Product(id,name,price,quantity)
        add_item_to_inventory(product)

        choice = input("Do you want to enter other item, Press Y for yes and any other key to exit :")
        if choice.lower() != 'y':
            break

def sell_item():
    id = input("Enter the product id: ")
    quantity = int(input("Enter the items for sale: "))
    product = inventory[id]
    product.sale(quantity)
    inventory[id] = product

def load():
    """This method loads the values from csv file into dictionary
    """
    with open("inventory.csv","r") as inventory_file: 
        for line in inventory_file.readlines():
            product = Product.create(line)
            if product is not None:
                add_item_to_inventory(product)

def save():
    """This method will save all the items in inventory to a file
    """
    with open("inventory.csv","w") as inventory_file:
        inventory_file.write("id,name,price,quantity")
        for product in inventory.values():
            inventory_file.write((str)(product))

if __name__ == "__main__":
    load()
    create_inventory(add_item_to_inventory)
    save()
    sell_item()
    save()




