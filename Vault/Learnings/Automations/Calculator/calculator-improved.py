# Hello, this is a test script. 
# This will help me improve my coding skills.
# I will be adding more features to this script in the future.
# I will also be adding more comments to explain the code.


# I want to create a simple calculator that can perform basic arithmetic operations.
# The calculator will take two numbers and an operator as input and return the result.
# -----------------------------------------------------
# This is an improved version of the calculator script.
# This calculator can perform addition, subtraction, multiplication, division, and exponentiation.


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
    operation = input("Enter operation (+, -, *, /, **): ")
    input2 = float(input("Enter second number: "))
    if operation == '+':
        print(f"{input1} + {input2} = {add(input1, input2)}")
    elif operation == '-':
        print(f"{input1} - {input2} = {subtract(input1, input2)}")
    elif operation == '*':
        print(f"{input1} * {input2} = {multiply(input1, input2)}")
    elif operation == '/':
        print(f"{input1} / {input2} = {divide(input1, input2)}")

    else:
        print("Invalid operator. Please use a valid operator.")
        
