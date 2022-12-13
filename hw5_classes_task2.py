from hw5_classes_task1 import Item


class Phone(Item):
    def __init__(self, name, price, quantity, broken_phones):
        super().__init__(name, price, quantity)
        self.broken_phones = broken_phones

    def __str__(self):
        return f'{__class__.__name__}({self.name}, {self.price}, {self.quantity}, {self.broken_phones})'
