# Define the class
class Vehicle:

    # Initialize the class
    def __init__(self, speed, distance):

        # Store the given values
        self.speed = speed
        self.distance = distance

# Create an object
vehicle1 = Vehicle(220, 20)

# Display vehicle details
print("Vehicle Speed:", vehicle1.speed)
print("Vehicle Mileage:", vehicle1.distance)