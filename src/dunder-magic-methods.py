# Dunder methods, also known as magic methods or special methods, are a set of predefined methods in Python that you can use to enrich your classes. They are called "dunder" because they have double underscores before and after their names (e.g., __init__, __str__).
# These methods allow you to define the behavior of your objects for built-in operations, such as arithmetic operations, comparisons, and type conversions.

# Dunder methods are defined within a class and are applied to the objects (instances) of that class. They allow you to define how instances of your class should behave with respect to various operations and built-in functions.


# __init__: Called as Constructor , this method defines the attributes that each instance of that particular class will have.
# __str__: This method is used to define the string representation of an object i.e when you print the object what you want to display.
# __repr__: This method is used to define the "official" string representation of an object.
# __len__: This method is used to define the length of an object.
# __getitem__: This method is used to define the behavior of the [] operator.
# __setitem__: This method is used to define the behavior of the []= operator.
# __delitem__: This method is used to define the behavior of the del operator.
# __add__: This method is used to define the behavior of the + operator.
# __sub__: This method is used to define the behavior of the - operator.
# __mul__: This method is used to define the behavior of the * operator.
# __eq__: This method is used to define the behavior of the == operator.
# __ne__: This method is used to define the behavior of the != operator.
# __lt__: This method is used to define the behavior of the < operator.
# __le__: This method is used to define the behavior of the <= operator.
# __gt__: This method is used to define the behavior of the > operator.
# __ge__: This method is used to define the behavior of the >= operator.
# __and__: This method is used to define the behavior of the & operator.
# __or__: This method is used to define the behavior of the | operator.
# __iter__: This method is used to define the behavior of the iter() function.


#Example

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author} - ${self.price}"
    
    def __len__(self):
        return len(self.title)
    
    def __getitem__(self, index):
        return self.title[index]
    
    def __setitem__(self, index, value):
        self.title = self.title.replace(self.title[index], value)

    def __add__(self,value):
        return self.price + value

    def __sub__(self,value):
        return self.price - value
    
    def __mul__(self,value):
        return self.price * value




if __name__ == "__main__":
        
    #lets create an instance of the class
    book_1 = Book("Chota Bheem ke kise", "Tun Tun Mausi", 25)

    print(f'__str__ method: {book_1}')

    print(f"The length of the title is {len(book_1)} characters") #len()

    print(f"The first character of the title is {book_1[0]}")  #get item

    book_1[0] = "Hehehe"  #set item

    print(f"The changed title is {book_1}")

    print(f"The price of the book after adding 10 is {book_1 + 10}") #__add__

    print(f"The price of the book after subtracting 10 is {book_1 - 10}") #__sub__

    print(f"The price of the book after multiplying by 10 is {book_1 * 10}") #__mul__
