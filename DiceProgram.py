import random
roll_state = False
dice_sides = 6
while not roll_state:
    first_dice = random.randint(1, dice_sides)
    second_dice = random.randint(1, dice_sides)
    user_action = str.capitalize((input("Type 'Roll' to roll the dice or 'Mod' to change dice faces: ")))
    if user_action == "Roll":
        print("First Dice:", first_dice)
        print("Second Dice:", second_dice)
    if user_action == "Mod":
        dice_sides = float(input("How many faces you want your dice to have? "))
    if user_action == "Exit":
        roll_state = True
    else:
        print("Wrong input, Type 'Roll' to roll the dice: ")