#Iterables = An object/collection that can return its elements one at a time,
#           1 allowing it to be iterated over in a loop

# Function to demonstrate iterable behavior using a for loop
def demonstrate_iterable(iterable):
    print(f"Iterating over: {iterable}")
    for item in iterable:
        print(item)

# Function to demonstrate iter() and next()
def demonstrate_iter_with_next(iterable):
    print(f"\nUsing iter() and next() on: {iterable}")
    iterator = iter(iterable)  # Create an iterator from the iterable
    try:
        while True:
            print(next(iterator))  # Get the next item from the iterator
    except StopIteration:
        print("Iteration complete.")

# Main function to test different iterables
def main():
    # Define some sample iterables
    list_example = [1, 2, 3, 4, 5]
    tuple_example = (10, 20, 30)
    string_example = "Hello"
    dict_example = {"a": 1, "b": 2, "c": 3}

    # Demonstrate iterables using a for loop
    demonstrate_iterable(list_example)
    demonstrate_iterable(tuple_example)
    demonstrate_iterable(string_example)
    demonstrate_iterable(dict_example)

    # Demonstrate iterables using iter() and next()
    demonstrate_iter_with_next(list_example)
    demonstrate_iter_with_next(tuple_example)

# Run the main function
if __name__ == "__main__":
    main()
