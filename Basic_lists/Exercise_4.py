# Exercise 4: List Slicing
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Using slicing to get a sublist of the first five numbers
first_five = numbers[:5]
print("First five numbers:", first_five)
# Using slicing to get a sublist of the last five numbers
last_five = numbers[-5:]
print("Last five numbers:", last_five)
# Using slicing to get a sublist of numbers from index 2 to 6
middle_numbers = numbers[2:7]
print("Numbers from index 2 to 6:", middle_numbers)
# Using slicing to get every second number from the list
every_second = numbers[::2]
print("Every second number:", every_second)
# Using slicing to get the list in reverse order
reverse_numbers = numbers[::-1]
print("Numbers in reverse order:", reverse_numbers)

