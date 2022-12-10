class Product(object):
    pass

class Inventory(object):
    def __init__(self):
        self.items = []
        self.test = "abc"
    
    def add_new_item(self, product):
        if type(product) == Product:
            # self.items.append(product)
            self.__items.append(product)
            '''
            마음대로 접근해서 객체 수정을 못하도록 함
            '''
            print("new item added")
        else:
            raise ValueError("Invalid Item")

    def get_number_of_itmes(self):
        return len(self.items)

my_inventory = Inventory()
my_inventory.add_new_item(Product())
my_inventory.add_new_item(Product())