# Task 1: User Info Manager (Functions + Dictionary)

# Function to create a user
def create_user(name, age, role):
    user = {
        "name": name.title(),   # Format name using .title()
        "age": age,
        "role": role.title()   # Optional: format role also
    }
    return user


# List to store multiple users
users = []

# Adding users
users.append(create_user("satish kumar", 22, "developer"))
users.append(create_user("alice johnson", 25, "designer"))
users.append(create_user("bob smith", 30, "manager"))

# Print all users
print("===== User Details =====")
for user in users:
    print(f"Name: {user['name']}, Age: {user['age']}, Role: {user['role']}")

# Task 2: Dynamic Calculator (*args)

# Function to calculate total and average
def calculate_total(*numbers):
    total = sum(numbers)
    
    if len(numbers) == 0:
        average = 0
    else:
        average = total / len(numbers)
    
    return total, average


# Example usage
result = calculate_total(10, 20, 30, 40)

print("Total:", result[0])
print("Average:", result[1])

#  Task 3: Keyword Config System (**kwargs)

# Function to print system configurations
def system_config(**settings):
    print("===== System Configuration =====")
    for key, value in settings.items():
        print(f"{key}: {value}")


# Example usage
system_config(mode="debug", version="1.0", theme="dark", max_users=100)

#  Task 4: Factorial Service (Recursion)

# Recursive factorial function
def factorial(n):
    if n < 0:
        return "Error: Factorial of negative numbers is not defined."
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Example usage
numbers = [5, 0, -3]
for num in numbers:
    print(f"Factorial of {num}:", factorial(num))

#Task 5: Memory Optimization (Generator)

# Generator function to yield squares
def square_generator(n):
    for i in range(1, n + 1):
        yield i ** 2


# Normal list approach
n = 5
squares_list = [i ** 2 for i in range(1, n + 1)]
print("Normal list:", squares_list)
print("Type:", type(squares_list))

# Generator approach
squares_gen = square_generator(n)
print("\nGenerator object:", squares_gen)
print("Type:", type(squares_gen))

# To get values from generator
print("Squares from generator:", list(squares_gen))

# Task 6: Exception Handling Module

# Exception handling for division
def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print(f"Input: numerator={numerator}, denominator={denominator}")
        print("Error: Cannot divide by zero.")
    except TypeError:
        print(f"Input: numerator={numerator}, denominator={denominator}")
        print("Error: Invalid input. Please enter numbers only.")
    else:
        print(f"Input: numerator={numerator}, denominator={denominator}")
        print(f"Result: {result}")
    finally:
        print("Program Completed\n")


# Example usage
# Case 1: Valid division
divide_numbers(10, 2)

# Case 2: Divide by zero
divide_numbers(10, 0)

# Case 3: Invalid input (simulated by passing string)
divide_numbers("ten", 2)

#  Task 7: File Handling

# Sample user details
users = [
    {"name": "Satish Kumar", "age": 22, "role": "Developer"},
    {"name": "Alice Johnson", "age": 25, "role": "Designer"},
    {"name": "Bob Smith", "age": 30, "role": "Manager"}
]

# File path
file_name = "team_data.txt"

# Writing user details to file
with open(file_name, "w") as file:
    for user in users:
        file.write(f"Name: {user['name']}, Age: {user['age']}, Role: {user['role']}\n")

# Reading and displaying content
with open(file_name, "r") as file:
    content = file.read()
    print("===== Team Data =====")
    print(content)

# Bonus: Check if file is closed
print("Is file closed after writing and reading?", file.closed)  # False, because last with block is closed 