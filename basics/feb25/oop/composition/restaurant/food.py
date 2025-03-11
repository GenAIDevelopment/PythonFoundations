class FoodItem:
    """This represents food item
    """
    def __init__(self,id,name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name}  {self.price}"


class Menu:
    """This represents
    """
    def __init__(self):
        self.items = []

    def add_item(self, food_item):
        """This adds food item

        Args:
            food_item (_type_): _description_
        """
        self.items.append(food_item)

    def get_all_items(self):
        """Get all items of menu
        """
        for item in self.items:
            print(f"{item.name}  {item.price}")
