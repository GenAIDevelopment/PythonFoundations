class Address:
    """This class represents address
    """
    def __init__(self, roadno, area, street, pincode, city):
        self.roadno = roadno
        self.area = area
        self.street = street
        self.pincode = pincode
        self.city = city

    def __str__(self):
        return f"{self.roadno}, {self.street}, {self.area}, {self.city} - {self.pincode}"