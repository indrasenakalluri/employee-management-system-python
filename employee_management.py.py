import json

FILENAME = "employees.txt"

# Load existing data from file
def load_data():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except:
        return []

# Save data to file
def save_data(employees):
    with open(FILENAME, "w") as file:
        json.dump(employees, file)

# Add employees
def add_employee(employees):
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    salary = input("Enter Salary: ")

    employees.append({
        "id": emp_id,
        "name": name,
        "department": dept,
        "salary": salary
    })

    save_data(employees)
    print("Employee added successfully!\n")

# Display employees
def display_employees(employees):
    if not employees:
        print("No employee records found.\n")
        return

    print("\nEmployee Records:")
    for emp in employees:
        print(f"ID: {emp['id']}, Name: {emp['name']}, "
              f"Dept: {emp['department']}, Salary: {emp['salary']}")
    print()

# Update employee
def update_employee(employees):
    emp_id = input("Enter Employee ID to update: ")

    for emp in employees:
        if emp["id"] == emp_id:
            emp["name"] = input("Enter new name: ")
            emp["department"] = input("Enter new department: ")
            emp["salary"] = input("Enter new salary: ")

            save_data(employees)
            print("Employee updated successfully!\n")
            return

    print("Employee not found.\n")

# Delete employee
def delete_employee(employees):
    emp_id = input("Enter Employee ID to delete: ")

    for emp in employees:
        if emp["id"] == emp_id:
            employees.remove(emp)
            save_data(employees)
            print("Employee deleted successfully!\n")
            return

    print("Employee not found.\n")

# Menu
def menu():
    employees = load_data()

    while True:
        print("==== Employee Management System ====")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. Display Employees")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            update_employee(employees)
        elif choice == "3":
            delete_employee(employees)
        elif choice == "4":
            display_employees(employees)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")

menu()
