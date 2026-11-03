# PART 1: Create two snack boxes using sets
box1 = {"chips", "juice", "cookies", "chips", "apple"}
box2 = {"cookies", "sandwich", "juice", "sandwich"}

print("First Snack Box:", box1)
print("Second Snack Box:", box2)

# PART 2: Add a banana to the first snack box
box1.add("banana")
print("First Box after adding a banana:", box1)

# PART 3: Find common snacks in both boxes
shared_snacks = box1.intersection(box2)
print("Common snacks:", shared_snacks)

# PART 4: Create an array to store snack quantities
import array as arr

snack_array = arr.array('i', [4, 6, 3, 5])
print("Original snack array:", snack_array)

# PART 5: Insert and append new quantities
snack_array.insert(0, 2)
snack_array.append(7)
print("Array after adding new quantities:", snack_array)

# PART 6: Find how many times 5 occurs in the array
five_count = snack_array.count(5)
print("Count of number 5:", five_count)

# PART 7: Reverse the snack array
snack_array.reverse()
print("Snack array in reverse order:", snack_array)

# PART 8: Display the final snack counter report
print("")
print("===== SNACK COUNTER REPORT =====")
print("First Snack Box:", box1)
print("Second Snack Box:", box2)
print("Common Snacks:", shared_snacks)
print("Final Snack Array:", snack_array)
print("================================")