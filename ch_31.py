# Question:
# Define a function which can print a dictionary where the keys are numbers between 1 and 20
# (both included) and the values are square of keys.
dic = {}


def ft_printDic():
    dic = {i**2 for i in range(1, 21)}
    print(dic)


ft_printDic()
