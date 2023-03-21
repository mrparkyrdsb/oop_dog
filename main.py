# Using Dog Class in our code

# import our dog.py to access our Dog Class
from dog import Dog

# Create an instance of a Dog Object
dog1 = Dog('Marshall', 'Westie', 3)
dog2 = Dog('Freya', 'Samoyed', 3)
dog3 = Dog('Goji', 'Mutt', 2)

# Dog Class provides a .bark() method
dog1.bark()
dog2.bark()
dog3.bark()

# Since the Dog Class had __str__() and __repr__() overrides, they are printable
print(dog1)
print(dog2)
print(dog3)