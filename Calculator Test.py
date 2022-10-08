def calculator():
    import operator
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    operations_list = ["+", "-", "*", "/"]
    print("Welcome to J's Calculator 2.0")
    first_number = float(input("Enter your first number: "))
    operation = input("What operation you want to calculate? (+,-,*,/)")
    while operation not in operations_list:
        operation = input("Wrong input, please chose an operation from (+,-,*,/)")
    second_number = float(input("Enter your second number: "))
    answer = (ops[operation](first_number, second_number))
    answer_two_decimal = "{:.2f}" .format(answer)
    print(f"Full answer: {answer}")
    print(f"Approximated answer: {answer_two_decimal}")
calculator()
