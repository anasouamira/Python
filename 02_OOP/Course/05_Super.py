# super() = Function used in a child class to call methods from a parent class (superclass).
#           I Allows you to extend the functionality of the inherited methods

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal {self.name} created")

    def speak(self):
        print(f"{self.name} makes a sound")

# Child class inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        # Using super() to call the parent class constructor
        super().__init__(name)  # This calls Animal.__init__(self, name)
        self.breed = breed
        print(f"Dog {self.name} of breed {self.breed} created")

    def speak(self):
        # Using super() to call the parent class method
        super().speak()  # This calls Animal.speak(self)
        print(f"{self.name} barks")

# Create an object of Dog class
dog = Dog("Buddy", "Golden Retriever")

# Call the speak method of the Dog class (which calls the parent method)
dog.speak()
