# Hello, this is a test script. 
# This will help me improve my coding skills.
# I will be adding more features to this script in the future.
# I will also be adding more comments to explain the code.


# I want to create a simple calculator that can perform basic arithmetic operations.
# The calculator will take two numbers and an operator as input and return the result.

def add(x, y):
    """This function adds two numbers."""
    return x + y
def subtract(x, y):
    """This function subtracts two numbers."""
    return x - y
def multiply(x, y):
    """This function multiplies two numbers."""
    return x * y
def divide(x, y):
    """This function divides two numbers."""
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y
def calculator():
    input1 = float(input("Enter first number: "))
    input2 = operation = input("Enter operation (+, -, *, /): ")
    input3 = float(input("Enter second number: "))
    if operation == '+':
        print(f"{input1} + {input3} = {add(input1, input3)}")
    elif operation == '-':
        print(f"{input1} - {input3} = {subtract(input1, input3)}")
    elif operation == '*':
        print(f"{input1} * {input3} = {multiply(input1, input3)}")
    elif operation == '/':
        print(f"{input1} / {input3} = {divide(input1, input3)}")
    else:
        print("Invalid operator. Please use +, -, *, or /.")
        
