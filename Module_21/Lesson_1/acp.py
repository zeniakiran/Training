# Animal Profile Creator

# PART 1: Define a simple class
class Pet:
    print("Welcome to the pet profile program!")

# PART 2: Create an object
my_pet = Pet()


# PART 3: Define a class with the __init__ method
class PetProfile:

    # Shared class attribute
    category = "animal"

    # Store information about each pet
    def __init__(self, name, animal_type, age, favourite_food):
        self.name = name
        self.animal_type = animal_type
        self.age = age
        self.favourite_food = favourite_food

# PART 4: Create objects
pet1 = PetProfile("Charlie", "Dog", 5, "Chicken")
pet2 = PetProfile("Luna", "Cat", 2, "Milk")

# PART 5: Display class attributes
print("Charlie is an {}".format(pet1.category))
print("Luna is also an {}".format(pet2.category))

# PART 6: Display instance attributes
print("{} is a {} and is {} years old.".format(pet1.name, pet1.animal_type, pet1.age))
print("{} loves eating {}.".format(pet1.name, pet1.favourite_food))

print("{} is a {} and is {} years old.".format(pet2.name, pet2.animal_type, pet2.age))
print("{} loves eating {}.".format(pet2.name, pet2.favourite_food))