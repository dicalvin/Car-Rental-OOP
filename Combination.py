#Vehicle Class
class Vehicle:
    def __init__(self, color):
        self.color = color

    def getColor(self):
        return self.color
    
    def __str__(self):
        return f"The color of the vehicle is {self.color}"
    
#Example
print("\nVehicle Class")
car1 = Vehicle("Silver")
print(car1)

#Car Class
class Car(Vehicle):
    def __init__(self, color, winterTyres = False):
        super().__init__(color)
        self.winterTyres = winterTyres

    def __str__(self):
        return super().__str__() + f"\nhas winter tyres: {self.winterTyres}"
    
#Example
print("\n Car Class")
car2 = Car("Blue", True)
print(car2)

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

#Garage Class
class Garage:
    def __init__(self):
        self.parkedVehicle = None
    
    def setVehicle(self, parked):
        self.parkedVehicle = parked

    def __str__(self):
        return "Description of the parked vehicle ... \n" + (str(self.parkedVehicle) if self.parkedVehicle else "No vehicle parked")
    
#Example
print("\nGarage class")
garage = Garage()
garage.setVehicle(car2)
print(garage)

#GarageTester Class
print("\nGarage Tester Class")
class GarageTester:
    @staticmethod
    def getExample():
        truck = Truck("Black")
        garage = Garage()
        garage.setVehicle(truck)
        print(garage)

#Example
GarageTester.getExample()

#Customer Class
class Customer:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def getName(self):
        return self.name
    def getLocation(self):
        return self.location
    
#Example
print("\nCustomer Class")
customer = Customer("Coco Jones", "Mutungo, Kampala")
print(customer.getName())
print(customer.getLocation())