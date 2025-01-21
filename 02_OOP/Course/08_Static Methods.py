# Instance methods = Best for operations on instances of the class (objects) 
# Static methods = Best for utility functions that do not need access to class data 

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand  # Instance variable
        self.model = model  # Instance variable

    # Instance method (requires self)
    def display_info(self):
        return f"Vehicle Brand: {self.brand}, Model: {self.model}"

    # Static method (does not require self or cls)
    @staticmethod
    def is_motorized(vehicle_type):
        motorized_types = ['car', 'motorcycle', 'truck']
        if vehicle_type.lower() in motorized_types:
            return True
        return False


# Create an instance of Vehicle
vehicle = Vehicle("Toyota", "Camry")

# Calling the instance method
print(vehicle.display_info())  # Output: Vehicle Brand: Toyota, Model: Camry

# Calling the static method directly from the class
print(Vehicle.is_motorized("car"))  # Output: True
print(Vehicle.is_motorized("bicycle"))  # Output: False

# Calling the static method from the instance (not typical, but possible)
print(vehicle.is_motorized("truck"))  # Output: True
