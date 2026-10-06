# Exercise 19: Simple Student Database
students = {
    101: {
        "name": "Ram",
        "age": 20,
        "course": "Python"
    },
    102: {
        "name": "Sita",
        "age": 21,
        "course": "Java"
    },
    103: {
        "name": "Hari",
        "age": 19,
        "course": "Python"
    }
}

print("All students:")
for student_id, details in students.items():
    print(student_id, "->", details)

print("\nDetails of student 102:")
print(students[102])

students[103]["course"] = "Data Science"

students[104] = {
    "name": "Gita",
    "age": 20,
    "course": "JavaScript"
}

del students[101]

print("\nFinal student dictionary:")
for student_id, details in students.items():
    print(student_id, "->", details)

# Challenge: search by student ID
try:
    search_id = int(input("\nEnter a student ID to search: "))

    if search_id in students:
        print("Student information:", students[search_id])
    else:
        print("Student ID not found.")
except ValueError:
    print("Please enter a valid student ID.")
    