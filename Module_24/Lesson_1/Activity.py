import numpy as np 
data_type = [
    ("name", "S15"), 
    ("class", int)
]

# unorganized information / raw information
student_details = [
    ("Ali", 6), 
    ("fatima", 7), 
    ("Aqsa", 4) 
]

students = np.array(student_details, data_type)

sorted_Array = np.sort(students, order="name")

print("Sorted Array :")
print(sorted_Array)