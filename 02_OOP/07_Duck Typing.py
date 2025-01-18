#"Duck typing" = Another way to achieve polymorphism besides Inheritance 
#               Object must have the minimum necessary attributes/methods 
#               "If it looks like a duck and quacks like a duck, it must be & duck.”

# Class representing a Dog
class Dog:
    def speak(self):
        return "Woof"

# Class representing a Cat
class Cat:
    def speak(self):
        return "Meow"

# Class representing a Bird
class Bird:
    def speak(self):
        return "Chirp"

# Function that expects an object that can 'speak'
def animal_speak(animal):
    print(animal.speak())

# Create instances of different animal classes
dog = Dog()
cat = Cat()
bird = Bird()

# Call the same method on different objects (duck typing in action)
animal_speak(dog)   # Output: Woof
animal_speak(cat)   # Output: Meow
animal_speak(bird)  # Output: Chirp
