# Question:
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

# Suppose the following input is supplied to the program:

# Hello world

# Practice makes perfect

# Then, the output should be:

# HELLO WORLD

# PRACTICE MAKES PERFECT
lst = []

while True:
    inp = input()
    if inp == "":
        break
    lst.append(inp)
for string in lst:
    print(string.upper())
