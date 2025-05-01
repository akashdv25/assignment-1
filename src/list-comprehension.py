# List comprehension provides a compact way to process all or part of the elements in a sequence and return a list with the results.
# The syntax is:

# [expression for item in iterable if condition]

# expression: The expression to evaluate and include in the new list.
# for item in iterable: Iterates over each item in the iterable.
# if condition: An optional condition to filter items.

import time

"""
List comprehensions are generally faster than traditional loops because they are optimized for performance in Python.
"""


def looping():
    time_start = time.time()
    # Example: Create a list of squares using a loop vs. list comprehension
    squares_loop = []

    for x in range(100000000):
        squares_loop.append(x**2)
    time_end = time.time()
    return f"Time taken to create list of squares using loop: {time_end - time_start} seconds"


print(looping())


def comprehension():
    time_start = time.time()
    squares_comprehension = [x**2 for x in range(100000000)]
    time_end = time.time()
    return f"Time taken to create list of squares using list comprehension: {time_end - time_start} seconds"


print(comprehension())

# it can also be used to filter elements if the condition is true
# Example: Create a list of even numbers from 1 to 10
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)


lists = ["None" if x % 2 == 0 else x for x in range(10)]
print(lists)
