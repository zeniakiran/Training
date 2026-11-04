# Define a class
class Employee:

    # Initialize the object
    def __init__(self):
        print("New employee added!")

    # Destructor method
    def __del__(self):
        print("Employee object destroyed")

def Create_obj():
    print("Creating an object...")
    employee = Employee()
    print("Function completed...")
    return employee

print("Calling the Create_obj() function...")
employee_obj = Create_obj()
print("Program finished!")