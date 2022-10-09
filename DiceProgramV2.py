import random

import hello

program_state = True

while program_state:

    hello.program_name("Dice Roll V2")

    try:
        dice_faces = int(input("How Many faces you would like your dices to have? "))
        roll_state = True
        while roll_state:
            try:
                dices = [random.randint(1, dice_faces)]
                number_of_dices = int(input("How many dices you want roll? (0 to go back) "))
                if number_of_dices == 1:
                    print("Outcome:")
                    print(dices)
                elif number_of_dices == 0:
                    roll_state = False
                else:
                    create = 1
                    # for create, number_of_dices in enumerate(dices.append(random.randint(1,dice_faces))):
                    while create != number_of_dices:
                        dices.append(random.randint(1, dice_faces))
                        create += 1
                    print("Outcome:")
                    print(*dices, sep="|")
                    print(f"For {len(dices)} dice")
            except ValueError:
                print("Wrong value, type a number")
    except ValueError:
        print("Wrong value, type a number")
