# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.

# Suppose the following input is supplied to the program:

# hello world! 123

# Then, the output should be:

# LETTERS 10

# DIGITS 3


intcont = 0
charcont = 0
lst = input()
for element in lst:
    if element.isalpha():
        charcont += 1
    elif element.isdigit():
        intcont += 1
print(f"LETTERS {charcont}")
print(f"DIGITS {intcont}")
