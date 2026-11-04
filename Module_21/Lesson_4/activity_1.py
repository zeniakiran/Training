# Define a class
class myClass:

    # Declare a private variable
    __privateVar = 25

    # Create a private method
    def __privMeth(self):
        print("This is a private method inside myClass")

    # Method to display the private variable
    def display(self):
        print("Value of Private Variable:", myClass.__privateVar)

# Create an object and call the method
obj = myClass()
obj.display()
obj.__privMeth()