class Vehicle:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        pass  # Abstract method to be implemented by subclasses

class Car(Vehicle):
    def move(self):
        print(f"{self.name} is driving 🚗")

class Plane(Vehicle):
    def move(self):
        print(f"{self.name} is flying ✈️")

class Boat(Vehicle):
    def move(self):
        print(f"{self.name} is sailing ⛵")

class Bicycle(Vehicle):
    def move(self):
        print(f"{self.name} is cycling 🚲")

# Example usage
if __name__ == "__main__":
    # Create instances of different vehicles
    car = Car("Toyota")
    plane = Plane("Boeing")
    boat = Boat("Sailboat")
    bicycle = Bicycle("Mountain Bike")

    # Create a list of vehicles
    vehicles = [car, plane, boat, bicycle]

    # Demonstrate polymorphism
    print("Let's see how different vehicles move:")
    for vehicle in vehicles:
        vehicle.move() 