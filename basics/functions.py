import math

def addition(num_one, num_two):
    return num_one + num_two

def subtraction(num_one, num_two):
    return num_two - num_one

def division(num_one, num_two):
    return math.floor(num_two/num_one)

def multiplication(num_one, num_two):
    return num_two*num_one

num_one = int(input("Enter first number:"))
num_two = int(input("Enter second number:"))

operation = int(input("\n Enter Operation: \n 1. Addition (+) \n 2. Subtraction (-) \n 3. Multiplication (*) \n 4. Division (+) \n Please enter numbers only (1 to 4)."))

if operation == 1:
    print(addition(num_one, num_two))
elif operation == 2:
    print(subtraction(num_two, num_one))
elif operation == 3:
    print(division(num_two, num_one))
elif operation == 4:
     print(multiplication(num_two, num_one))
else:
    print("Please select valid operation.")
 
 