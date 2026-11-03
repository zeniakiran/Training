# PART 1: Store student names and scores
scores = {
    "Ali": 85,
    "Sara": 92,
    "Ahmed": 78,
    "Zoya": 95,
    "Hamza": 88
}

print("Student Scores:", scores)

# PART 2: Calculate the total marks using a loop
total = 0

for marks in scores.values():
    total = total + marks

average = total / len(scores)
print("Class Average:", average)

# PART 3: Find the student with the highest score
top_student = ""
highest_score = 0

for name, marks in scores.items():
    if marks > highest_score:
        highest_score = marks
        top_student = name

print("Top Scorer:", top_student)
print("Highest Score:", highest_score)

# PART 4: Search for a student's score
search_name = input("Enter a student name to find their score: ")

if search_name in scores:
    print(search_name, "scored", scores[search_name], "marks.")
else:
    print("Student not found!")

# PART 5: Display the final class report
print("")
print("===== CLASS SCORE REPORT =====")
print("Total Students:", len(scores))
print("Class Average:", average)
print("Top Student:", top_student)
print("Top Score:", highest_score)
print("==============================")