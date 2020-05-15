#parent class 1
class item():
    def __init__(self, sku):
        self.sku = sku

    def print_sku(self):
        print("The SKU is {}".format(self.sku))

#parent class 2
class garment():
    def __init__(self, section, type):
        self.section = section
        self.type = type

    def print_garment(self):
        print("The garment is in section {}, {}.".format(self.section, self.type))

#child class
class Shirts(item, garment):
    def __init__(self, sku, section, type, name, color):
        self.name = name
        self.color = color
        item.__init__(self, sku)
        garment.__init__(self, section, type)

    def print_Shirts(self):
        print("{} {} on sale!".format(self.name, self.color))


Blouse = Shirts("0004", 43, "Tops", "Formal Blouse", "White")

Blouse.print_sku()
Blouse.print_garment()
Blouse.print_Shirts()

