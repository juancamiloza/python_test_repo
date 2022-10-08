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
    print(ops[operation](first_number, second_number))
calculator()
