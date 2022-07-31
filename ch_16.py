# Question:
# Use a list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers.
# >Suppose the following input is supplied to the program:

# 1,2,3,4,5,6,7,8,9

# Then, the output should be:

# 1,9,25,49,81
lst = list(map(int, input().split(",")))

new_lst = [num**2 for num in lst if num % 2 != 0]

print(new_lst)
