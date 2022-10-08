import random
unknown_number = random.randint(0,100)
score = 105
accuracy = "100"
answer_correct = False
print("Welcome to J's guess a number game!")
# program loop
while not answer_correct:
    player_guess = float(input("Guess a number between 0 and 100: "))
    score = score - 5
    accuracy = abs(unknown_number - player_guess)
    if accuracy in range(1,5) and not answer_correct:
        print("You are very close!")
    elif accuracy in range (6,20) and not answer_correct:
        print("You are close!")
    elif accuracy in range (21,40) and not answer_correct:
        print("You're off, Keep Trying!")
    elif accuracy in range (41,100) and not answer_correct:
        print("You are no where close!")
    elif player_guess == unknown_number:
        print("You've guessed it!")
        answer_correct = True
    elif player_guess not in range(0,100):
        print("That's not even a correct guess")
print("Final Score: ",score,"/100")