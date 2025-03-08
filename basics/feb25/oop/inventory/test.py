"""We will learn how to create objects and use them
"""
from product import Product

if __name__ == "__main__":
    products = []
    # create an object for a product which is natraj pencil
    natraj_pencil = Product(
        id=1,
        name="Natraj Pencil",
        price=5,
        quantity=100)
    # lets sell pencils
    print(f"The current quantity before sale is {natraj_pencil.quantity}")
    natraj_pencil.sale(10)
    print(f"The current quantity after sale is {natraj_pencil.quantity}")

    print(f"The current quantity before purchase is {natraj_pencil.quantity}")
    natraj_pencil.purchase(30)
    print(f"The current quantity after purchase is {natraj_pencil.quantity}")

    products.append(natraj_pencil)

    # create an object for a product which is natraj pencil
    apsara_pencil = Product(2, "Apsara Pencil",6,1000)
    # lets sell pencils
    print(f"The current quantity before sale is {apsara_pencil.quantity}")
    apsara_pencil.sale(10)
    print(f"The current quantity after sale is {apsara_pencil.quantity}")

    print(f"The current quantity before purchase is {apsara_pencil.quantity}")
    apsara_pencil.purchase(30)
    print(f"The current quantity after purchase is {apsara_pencil.quantity}")

    products.append(apsara_pencil)

    for product in products:
        print(product.name)
        print(product.quantity)

