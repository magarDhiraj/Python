# Exercise 13: Remove Dictionary Items
employee = {
    "name": "John",
    "age": 30,
    "department": "IT",
    "salary": 50000,
    "city": "Kathmandu"
}

employee.pop("age")
employee.pop("city")

print("After removing age and city:", employee)

# Safely try to remove email
removed_value = employee.pop("email", None)

if removed_value is None:
    print("The 'email' key does not exist, so nothing was removed.")