# Question:
# Define a class which has at least two methods:

# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class TestClass():
    def __init__(self):
        pass

    def getString(self):
        self.string = str(input("Write something! "))

    def printString(self):
        print(self.string.upper())


def test():
    clase = TestClass()
    clase.getString()
    clase.printString()


test()
