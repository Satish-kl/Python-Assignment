# Section 1 : Loop Basics (1-10)

# 1 Print numbers from 1 to 50

for i in range(1, 51):
    print(i)

# 2 Print even numbers (1–100)

for i in range(2, 101, 2):
    print(i)

# 3 Print odd numbers (1–100)

for i in range(1, 101, 2):
    print(i)

# 4 Multiplication table of 7

for i in range(1, 11):
    print(7 * i)

# 5 Sum of numbers (1–100)

total = 0

for i in range(1, 101):
    total += i

print(total)

# 6 Reverse (50 → 1)

for i in range(50, 0, -1):
    print(i)

# 7 Count numbers divisible by 3 (1–100)

count = 0

for i in range(1, 101):
    if i % 3 == 0:
        count += 1

print(count)

# 8 Squares (1–10)

for i in range(1, 11):
    print(i * i)

# 9 Cubes (1–10)

for i in range(1, 11):
    print(i ** 3)

#10 Input n → print 1 to n

n = int(input("Enter number: "))

for i in range(1, n + 1):
    print(i)

# Section 2 : While Loop (11-15)

# 11 Print numbers from 1 to 20
i = 1

while i <= 20:
    print(i)
    i += 1

# 12 Factorial using while
n = int(input("Enter number: "))
fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1

print(fact)

# 13 Reverse a number
num = int(input("Enter number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print(rev)

# 14 Count digits in a number
num = int(input("Enter number: "))
count = 0

while num > 0:
    num = num // 10
    count += 1

print(count)

# 15 Keep asking input until user enters "stop"
while True:
    text = input("Enter something: ")
    
    if text == "stop":
        break

# Section 3 : NESTED LOOPS (16–20)

# 16 Pattern
for i in range(1, 5):
    line = ""
    for j in range(1, i+1):
        line += "*"
    print(line)

# 17 Pattern
for i in range(1, 5):
    line = ""
    for j in range(1, i + 1):
        line += str(j)
    print(line)

 # 18 Multiplication tables (1 to 5)
 for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print()  # space between tables

# 19 Pattern
for i in range(3):
    line = ""
    for j in range(3):
        line += chr(65 + j) + " "
    print(line)

# 20 Pattern
num = 1

for i in range(3):
    line = ""
    for j in range(3):
        line += str(num) + " "
        num += 1
    print(line)

# Section 4: String Basics (21–25)

# 21 Count total characters in a string
text = "hello world"   # manually give input

count = 0
for ch in text:
    count += 1

print("Total characters:", count)

# 22 Count vowels
text = "education"   # give your own string here

count = 0
for ch in text:
    if ch.lower() in "aeiou":
        count += 1

print("Vowels:", count)

# 23 Count consonants
text = "Hello World"

count = 0
for ch in text:
    if ch.isalpha() and ch.lower() not in "aeiou":
        count += 1

print("Consonants:", count)

# 24 Reverse a string (using loop)
text = input("Enter string: ")

rev = ""
for ch in text:
    rev = ch + rev

print("Reversed:", rev)

# 25 Check palindrome
text = "madam"

rev = ""
for ch in text:
    rev = ch + rev

if text == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

# Section 5: String Slicing (26–30)

# 26 Print first 5 characters
text = "HelloWorld"

print(text[:5])

# 27 Print last 3 characters
text = "HelloWorld"

print(text[-3:])

# 28 Print string in reverse using slicing
text = "HelloWorld"

print(text[::-1])

# 29 Print every 2nd character
text = "HelloWorld"

print(text[::2])

# 30 Remove first and last character
text = "HelloWorld"

print(text[1:-1])

# Section 6: List Basics (31–35)

# 31 Create a list of 5 numbers and print sum
nums = [10, 20, 30, 40, 50]

total = sum(nums)
print("Sum:", total)

# 32 Find maximum value in list
nums = [10, 20, 30, 40, 50]

print("Maximum:", max(nums))

# 33 Find minimum value in list
nums = [10, 20, 30, 40, 50]

print("Minimum:", min(nums))

# 34 Count total elements in list
nums = [10, 20, 30, 40, 50]

print("Count:", len(nums))

# 35 Check if element exists in list
nums = [10, 20, 30, 40, 50]

element = 30

if element in nums:
    print("Element exists")
else:
    print("Element not found")

# Section 7: List Operations (36–40)

# 36 Add 3 elements using append()
nums = [10, 20]

nums.append(30)
nums.append(40)
nums.append(50)

print(nums)

# 37 Insert element at specific index
nums = [10, 20, 40, 50]

nums.insert(2, 30)   # insert 30 at index 2

print(nums)

# 38 Remove element using remove()
nums = [10, 20, 30, 40, 50]

nums.remove(30)   # removes value 30

print(nums)

# 39 Reverse list without using .reverse()
nums = [10, 20, 30, 40, 50]

rev = []
for i in range(len(nums) - 1, -1, -1):
    rev.append(nums[i])

print(rev)

# 40 Sort list without using .sort()
nums = [50, 20, 40, 10, 30]

# simple bubble sort
for i in range(len(nums)):
    for j in range(len(nums) - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(nums)

