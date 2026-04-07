# ============================================
#  SMART EXPENSE MANAGER SYSTEM
# ============================================
# Features:
# User Creation
# Add / View Expenses
# Filter (Category & Date)
# Total Calculation (map + reduce)
# Category-wise Spending
# Update / Delete
# Monthly Report
# Highest Expense
# Smart Insight
# ============================================


# ---------- DATABASE CONNECTION ----------
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="satish@1234",
    database="expense_db"
)

cursor = conn.cursor()


# ---------- OOP IMPLEMENTATION ----------
from abc import ABC, abstractmethod

#  Abstract Class
class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass


#  Base Class (Encapsulation)
class User(AbstractUser):
    def __init__(self, name):
        self.__name = name   # private variable

    def get_details(self):
        return self.__name

    def add_user(self):
        query = "INSERT INTO users (name) VALUES (%s)"
        cursor.execute(query, (self.__name,))
        conn.commit()
        print(" User Added Successfully!")


#  Derived Class (Inheritance + Overriding)
class Expense(User):
    def __init__(self, name):
        super().__init__(name)

    def get_details(self):   # Method overriding
        return "Expense User: " + super().get_details()

    def add_expense(self, user_id, amount, category, desc, date):
        query = """
        INSERT INTO expenses (user_id, amount, category, description, date)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (user_id, amount, category, desc, date))
        conn.commit()
        print(" Expense Added!")


# ---------- VIEW EXPENSES (JOIN) ----------
def view_expenses(user_id):
    print("\n All Expenses:")
    query = """
    SELECT u.name, e.amount, e.category, e.description, e.date
    FROM users u
    JOIN expenses e ON u.user_id = e.user_id
    WHERE u.user_id = %s
    """
    cursor.execute(query, (user_id,))
    for row in cursor.fetchall():
        print(row)


# ---------- FILTERING ----------
def filter_by_category(user_id, category):
    print("\n Filter by Category:")
    cursor.execute("SELECT * FROM expenses WHERE user_id=%s", (user_id,))
    data = cursor.fetchall()

    result = [x for x in data if x[3] == category]   # list comprehension
    print(result)


def filter_by_date(user_id, date):
    print("\n Filter by Date:")
    cursor.execute("SELECT * FROM expenses WHERE user_id=%s", (user_id,))
    data = cursor.fetchall()

    result = list(filter(lambda x: str(x[5]) == date, data))
    print(result)


# ---------- TOTAL EXPENSE ----------
from functools import reduce

def total_expense(user_id):
    print("\n Total Expense:")
    cursor.execute("SELECT amount FROM expenses WHERE user_id=%s", (user_id,))
    data = cursor.fetchall()

    amounts = list(map(lambda x: x[0], data))
    total = reduce(lambda a, b: a + b, amounts, 0)

    print("Total:", total)


# ---------- CATEGORY-WISE SPENDING ----------
def category_wise(user_id):
    print("\n Category-wise Spending:")
    cursor.execute("SELECT category, amount FROM expenses WHERE user_id=%s", (user_id,))
    data = cursor.fetchall()

    result = {}
    for cat, amt in data:
        result[cat] = result.get(cat, 0) + amt

    print(result)


# ---------- UPDATE & DELETE ----------
def update_expense(exp_id, amount):
    cursor.execute("UPDATE expenses SET amount=%s WHERE exp_id=%s", (amount, exp_id))
    conn.commit()
    print(" Expense Updated!")


def delete_expense(exp_id):
    cursor.execute("DELETE FROM expenses WHERE exp_id=%s", (exp_id,))
    conn.commit()
    print(" Expense Deleted!")


# ---------- ADVANCED FEATURES ----------
#  Monthly Report
def monthly_report(user_id):
    print("\n Monthly Report:")
    cursor.execute("SELECT date, amount FROM expenses WHERE user_id=%s", (user_id,))
    data = cursor.fetchall()

    report = {}
    for d, amt in data:
        month = d.month
        report[month] = report.get(month, 0) + amt

    print(report)


#  Highest Expense
def highest_expense(user_id):
    print("\n🔝 Highest Expense:")
    cursor.execute("SELECT amount FROM expenses WHERE user_id=%s", (user_id,))
    data = cursor.fetchall()

    max_val = reduce(lambda a, b: a if a > b[0] else b[0], data, 0)
    print(max_val)


#  Smart Insight
def smart_insight(user_id):
    print("\n Smart Insight:")
    cursor.execute("SELECT category, amount FROM expenses WHERE user_id=%s", (user_id,))
    data = cursor.fetchall()

    result = {}
    for cat, amt in data:
        result[cat] = result.get(cat, 0) + amt

    highest = max(result, key=result.get)
    print(f" You are spending too much on {highest}")


# ============================================
#    MAIN EXECUTION
# ============================================

if __name__ == "__main__":

    # Create User
    u1 = Expense("Satish")
    u1.add_user()

    # Add Expenses
    u1.add_expense(1, 500, "Food", "Lunch", "2026-04-01")
    u1.add_expense(1, 1500, "Shopping", "Clothes", "2026-04-02")
    u1.add_expense(1, 700, "Travel", "Bus", "2026-04-03")

    # View Data
    view_expenses(1)

    # Filtering
    filter_by_category(1, "Food")
    filter_by_date(1, "2026-04-01")

    # Calculations
    total_expense(1)
    category_wise(1)

    # Advanced
    monthly_report(1)
    highest_expense(1)
    smart_insight(1)
