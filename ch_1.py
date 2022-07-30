# Question:
# Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def chall_one(item):
    return if item % 7 == 0 and item % 5 != 0


new_list = list(filter(chall_one, range(2000, 3200)))
print(new_list)
