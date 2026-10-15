from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# Get student details
name = input("Enter student's name: ")
marks = float(input("Enter student's marks: "))

# Display the student's name in cyan
print(Fore.CYAN + f"Student Name: {name}")

# Check whether the student has passed
if marks >= 40 and marks <= 100:
    print(Fore.GREEN + "Result: PASS")
elif marks < 40 and marks >= 0:
    print(Fore.RED + "Result: FAIL")
else:
    print(Fore.RED + "Please enter marks between 0 and 100.")

# Display marks
print(Style.RESET_ALL + f"Marks: {marks}")
