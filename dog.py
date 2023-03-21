# Style Guide: https://google.github.io/styleguide/pyguide.html#384-classes
class Dog:
    ''' Dog conceptualizes possible attributes and methods that a Dog can have to represent an idea of a Dog through programming

    Attributes:
        name: the name for the Dog
        breed: the breed for the Dog
        age: positive integer age for the Dog
        
    '''

    def __init__(self, given_name, breed, age):
        self.name = given_name
        self.breed = breed
        self.age = age