# ==============================
# Task 1: Encapsulation
# ==============================
class UserEncap:
    def __init__(self):
        self.__user_name = None
        self.__pwd = None

    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd

    def get_user(self):
        return self.__user_name

    def register(self):
        print(f"Registering user: {self.__user_name}")

    def login(self):
        print(f"Logging in: {self.__user_name}")


# ==============================
# Task 2: Inheritance
# ==============================
class UserBase:
    def register(self):
        print("User Registered")

    def login(self):
        print("User Logged In")


class StudentInherit(UserBase):
    def student_greet(self):
        print("Hello Student")


class FacultyInherit(UserBase):
    def faculty_greet(self):
        print("Hello Faculty")


class TempFaculty(FacultyInherit):
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")


# ==============================
# Task 3: Method Overriding
# ==============================
class UserOverride:
    def greet(self):
        print("Welcome User")


class StudentOverride(UserOverride):
    def greet(self):
        print("Welcome Student")


class FacultyOverride(UserOverride):
    def greet(self):
        print("Welcome Faculty")


# ==============================
# Task 4: Method Chaining
# ==============================
class UserChain:
    def register(self):
        print("registered")
        return self

    def login(self):
        print("logined")
        return self

    def greet(self):
        print("enjoy everyone")
        return self


# ==============================
# Task 5: Combined Real-Time System
# ==============================
class User:
    users_count = 0

    def __init__(self, username, pwd):
        self.__username = username
        self.__pwd = pwd
        User.users_count += 1

    def get_user(self):
        return self.__username

    def register(self):
        print(f"{self.__username} registered")
        return self

    def login(self):
        print(f"{self.__username} logined")
        return self

    def greet(self):
        print("Welcome User")
        return self


class Student(User):
    def greet(self):
        print("Welcome Student")
        return self


class Faculty(User):
    def greet(self):
        print("Welcome Faculty")
        return self


# ==============================
#   TESTING ALL TASKS
# ==============================

print("\n--- Task 1: Encapsulation ---")
u1 = UserEncap()
u1.set_user("john", "1234")
u1.register()
u1.login()
print("Username:", u1.get_user())

print("\n--- Task 2: Inheritance ---")
s = StudentInherit()
s.register()
s.login()
s.student_greet()

f = FacultyInherit()
f.register()
f.login()
f.faculty_greet()

t = TempFaculty()
t.register()
t.login()
t.faculty_greet()
t.tempFaculty_greet()

print("\n--- Task 3: Method Overriding ---")
s1 = StudentOverride()
s1.greet()

f1 = FacultyOverride()
f1.greet()

print("\n--- Task 4: Method Chaining ---")
user_chain = UserChain()
user_chain.login().greet().register()

print("\n--- Task 5: Combined System ---")
u2 = Student("john", "123")
u2.login().greet().register()

u3 = Faculty("smith", "456")
u3.login().greet().register()

print("Total Users:", User.users_count)