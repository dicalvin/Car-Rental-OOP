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