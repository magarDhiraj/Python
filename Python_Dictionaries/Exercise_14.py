# Exercise 14: Dictionary Keys and Values
book = {
    "title": "Python Basics",
    "author": "John Smith",
    "year": 2025,
    "price": 500
}

print("All keys:", book.keys())
print("All values:", book.values())
print("All key-value pairs:", book.items())

print("\nDictionary details:")
for key, value in book.items():
    print(f"{key} = {value}")