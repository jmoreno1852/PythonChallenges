# Question:
# Define a class, which have a class parameter and have a same instance parameter.

class MyCat():
    name = "Yuuki"

    def __init__(self, name=None):
        self.name = name


Cat = MyCat("Rodrigo")
print(f'My cat\'s name is {Cat.name}')
