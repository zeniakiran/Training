# Create a class
class IOString():

    # Initialize an empty string
    def __init__(self):
        self.text = ""

    # Get text from the user
    def get_String(self):
        self.text = input("Enter your text: ")

    # Display the text in uppercase
    def print_String(self):
        print("Uppercase Text:", self.text.upper())

# Create an object
string1 = IOString()

# Call the class methods
string1.get_String()
string1.print_String()