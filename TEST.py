def usr_input():
    testi = False
    while not testi:
        try:
            choice1 = int(input("Choose a cell to place X: "))
            testi = True
            return choice1
        except ValueError:
            print(("\nWrong value, type a number\n"))

choice = usr_input()
print(choice)

