import random

# Generate random numbers
print(random.random())           # Random float between 0.0 and 1.0
print(random.randint(1, 10))     # Random integer between 1 and 10
print(random.uniform(5.5, 10.5)) # Random float between 5.5 and 10.5

# Random choice and sampling
colors = ["red", "blue", "green", "yellow"]
print(random.choice(colors))       # Randomly choose one element
print(random.sample(colors, 2))    # Randomly choose 2 unique elements
print(random.choices(colors, k=3)) # Randomly choose 3 elements (with replacement)

# Shuffle a list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)  # Output: Shuffled order

# Generate numbers with a normal distribution
print(random.gauss(0, 1))  # Random number with mean 0 and standard deviation 1
