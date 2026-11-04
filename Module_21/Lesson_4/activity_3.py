# Define a class
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Display the point in coordinate format
    def __str__(self):
        return "X: {0}, Y: {1}".format(self.x, self.y)

# Create an object
point1 = Point(5, 7)

# Print the object details
print(point1)