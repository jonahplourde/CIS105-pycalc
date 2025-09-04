print("Select operation (1/2/3/4):")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
operation = input("")

def add (a, b):
    return (a + b)

def subtract (a, b):
    return (a - b)

def multiply (a, b):
    return (a * b)

def divide (a, b):
    return a / b

if operation not in ['1', '2', '3', '4']:
    print("Invalid input. Please choose 1, 2, 3, or 4.")

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
except ValueError:
    print("Invalid input. Please enter numbers.")
    exit()

if operation == '1':
    print(f"The sum of {a} and {b} is {add(a, b)}.")
elif operation == '2':
    print(f"The difference of {a} and {b} is {subtract(a, b)}.")
elif operation == '3':
    print(f"The product of {a} and {b} is {multiply(a, b)}.")
elif operation == '4':
    if b == 0:
        print("Error! You cannot divide by zero")
    elif b != 0:
        print(f"The quotient of {a} and {b} is {divide(a, b)}.")
