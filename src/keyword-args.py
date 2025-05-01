# Arbitrary Keyword Arguments (**kwargs):
# You can use **kwargs in a function definition to allow the function to accept any number of keyword arguments.
# Inside the function, kwargs is a dictionary containing all the keyword arguments passed to the function.

# we can perform dictionary operations on kwargs


def operations(**kwargs):
    # doctsring
    """
    This function performs various operations on a dictionary of keyword arguments.
    It prints the name, keys, values, items, and the dictionary itself.
    """
    print(kwargs["name"])
    print(kwargs.keys())
    print(kwargs.values())
    print(kwargs.items())
    print(kwargs)

    # we can also use for loop to iterate through the dictionary
    for key, value in kwargs.items():
        print(key, value)


operations(name="akash", age=25, city="Pune")
