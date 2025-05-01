'''
The __init__.py file is a special Python file used to indicate that a directory should be treated as a Python package.

You can put initialization code in __init__.py that you want to run when the package is imported.


Purpose of __all__:
The __all__ list in a module or package's __init__.py file defines the public interface of that module or package. 
It specifies which attributes, functions, or classes should be accessible when from module import * is used.

Subdirectory __init__.py:
When you import specific functions or classes in a subdirectory's __init__.py and include them in __all__, it allows those
components to be accessible directly from the package level.

Root Directory __init__.py:
At the root level, you can import everything from a subdirectory using from subdirectory import *. This will import all the
components listed in the subdirectory's __all__.


'''