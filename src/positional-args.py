# Arbitrary Positional Arguments (*args):
# You can use *args in a function definition to allow the function to accept any number of positional arguments.
# Inside the function, args is a tuple containing all the positional arguments passed to the function.


def operations(*args):
    # doctsring
    """
    This function performs various operations on a list of numbers.
    It calculates the minimum, maximum, length, and sum of the numbers.
    It also prints the first and last elements of the list.
    """
    # we can use *args to pass any number of arguments to the function
    print(min(args))
    print(max(args))
    print(len(args))
    print(sum(args))
    print(args[0])
    print(args[-1])

    return "done"


# we can pass any number of arguments to the function and perform tuple operations
print(operations(1, 2, 3, 4, 5))  

# practical use case in production grade code
"""
When you need to call a function with arguments that are determined at runtime, *args and **kwargs can be very useful.
"""

