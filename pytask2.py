# Bitwise Operator Tasks (1-8) 

# 1
a = 10
b = 6
print(a & b)

# 2 

x = 12
y = 5
print(x | y)

# 3
num = 8
print(~num)

# 4 
a = 15
b = 9
print(a ^ b)

# 5
num = 7
print(num << 2)

# 6
num = 20
print(num >> 1)

# 7
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a & b)

# 8
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a ^ b)


# String Tasks (9-14)

# 9 
s = "hi"
print(s * 4)

# 10
s = "python"
print(s * 3)

# 11
s1 = "super"
s2 = "man"
print(s1 + s2)

# 12 
s1 = "hello"
s2 = " "
s3 = "world"
print(s1 + s2 + s3)

# 13
name = input("Enter name: ")
print(name * 5)

# 14 
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print(s1 + s2)

# Input & Type Casting Tasks (15-20)

# 15 
name = input("Enter name: ")
print(type(name))

# 16
age = int(input("Enter age: "))
print(age)
print(type(age))

# 17 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a + b)

# 18 
m1 = int(input("Enter marks1: "))
m2 = int(input("Enter marks2: "))
avg = (m1 + m2) / 2
print(avg)

# 19 
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(3 * a * 2 + b - 2)

# 20 
num = input("Enter number: ")
print(type(num))
num = int(num)
print(type(num))

# Unit Digit Tasks (21–25)

# 21
num = input("Enter number: ")
print(num[-1])

# 22
num = int(input("Enter number: "))
print(num % 10)

# 23 
num = int(input("Enter number: "))
print(num // 10)

# 24
num = int(input("Enter number: "))
print((num // 10) % 10)

# 25
num = int(input("Enter 5 digit number: "))
print(num % 10)

#If Statement Tasks (26–30)

# 26
if 10 >= 5:
    print("10 is greater than or equal to 5")

# 27
num = int(input("Enter number: "))
if num > 50:
    print("Number is greater than 50")

# 28
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible")

# 29
num = int(input("Enter number: "))
if num > 100:
    print("Number is greater than 100")

# 30
num = int(input("Enter number: "))
if num >= 0:
    print("Number is positive")

# If-Else Tasks (31–34)

# 31
num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 32
marks = int(input("Enter marks: "))
if marks >= 35:
    print("Pass")
else:
    print("Fail")

# 33
num = int(input("Enter number: "))
if num >= 0:
    print("Positive")
else:
    print("Negative")

# 34
num = int(input("Enter number: "))
if num > 10:
    print("Greater than 10")
else:
    print("Not greater than 10")

# Nested If Tasks (35–37)

# 35
age = int(input("Enter age: "))
height = int(input("Enter height: "))
weight = int(input("Enter weight: "))

if age >= 18:
    if height >= 160:
        if weight >= 60:
            print("Selected")
        else:
            print("Rejected")
    else:
        print("Rejected")
else:
    print("Rejected")

# 36
marks = int(input("Enter marks: "))
age = int(input("Enter age: "))

if marks >= 60:
    if age >= 17:
        print("Admission Granted")
    else:
        print("Admission Rejected")
else:
    print("Admission Rejected")

# 37
age = int(input("Enter age: "))
height = int(input("Enter height: "))
weight = int(input("Enter weight: "))

if age >= 16:
    if height >= 150:
        if weight >= 50:
            print("Selected")
        else:
            print("Rejected")
    else:
        print("Rejected")
else:
    print("Rejected")

# Match Statement Tasks (38–40)

# 38
num = int(input("Enter number (1-7): "))

match num:
    case 1: print("Monday")
    case 2: print("Tuesday")
    case 3: print("Wednesday")
    case 4: print("Thursday")
    case 5: print("Friday")
    case 6: print("Saturday")
    case 7: print("Sunday")

# 39
num = int(input("Enter number (1-3): "))

match num:
    case 1: print("Red")
    case 2: print("Blue")
    case 3: print("Green")

# 40
num = int(input("Enter number (1-4): "))

match num:
    case 1: print("Apple")
    case 2: print("Mango")
    case 3: print("Orange")
    case 4: print("Banana")


