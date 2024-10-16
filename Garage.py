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
