#calculator

def add():
    a = float(input("Enter a number : "))
    b = float(input("Enter another number : "))
    print(a + b)


def substraction():
    a = float(input("Enter a number : "))
    b = float(input("Enter another number : "))
    print(a - b)


def multiply():
    a = float(input("Enter a number : "))
    b = float(input("Enter another number : "))
    print(a * b)


def division():
    a = float(input("Enter a number : "))
    b = float(input("Enter another number : "))
    print(a / b)


""""
add()
substraction()
multiply()
division()
"""

on = True
while on:

    operation = input("please type +, -, *, / or q:")

    if operation == "+":
        add()
    elif operation == "-":
        substraction()
    elif operation == "*":
        multiply()
    elif operation == "/":
        division()
    elif operation == "q":
        on = False
    else:
        print("That operation is not available")
