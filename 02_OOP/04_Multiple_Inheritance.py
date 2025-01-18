# First parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

# Second parent class
class Flyer:
    def __init__(self, species):
        self.species = species
    
    def fly(self):
        print(f"{self.species} can fly")

# Child class inheriting from both Animal and Flyer
class Bird(Animal, Flyer):
    def __init__(self, name, species):
        Animal.__init__(self, name)  # Initialize the Animal class
        Flyer.__init__(self, species)  # Initialize the Flyer class

    def speak(self):
        print(f"{self.name} chirps")

# Create an object of the Bird class
bird = Bird("Parrot", "Parrot species")

# Call methods from both parent classes
bird.speak()  # Output: Parrot chirps
bird.fly()    # Output: Parrot species can fly

# Access attributes from both parent classes
print(f"{bird.name} belongs to the {bird.species}.")  # Output: Parrot belongs to the Parrot species.
