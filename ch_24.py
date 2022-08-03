# Question:
# Python has many built-in functions, and if you do not know how to use it,
# you can read document online or find some books.
# But Python has a built-in document function for every built-in functions.

# Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()

# And add document for your own function
print(int.__doc__)
print(str.__doc__)


def square(num):
    '''
    num -> any number
    input must be integer
    return num**2
    '''
    return num**2


print(square(5))
print(square.__doc__)
