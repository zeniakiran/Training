# Import required modules
from abc import ABC, abstractmethod

# Define the parent class
class Animal(ABC):

    # Declare an abstract method
    # Each child class must provide its own version
    @abstractmethod
    def move(self):
        pass

# Define child classes
class Human(Animal):

    def move(self):
        print("I can walk and jump")

class Snake(Animal):

    def move(self):
        print("I can slither")

class Dog(Animal):

    def move(self):
        print("I can bark and run")

class Lion(Animal):

    def move(self):
        print("I can roar loudly")

# Create objects and call methods
person = Human()
person.move()

snake1 = Snake()
snake1.move()

dog1 = Dog()
dog1.move()

lion1 = Lion()
lion1.move()