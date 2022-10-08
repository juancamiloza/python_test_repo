status = input("Welcome to J's dice probability calculator, press enter to continue or exit to leave")
number_of_dice = int(input("How many dice you want to calculate? "))
number_of_faces = int(input("How many faces your dice will have? "))
desired_outcome = int(input("what is your desired outcome? "))
frequency = int(input("How many times you want it to show? "))
calculation = ((1*frequency/(number_of_faces*number_of_dice))**frequency)*100
rounded = "{:.2f}".format(calculation)
print(f"{desired_outcome} will have around a {rounded}% chance to show up "
      f"{frequency} times, when using {number_of_dice} dices, with {number_of_faces} faces")