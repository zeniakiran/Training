import matplotlib.pyplot as plt

students_names = ["sanjay", "Rahul", "Karan", "Wasim", "Ramesh", "Ajay", "Sartaj", "Priya"]
students_marks = [35, 50, 20, 45, 25, 40, 25, 40] # total = 50

# Calculate percentage
marks_perc = []
for x in students_marks:
    res = (x / 50) * 100 # obtained marked/total * 100
    marks_perc.append(res)

print(marks_perc)

# Line chart
def marks_line_chart():
    plt.plot(students_names, students_marks)
    plt.title("Students Marks Graph")
    plt.xlabel("Names")
    plt.ylabel("Marks")
    plt.show()

marks_line_chart()

# Bar chart
def percentage_bar_chart():
    plt.title("Students Percentage Graph")
    plt.xlabel("Names")
    plt.ylabel("Percentage")

    plt.bar(students_names, marks_perc)
    plt.show() # showing one graph

    plt.pie(marks_perc, labels=students_names, autopct='%1.1f%%')
    plt.show()

percentage_bar_chart()
