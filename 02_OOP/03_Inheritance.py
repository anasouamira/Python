# Inheritance = Allows a class to inherit attributes and methods from another class:
#               Helps with code reusability and extensibility
#               class Child(Parent)

# Parent class
class Animal:
    def __init__(self, name, species):
        self.name = name        # Instance variable
        self.species = species  # Instance variable
    
    def speak(self):
        print(f"{self.name} makes a sound")

# Child class inheriting from Animal
class Dog(Animal):
    def __init__(self, name, species, breed):
        # Call the parent class constructor to initialize name and species
        super().__init__(name, species)
        self.breed = breed      # Additional attribute for Dog
    
    # Overriding the speak method
    def speak(self):
        print(f"{self.name} barks")

# Child class inheriting from Animal
class Cat(Animal):
    def __init__(self, name, species, color):
        # Call the parent class constructor to initialize name and species
        super().__init__(name, species)
        self.color = color      # Additional attribute for Cat
    
    # Overriding the speak method
    def speak(self):
        print(f"{self.name} meows")

# Creating objects of the Dog and Cat classes
dog = Dog("Buddy", "Canine", "Golden Retriever")
cat = Cat("Whiskers", "Feline", "Black")

# Calling the speak method (overridden in child classes)
dog.speak()  # Output: Buddy barks
cat.speak()  # Output: Whiskers meows

# Accessing attributes from the parent class
print(f"{dog.name} is a {dog.species} of breed {dog.breed}")  # Output: Buddy is a Canine of breed Golden Retriever
print(f"{cat.name} is a {cat.species} of color {cat.color}")  # Output: Whiskers is a Feline of color Black
