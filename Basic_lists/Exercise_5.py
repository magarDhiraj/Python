# Exercise 5: Find Values in a List
numbers = [12, 5, 8, 20, 15, 3, 10]
# Asks the user to enter a number  
user_input = int(input("Enter a number: "))
# Check whether the number is in the list
if user_input in numbers:
    print(f"{user_input} is present in the list.")
else:
    print(f"{user_input} is not present in the list.")
    