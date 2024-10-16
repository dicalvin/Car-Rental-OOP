class Truck(Vehicle):
    def __init__(self, color, trailer=False):
        super().__init__(color)
        self.trailer = trailer

    def __str__(self):
        return super().__str__() + f"\nhas trailer: {self.trailer}"
    
#Example
print("\nTruck Class")
truck = Truck("Brown", False)
print(truck)