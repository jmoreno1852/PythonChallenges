# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

# Suppose the following input is supplied to the program:

# 7
# Then, the output should be:

# 0
# 7
# 14

class MyGen():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        while MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            if num % 7 == 0:
                return num
        raise StopIteration


for num in MyGen(0, 100):
    print(num)

    # def ft_generator(num):
    # for i in range(0,n+1):
    #     yield 1
