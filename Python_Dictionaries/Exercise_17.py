# Exercise 17: Count Items Using a Dictionary
fruits = [
    "apple", "banana", "apple",
    "orange", "banana", "apple",
    "mango", "orange", "banana"
]

fruit_count = {}

for fruit in fruits:
    if fruit in fruit_count:
        fruit_count[fruit] += 1
    else:
        fruit_count[fruit] = 1

print("Fruit counts:", fruit_count)