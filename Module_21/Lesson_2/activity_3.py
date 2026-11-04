# Define a class
class pair_elements:

    def twoSum(self, numbers, target):
        # Create an empty dictionary
        positions = {}

        # Check each number in the tuple
        for index, number in enumerate(numbers):
            if target - number in positions:
                return (positions[target - number], index)

            positions[number] = index

# Get the target sum from the user
total = int(input("Enter the target sum: "))

# Display the matching element indexes
print("First Index = %d, Second Index = %d" % pair_elements().twoSum((10, 20, 30, 40, 50, 60, 70), total))