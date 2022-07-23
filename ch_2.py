# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8
# Then, the output should be:40320
def chall_two(num):
    solution = 1
    try:
        if type(num) != int:
            raise AttributeError
        elif num < 0:
            raise ValueError
    except AttributeError:
        print('Insert an integer')
    except ValueError:
        print("Insert a number > 0")
    else:

        if num == 0:

            return 1

        else:
            while num > 0:
                solution *= num
                num = num-1
            return solution


print(chall_two(8))
