import random
roll_state = True
print("Welcome to J's dice program")
dice_faces = int(input("How Many faces you would like your dices to have? "))
while roll_state:
    try:
        dices = [random.randint(1, dice_faces)]
        number_of_dices = int(input("How many dices you want roll? (0 to change the number of faces,-1 to exit) "))
        if number_of_dices == 1:
            print("Outcome:")
            print(dices)
        elif number_of_dices == 0:
            dice_faces = int(input("How Many faces you would like your dices to have? "))
        elif number_of_dices == -1:
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
