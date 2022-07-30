# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as
# the value of a.

# Suppose the following input is supplied to the program:

# 9

# Then, the output should be:

# 11106

# Hints:
# In case of input data being supplied to the question,
# it should be assumed to be a console input.

a = int(input())
aa = a*10+a
aaa = aa*10+a
aaaa = aaa*10+a
suma = a+aa+aaa+aaaa
print(suma)
