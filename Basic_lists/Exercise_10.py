# Exercise 10: Student Marks List
marks = [75, 82, 68, 90, 55, 88, 72, 95]

print("All marks:", marks)
print("Total marks:", sum(marks))
print("Average marks:", sum(marks) / len(marks))
print("Highest mark:", max(marks))
print("Lowest mark:", min(marks))

count_75_or_more = sum(1 for mark in marks if mark >= 75)
print("Students scoring 75 or more:", count_75_or_more)

marks.sort(reverse=True)
print("Marks highest to lowest:", marks)

# Challenge: add another student's mark
choice = input("Do you want to add another student's mark? (y/n): ").lower()

if choice == "y":
    try:
        new_mark = int(input("Enter the new student's mark: "))
        marks.append(new_mark)

        print("\nUpdated marks:", marks)
        print("Updated total:", sum(marks))
        print("Updated average:", sum(marks) / len(marks))
        print("Updated highest:", max(marks))
        print("Updated lowest:", min(marks))
    except ValueError:
        print("Invalid mark. Please enter an integer.")