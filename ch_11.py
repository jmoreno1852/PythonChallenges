# Question
# Write a program which accepts a sequence of comma separated 4 digit binary numbers
# as its input and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.

# Example:

# 0100,0011,1010,1001,1111

# Then the output should be:

# 1010

# Notes: Assume the data is input by console.


bin_list = input().split(",")
dec_list = list(map(lambda num: int(num, 2), bin_list))
check_list = list(filter(lambda num: num % 5 == 0, dec_list))
final_list = list(map(lambda num: str(bin(num))[2:], check_list))
print(" ".join(final_list))
