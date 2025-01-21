# Inheritance = Allows a class to inherit attributes and methods from another class:
#               Helps with code reusability and extensibility
#               class Child(Parent)

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

# Another child class inheriting from Animal
class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."

# Example usage
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Buddy barks.
print(cat.speak())  # Whiskers meows.
