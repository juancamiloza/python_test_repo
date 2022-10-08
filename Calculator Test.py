def calculator():
    import operator
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    print("Welcome to J's Calculator 2.0")
    first_number = float(input("Enter your first number: "))
    operation = input("What operation you want to calculate? (+,-,*,/)")
    second_number = float(input("Enter your second number: "))
    answer = (ops[operation](first_number, second_number))
    answer_two_decimal = "{:.2f}" .format(answer)
    print(f"Full answer: {answer}")
    print(f"Aproximated answer: {answer_two_decimal}")
calculator()
