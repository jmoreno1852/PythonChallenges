# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters
# and lower case letters.

# Suppose the following input is supplied to the program:

# Hello world!

# Then, the output should be:

# UPPER CASE 1

# LOWER CASE 9

uppercont = 0
lowercont = 0
lst = input()
for element in lst:
    if element.islower():
        lowercont += 1
    elif element.isupper():
        uppercont += 1
print(f"LOWER CASE {lowercont}")
print(f"UPPER CASE {uppercont}")
