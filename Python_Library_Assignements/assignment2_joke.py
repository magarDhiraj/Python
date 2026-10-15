import sys

sys.stdout.reconfigure(encoding="utf-8")

# Ask for the user's name
name = input("Enter your name: ")

# Display a welcome message
print(f"Hello {name}! 😄")

# Ask for the favorite activity
activity = input("What is your favorite activity? ")

# Display a personalized message
print(f"Your favorite activity is {activity}!")
print("Keep learning Python! 👍")
