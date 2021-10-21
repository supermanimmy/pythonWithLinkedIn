# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book:
    # init function initialises the class with info, called before any other function
    # not the same as constructor in java, the object is already created when this object is called
    def __init__(self, title):
        self.title = title

# TODO: create instances of the class
b1 = Book('Brave New World')
b2 = Book('War and Peace')

# TODO: print the class and property
print(b1)
print(b1.title)
