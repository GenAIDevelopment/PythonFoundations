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

if __name__ == "__main__":
    # read from file into inventory
    
    # dell_keyboard = Product(1,"Dell-Keyboard", 450,10)
    # print(dell_keyboard)
    # try:
    #     dell_keyboard.sale(100)
    # except OutOfStockException:
    #     print(f"The current stock available is {dell_keyboard.quantity}")
    #     print("So sale not processed")
    # print(dell_keyboard)
    create_inventory(add_item_to_inventory)
    sell_item()

    # writing to a file
    for id, product in inventory.items():
        with open("inventory","w") as file:
            file.write(str(product))




