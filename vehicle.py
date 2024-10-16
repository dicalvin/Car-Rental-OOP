class Vehicle:
    def __init__(self, color):
        self.color = color

    def getColor(self):
        return self.color
    
    def __str__(self):
        return f"The color of the vehicle is {self.color}"
    
#Example
car1 = Vehicle("Silver")
print(car1)