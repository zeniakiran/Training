# Define the class
class Parrot:

    # Shared class attribute
    species = "bird"

    # Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create objects
parrot1 = Parrot("Blu", 10)
parrot2 = Parrot("Woo", 15)

# Display class attributes
print("Blu belongs to the {}".format(parrot1.species))
print("Woo also belongs to the {}".format(parrot2.species))

# Display instance attributes
print("{} is {} years old".format(parrot1.name, parrot1.age))
print("{} is {} years old".format(parrot2.name, parrot2.age))