# String formatters in Python are used to create formatted strings by embedding variables and expressions within string literals. They are essential in production-grade code for creating readable, maintainable, and efficient string outputs, especially when dealing with user interfaces, logging, and data presentation.

#method 1: using % operator
name = "akash"
age = 25

# s is for string and d is for integer
print("Name: %s, Age: %d" % (name, age))

#method 2: using format() method
# {} is for placeholder for variables
print("Name: {}, Age: {}".format(name, age))

#method 3: using f-string 
# modern way to format strings in python
print(f"Name: {name}, Age: {age}")

'''
practical use case in production grade code: 

String formatters are used to create informative log messages that include variable data.


'''


