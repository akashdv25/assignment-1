# Decorators in Python are a powerful and flexible way to modify the behavior of functions or classes. They allow you to wrap another function in order to extend or alter its behavior without permanently modifying it.

# How Decorators Work
# A decorator is a function that takes another function as an argument, adds some functionality, and returns a new function.


def decorator_function(add):
    def wrapper():
        print("initializing addition")
        print(add())
        print("Execution done")
    return wrapper



@decorator_function
def add():
    return 4 + 5

''' 
# Decorator Function: decorator_function takes the add function as an argument and returns the wrapper function.
# Wrapper Function: Inside wrapper, it prints "initializing addition", then calls add() and prints its return value, and finally prints "Execution done".
# Decorated Function: The @decorator_function decorator replaces add with wrapper, so when you call add(), you are actually calling wrapper().
# Output: When add() is called in the if __name__ == "__main__": block, the following happens:
# "initializing addition" is printed.
#  add() is called, which returns 9, and this value is printed.
# "Execution done" is printed.
''' 


'''
Practical use of decorators
*Logging
*Caching
*Flask routes handling

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Home Page!"

'''








if __name__ == "__main__":
    add()