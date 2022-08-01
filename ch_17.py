# Question 17
# Question:
# Write a program that computes the net amount of a bank account based
# a transaction log from console input.
# The transaction log format is shown as following:

# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:

# D 300
# D 300
# W 200
# D 100
# Then, the output should be:

# 500
wcount = 0
dcount = 0

while True:
    inp = input().upper()
    if inp == "":
        break
    else:
        if inp[0] == "D":
            dcount += int(inp[2:])

        elif inp[0] == "W":
            wcount += int(inp[2:])
        else:
            break

output = dcount - wcount
print(output)
