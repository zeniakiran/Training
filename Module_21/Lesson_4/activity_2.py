# Define a class
class Computer:

    # Initialize the computer price
    def __init__(self):
        self.__maxprice = 900

    # Display the selling price
    def sell(self):
        print("Computer Price: {}".format(self.__maxprice))

    # Update the maximum price
    def setMaxPrice(self, price):
        self.__maxprice = price

# Create an object
computer1 = Computer()
computer1.sell()

# Try to change the private price directly
computer1.__maxprice = 1200
computer1.sell()

# Change the price using the setter method
computer1.setMaxPrice(1200)
computer1.sell()