# Polymorphism = Greek word that means to "have many forms or faces”

#               Poly = Many
#               Morphe = Form

#               THO WAYS TO ACHIEVE POLYMORPHISM
#               1. Inheritance = An object could be treated of the same type as a parent class
#               2. "Duck typing" = Object must have necessary attributes/methods

# Parent class
class Animal:
    def speak(self):
        print("Animal makes a sound")

# Child class 1
class Dog(Animal):
    def speak(self):
        print("Dog barks")

# Child class 2
class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Child class 3
class Cow(Animal):
    def speak(self):
        print("Cow moos")

# Function that demonstrates polymorphism
def animal_sound(animal):
    animal.speak()

# Create objects of different classes
dog = Dog()
cat = Cat()
cow = Cow()

# Call the same method on different objects
animal_sound(dog)  # Output: Dog barks
animal_sound(cat)  # Output: Cat meows
animal_sound(cow)  # Output: Cow moos
