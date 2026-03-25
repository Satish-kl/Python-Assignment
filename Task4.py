#Mini Project 1: Employee Management System

# Employee Management System

employees = [
    {"name": "Satish Kumar", "age": 28, "role": "Software Engineer", "salary": 50000},
    {"name": "Pavan Kumar", "age": 32, "role": "Manager", "salary": 70000},
    {"name": "Lalita", "age": 26, "role": "Data Analyst", "salary": 45000}
]

# Function to add a new employee
def add_employee():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    role = input("Enter role: ")
    salary = float(input("Enter salary: "))

    emp = {
        "name": name,
        "age": age,
        "role": role,
        "salary": salary
    }

    employees.append(emp)
    print(f"\nEmployee {name} added successfully!\n")


# Function to update an employee
def update_employee():
    name = input("Enter the name of employee to update: ")
    found = False

    for emp in employees:
        if emp["name"].lower() == name.lower():
            found = True
            print(f"\nUpdating employee: {emp['name']}")
            emp["role"] = input("Enter new role: ")
            emp["salary"] = float(input("Enter new salary: "))
            print("Employee updated successfully!\n")
            break

    if not found:
        print(f"No employee found with name '{name}'.\n")


# Function to delete an employee
def delete_employee():
    name = input("Enter the name of employee to delete: ")
    found = False

    for emp in employees:
        if emp["name"].lower() == name.lower():
            found = True
            employees.remove(emp)
            print(f"Employee {name} deleted successfully!\n")
            break

    if not found:
        print(f"No employee found with name '{name}'.\n")


# Function to display all employees
def display_employees():
    if not employees:
        print("No employees to display.\n")
        return

    print(f"{'Name':<20} {'Age':<5} {'Role':<20} {'Salary':<10}")
    print("-" * 60)
    for emp in employees:
        print(f"{emp['name']:<20} {emp['age']:<5} {emp['role']:<20} {emp['salary']:<10}")
    print()


# Main menu
def main():
    while True:
        print("===== Employee Management System =====")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. Display Employees")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            update_employee()
        elif choice == "3":
            delete_employee()
        elif choice == "4":
            display_employees()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Try again.\n")


# Run the Employee Management System
main()

#  Mini Project 2: Student Report Card

# Student Report Card System

def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"


def generate_report(student):
    total = sum(student["marks"])
    average = total / len(student["marks"])
    grade = calculate_grade(average)

    print("\n===== REPORT CARD =====")
    print(f"Name       : {student['name']}")
    print(f"Marks      : {student['marks']}")
    print(f"Total      : {total}")
    print(f"Average    : {average:.2f}")
    print(f"Grade      : {grade}")
    print("========================")


def main():
    # Student data (given)
    student = {
        "name": "Satish Kumar",
        "marks": [99, 99, 99]   # 3 subjects
    }

    generate_report(student)


# Run the program
main()

# Mini Project 3: Shopping Cart System

# Shopping Cart System

cart = []

# Function to add product
def add_product(name, price, quantity):
    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    cart.append(product)
    print(f"{name} added to cart successfully!")

# Function to remove product
def remove_product(name):
    for item in cart:
        if item["name"].lower() == name.lower():
            cart.remove(item)
            print(f"{name} removed from cart.")
            return
    print(f"{name} not found in cart.")

# Function to display cart
def display_cart():
    if not cart:
        print("Cart is empty.")
        return
    
    print("\n===== Shopping Cart =====")
    print(f"{'Name':<15}{'Price':<10}{'Quantity':<10}{'Total':<10}")
    
    total_bill = 0
    for item in cart:
        total = item["price"] * item["quantity"]
        total_bill += total
        print(f"{item['name']:<15}{item['price']:<10}{item['quantity']:<10}{total:<10}")
    
    print("-------------------------------")
    print(f"Total Bill: {total_bill}")

# Adding updated product
add_product("sugar", 18000, 60)

# Display cart
display_cart()

# Mini Project 4: Login & User Validation

# Dictionary to store users: username -> password
users = {
    "satish": "12345",
    "alice": "alice2026",
    "bob": "bob@321"
}

# Function to validate login
def login_system():
    print("===== Login System =====")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if username exists
    if username in users:
        # Check if password matches
        if users[username] == password:
            print(f"Login Successful! Welcome, {username}.")
        else:
            print("Login Failed! Incorrect password.")
    else:
        print("Login Failed! Username not found.")

# Run login system
login_system()

# Mini Project 5: Unique Visitor Counter

# Set to store unique visitor names
unique_visitors = set()

# Function to add a visitor
def add_visitor(name):
    if name in unique_visitors:
        print(f"{name} has already visited.")
    else:
        unique_visitors.add(name)
        print(f"Welcome, {name}! Added to visitor list.")

# Function to display all unique visitors
def display_visitors():
    print("\n===== Unique Visitors =====")
    if not unique_visitors:
        print("No visitors yet.")
    else:
        for visitor in unique_visitors:
            print(visitor)
    print(f"Total unique visitors: {len(unique_visitors)}")

# Example usage
add_visitor("Satish")
add_visitor("Alice")
add_visitor("Bob")
add_visitor("Satish")  # Duplicate, won't be added

# Display all visitors and count
display_visitors()

# Mini Project 6: String Formatter Tool

# Predefined name and product
name = "satish"
product = "sugar"

# Basic formatted sentence
formatted_sentence = f"Hello {name}, you have purchased {product}."
print("\nFormatted Sentence:")
print(formatted_sentence)

# Padded outputs
width = 40  # Total width for padding

print("\nPadded Outputs:")
print("Left padded:   " + formatted_sentence.ljust(width))
print("Right padded:  " + formatted_sentence.rjust(width))
print("Center padded: " + formatted_sentence.center(width))

# Mini Project 7: Bank Account System

# Dictionary to store accounts: account_name -> balance
accounts = {}

# Function to create a new account
def create_account(name, balance):
    if name in accounts:
        print(f"Account already exists for {name}.")
    else:
        accounts[name] = balance
        print(f"Account created for {name} with balance ₹{balance}.")

# Function to deposit money
def deposit(name, amount):
    if name in accounts:
        accounts[name] += amount
        print(f"₹{amount} deposited to {name}'s account. New balance: ₹{accounts[name]}")
    else:
        print(f"No account found for {name}.")

# Function to withdraw money
def withdraw(name, amount):
    if name in accounts:
        if amount <= accounts[name]:
            accounts[name] -= amount
            print(f"₹{amount} withdrawn from {name}'s account. New balance: ₹{accounts[name]}")
        else:
            print("Insufficient balance!")
    else:
        print(f"No account found for {name}.")

# Function to check balance
def check_balance(name):
    if name in accounts:
        print(f"{name}'s account balance: ₹{accounts[name]}")
    else:
        print(f"No account found for {name}.")

# ===== Example =====
create_account("satish", 25000)   # Predefined account
deposit("satish", 5000)           # Example deposit
withdraw("satish", 10000)         # Example withdrawal
check_balance("satish")           # Check final balance

# Mini Project 8: Voting System

# Dictionary to store candidates and their vote counts
votes = {}

# Function to add a candidate (optional)
def add_candidate(name):
    if name in votes:
        print(f"{name} is already a candidate.")
    else:
        votes[name] = 0
        print(f"{name} added as a candidate.")

# Function to cast a vote
def cast_vote(candidate_name):
    if candidate_name in votes:
        votes[candidate_name] += 1
        print(f"Vote casted for {candidate_name}!")
    else:
        print(f"{candidate_name} is not a valid candidate.")

# Function to display the winner
def display_winner():
    if not votes:
        print("No votes cast yet.")
        return
    max_votes = max(votes.values())
    winners = [name for name, v in votes.items() if v == max_votes]
    
    print("\n===== Election Result =====")
    for name, v in votes.items():
        print(f"{name}: {v} votes")
    
    if len(winners) == 1:
        print(f"\nWinner: {winners[0]} with {max_votes} votes!")
    else:
        print(f"\nIt's a tie between: {', '.join(winners)} with {max_votes} votes each!")

# ===== Example Usage =====
add_candidate("Alice")
add_candidate("Bob")
add_candidate("Satish")

# Cast some votes
cast_vote("Alice")
cast_vote("Bob")
cast_vote("Alice")
cast_vote("Satish")
cast_vote("Alice")

# Display final winner
display_winner()

# Mini Project 9: Course Enrollment System

# Dictionary to store students: name -> list of courses
students = {}

# Function to add a new student with courses
def add_student(name, course_list):
    if name in students:
        print(f"Student {name} already exists.")
    else:
        students[name] = course_list
        print(f"Student {name} added with courses: {', '.join(course_list)}")

# Function to update courses for a student
def update_courses(name, new_courses):
    if name in students:
        students[name].extend(new_courses)
        # Remove duplicates if any
        students[name] = list(set(students[name]))
        print(f"Updated courses for {name}: {', '.join(students[name])}")
    else:
        print(f"Student {name} not found.")

# Function to display all students with their courses
def display_students():
    if not students:
        print("No students enrolled yet.")
        return
    print("\n===== Student Enrollment Details =====")
    for name, courses in students.items():
        print(f"{name}: {', '.join(courses)}")

# ===== Example Usage =====
# Add students
add_student("Satish", ["Math", "Physics"])
add_student("Lalita", ["Chemistry", "Biology"])
add_student("Pavan", ["Computer Science"])

# Update courses
update_courses("Satish", ["English", "Physics"])  # Physics already exists, will avoid duplicate
update_courses("Pavan", ["Math", "English"])

# Display all student details
display_students()

# Mini Project 10: Number Utility Tool

# Function to convert number to binary, octal, and hexadecimal
def convert_number(num):
    binary = bin(num)
    octal = oct(num)
    hexa = hex(num)
    return binary, octal, hexa

# Function to format number with commas
def format_with_commas(num):
    return "{:,}".format(num)

# Function to print scientific notation
def scientific_notation(num):
    return "{:.3e}".format(num)  # 3 decimal places

# ===== Example Usage =====
number = 123456789

# Conversions
binary, octal, hexa = convert_number(number)
print(f"Number: {number}")
print(f"Binary: {binary}")
print(f"Octal: {octal}")
print(f"Hexadecimal: {hexa}")

# Formatted with commas
formatted = format_with_commas(number)
print(f"Formatted with commas: {formatted}")

# Scientific notation
sci_notation = scientific_notation(number)
print(f"Scientific notation: {sci_notation}")











