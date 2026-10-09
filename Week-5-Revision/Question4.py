
# Employee Salary System

employees = {
    "E101": {"name": "Ram", "department": "IT", "salary": 30000},
    "E102": {"name": "Sita", "department": "HR", "salary": 35000},
    "E103": {"name": "Hari", "department": "Sales", "salary": 28000},
    "E104": {"name": "Gita", "department": "Finance", "salary": 40000},
    "E105": {"name": "Amit", "department": "IT", "salary": 45000}
}

def find_employee(employee_id):
    if employee_id not in employees:
        raise KeyError("Employee ID does not exist.")
    return employees[employee_id]

def calculate_yearly_salary(salary):
    return salary * 12

def increase_salary(salary, percentage):
    return salary + (salary * percentage / 100)

employee_id = input("Enter employee ID: ").upper()

try:
    employee = find_employee(employee_id)

    old_salary = employee["salary"]

    print("Employee Name:", employee["name"])
    print("Department:", employee["department"])
    print("Old Monthly Salary:", old_salary)

    percentage = float(input("Enter salary increase percentage: "))

    if percentage < 0:
        raise ValueError("Percentage cannot be negative.")

    new_salary = increase_salary(old_salary, percentage)
    yearly_salary = calculate_yearly_salary(new_salary)

    employee["salary"] = new_salary

    print("New Monthly Salary:", round(new_salary, 2))
    print("New Yearly Salary:", round(yearly_salary, 2))

except KeyError as error:
    print("Error:", error.args[0])

except ValueError:
    print("Error: Enter a valid non-negative number.")
