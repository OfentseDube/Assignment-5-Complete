class Device:
    def __init__(self, brand, model, year):
        self._brand = brand  # Encapsulated attribute
        self._model = model  # Encapsulated attribute
        self._year = year    # Encapsulated attribute
    
    def get_info(self):
        return f"Brand: {self._brand}, Model: {self._model}, Year: {self._year}"
    
    def power_on(self):
        return "Device is powering on..."

class Smartphone(Device):
    def __init__(self, brand, model, year, os, storage, ram):
        super().__init__(brand, model, year)
        self._os = os
        self._storage = storage
        self._ram = ram
        self._battery_level = 100
    
    def get_info(self):  # Polymorphism - overriding parent method
        return f"{super().get_info()}, OS: {self._os}, Storage: {self._storage}GB, RAM: {self._ram}GB"
    
    def power_on(self):  # Polymorphism - overriding parent method
        return "Smartphone is booting up..."
    
    def check_battery(self):
        return f"Battery level: {self._battery_level}%"
    
    def charge(self, percentage):
        if self._battery_level + percentage <= 100:
            self._battery_level += percentage
            return f"Charged to {self._battery_level}%"
        else:
            self._battery_level = 100
            return "Battery fully charged"
    
    def use_battery(self, percentage):
        if self._battery_level - percentage >= 0:
            self._battery_level -= percentage
            return f"Battery level: {self._battery_level}%"
        else:
            self._battery_level = 0
            return "Battery depleted"

# Example usage
if __name__ == "__main__":
    # Create a smartphone instance
    my_phone = Smartphone("Samsung", "Galaxy S23", 2023, "Android", 256, 8)
    
    # Demonstrate polymorphism
    print(my_phone.get_info())  # Uses Smartphone's get_info method
    print(my_phone.power_on())  # Uses Smartphone's power_on method
    
    # Demonstrate encapsulation and methods
    print(my_phone.check_battery())
    print(my_phone.charge(30))
    print(my_phone.use_battery(50))
    print(my_phone.check_battery()) 