# PART 1: Define the parent class with common family features
class FamilyMember:
    def __init__(self, eye_color, height_cm):
        self.eye_color = eye_color
        self.height_cm = height_cm

    def display_traits(self):
        print("Eye Colour:", self.eye_color)
        print("Height:", self.height_cm, "cm")

# PART 2: Create a child class using inheritance
class Kid(FamilyMember):

    # PART 3: Initialize the child's information
    def __init__(self, name, age, eye_color, height_cm):
        self.name = name
        self.age = age
        super().__init__(eye_color, height_cm)

    # PART 4: Override the parent method
    def display_traits(self):
        print("Child Name:", self.name)
        print("Child Age:", self.age)
        super().display_traits()

    # PART 5: Create an additional method for Kid
    def show_hobby(self, hobby):
        print(self.name, "enjoys", hobby)

# PART 6: Create an object
kid1 = Kid("Sara", 9, "black", 135)

# PART 7: Display details and hobby
kid1.display_traits()
kid1.show_hobby("reading")

# PART 8: Check the inheritance relationship
print("Is Kid derived from FamilyMember?", issubclass(Kid, FamilyMember))