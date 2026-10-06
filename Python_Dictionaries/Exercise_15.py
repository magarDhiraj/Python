# Exercise 15: Check if a Key Exists
student = {
    "name": "Hari",
    "age": 19,
    "course": "Python",
    "city": "Lalitpur"
}

key = input("Enter a key: ")

if key in student:
    print(key, "exists in the dictionary.")
else:
    print(key, "does not exist in the dictionary.")
    