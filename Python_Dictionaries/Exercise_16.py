# Exercise 16: Student Marks Dictionary
marks = {
    "Ram": 75,
    "Sita": 88,
    "Hari": 65,
    "Gita": 92,
    "John": 55
}

print("Students and marks:")
for name, mark in marks.items():
    print(name, "-", mark)

total = sum(marks.values())
average = total / len(marks)
highest_mark = max(marks.values())
lowest_mark = min(marks.values())
highest_student = max(marks, key=marks.get)

print("Total marks:", total)
print("Average marks:", average)
print("Highest mark:", highest_mark)
print("Lowest mark:", lowest_mark)
print("Student with highest mark:", highest_student)