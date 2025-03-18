class Product:
    def __init__(self, id: str, name:str, price:float, quantity: int):
        """Initializer

        Args:
            id (str): _description_
            name (str): _description_
            price (float): _description_
            quantity (int): _description_
        """
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
    
    @staticmethod
    def create(line):
        if line.startswith("id,name,price,quantity"):
            return None
        details = line.split(",")
        return Product(details[0],details[1],details[2], details[3])


    def sale(self,count:int):
        """Sale

        Args:
            count (int): _description_

        Raises:
          OutOfStockException when sale count is greater than existing stock
        """
        if self.quantity < count:
            raise OutOfStockException("We dont't have enough stock")
        self.quantity -= count

    def purchase(self,count: int):
        """Purchase

        Args:
            count (int): _description_
        """
        self.quantity += count

    def __str__(self):
        return f"{self.id},{self.name},{self.price},{self.quantity}"
        

class OutOfStockException(Exception):
    pass