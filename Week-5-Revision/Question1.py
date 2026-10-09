# Student Result System

students = [
    {"name": "Ram", "marks": [80, 75, 90]},
    {"name": "Sita", "marks": [85, 90, 88]},
    {"name": "Hari", "marks": [70, 65, 75]},
    {"name": "Gita", "marks": [92, 89, 95]},
    {"name": "Amit", "marks": [60, 70, 80]}
]

def calculate_total(marks):
    return sum(marks)

def calculate_percentage(total):
    return (total / 300) * 100

name = input("Enter student name: ")

try:
    student = next(
        s for s in students
        if s["name"].lower() == name.lower()
    )

    marks = student["marks"]

    if len(marks) < 3 or any(m is None for m in marks):
        raise ValueError("A subject mark is missing.")

    total = calculate_total(marks)
    percentage = calculate_percentage(total)

    print("\nStudent Name:", student["name"])
    print("Total Marks:", total, "/ 300")
    print("Percentage:", round(percentage, 2), "%")

except StopIteration:
    print("Error: Student does not exist.")

except (ValueError, TypeError) as error:
    print("Error:", error)