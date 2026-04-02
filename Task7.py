# ===============================
# ✅ Task 2: Abstraction (ABC)
# ===============================
from abc import ABC, abstractmethod
from functools import reduce

class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass


# ===============================
# ✅ Task 1: super() Usage
# ===============================
class User(AbstractUser):
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return f"Student -> {self.name}, {self.id}, {self.dept}, {self.fees}"


class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def get_details(self):
        return f"Faculty -> {self.name}, {self.id}, {self.salary}"


class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

    def get_details(self):
        return f"TempFaculty -> {self.name}, {self.id}, {self.salary}, {self.duration}"


# ===============================
#    Data Creation
# ===============================
students = [
    Student("Satish", 101, "CSE", 60000),
    Student("Ravi", 102, "ECE", 45000),
    Student("Anjali", 103, "IT", 75000)
]

faculty = [
    Faculty("Rao", 201, 40000),
    Faculty("Sharma", 202, 28000),
    TempFaculty("Kumar", 203, 35000, "6 months")
]


# ===============================
# ✅ Task 3: Sorting using key
# ===============================
students.sort(key=lambda x: x.fees)
faculty.sort(key=lambda x: x.salary)


# ===============================
# ✅ Task 4: map()
# ===============================
student_names = list(map(lambda s: s.name, students))


# ===============================
# ✅ Task 5: filter()
# ===============================
high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))


# ===============================
# ✅ Task 6: reduce()
# ===============================
total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)


# ===============================
# ✅ Task 7: Higher Order Function
# ===============================
def process_users(users, func):
    return list(map(func, users))

uppercase_names = process_users(students, lambda s: s.name.upper())


# ===============================
#   Final Challenge Output
# ===============================
print("\n--- ALL DETAILS ---")
for s in students:
    print(s.get_details())
for f in faculty:
    print(f.get_details())

print("\n--- SORTED DATA ---")
for s in students:
    print(s.get_details())
for f in faculty:
    print(f.get_details())

print("\n--- STUDENT NAMES (map) ---")
print(student_names)

print("\n--- FILTERED DATA ---")
for s in high_fee_students:
    print(s.get_details())
for f in high_salary_faculty:
    print(f.get_details())

print("\n--- TOTALS ---")
print("Total Fees:", total_fees)
print("Total Salary:", total_salary)

print("\n--- HIGHER ORDER FUNCTION ---")
print("Uppercase Names:", uppercase_names)

print("\n--- COMBINED (map + filter + reduce) ---")
combined = reduce(
    lambda acc, x: acc + x,
    map(lambda s: s.fees, filter(lambda s: s.fees > 50000, students)),
    0
)
print("Filtered Total Fees:", combined)