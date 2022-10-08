operation = 0
def calculator():
    print("Welcome to J's Calculator 1.0")
    operation = input("What operation you want to calculate? (+,-,*,/)")
    if operation == "+":
        first_number = float(input("Enter your first number: "))
        second_number = float(input("Enter your second number: "))
        print("Answer: ")
        print(first_number + second_number)
    elif operation == "-":
        first_number = float(input("Enter your first number: "))
        second_number = float(input("Enter your second number: "))
        print("Answer: ")
        print(first_number - second_number)
    elif operation == "*":
        first_number = float(input("Enter your first number: "))
        second_number = float(input("Enter your second number: "))
        print("Answer: ")
        print(first_number * second_number)
    elif operation == "/":
        first_number = float(input("Enter your first number: "))
        second_number = float(input("Enter your second number: "))
        print("Answer: ")
        print(first_number / second_number)
    elif operation == "Exit":
        print("Tank you for using J's Calculator")
    else: print("Error, Type a valid operation")
while operation != "Exit":
    calculator()