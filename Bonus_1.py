# BONUS 1: LIST AND DICTIONARY TOGETHER
students = ["Ram", "Sita", "Hari", "Gita"]

marks = {
    "Ram": 75,
    "Sita": 88,
    "Hari": 65,
    "Gita": 92
}

for student in students:
    print(student, "-", marks[student])

print("\nStudents who scored 80 or above:")
for student in students:
    if marks[student] >= 80:
        print(student, "-", marks[student])