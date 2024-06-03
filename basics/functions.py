import math

def addition(num_one = 0, num_two = 0):
    return num_one + num_two

def addition(num_one = 0, num_two = 0):
    return num_two - num_one

def division(num_one = 0, num_two = 0):
    return math.floor(num_two/num_one)

def multiplication(num_one = 0, num_two = 0):
    return math.floor(num_two/num_one)

# def calculate(operation, num_one, num_two):
#     operation:
#         case 1:
#             return addition(num_one, num_two)

RUN_CALCULATOR = True

num_one = int(input("Enter first number:"))
num_two = int(input("Enter second number:"))

operation = (input("\n Enter Operation: \n 1. Addition (+) \n 2. Subtraction (-) \n 3. Multiplication (*) \n 4. Division (+) \n Please enter numbers only (1 to 4)."))


    