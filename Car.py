class Car(Vehicle):
    def __init__(self, color, winterTyres = False):
        super().__init__color(color)
        self.winterTyres = winterTyres

    def __str__(self):
        return super().__str__() + f"\nDoes it have winter Tyres: {self.winterTyres}"
    
car2 = Car("Silver", True)
print(car2)