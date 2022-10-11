import random
import copy
import time
import hello



program_state = True   

while program_state:

    hello.program_name("Tic Tac Toe")

#def create_board(size):
#    glist = []
#    for c in range (size):
#        glist.append([" "])
#    for d in range (size-1):
#        glist[0].append((" "))
#    for e in range (size-1):
#        glist[1].append((" "))
#    for f in range (size-1):
#        glist[2].append((" "))
#    print(glist)



    win_condition = False
    winx = [" X "," X "," X "]
    wino = [" O "," O "," O "]
    size = 3
    help = [[" 1 "," 2 "," 3 "],[" 4 "," 5 "," 6 "],[" 7 "," 8 "," 9 "]]
    glist = []
    clist = []
    start = random.randint(0,1)
    for c in range (size):
        glist.append(["   "])
    for d in range (size-1):
        glist[0].append(("   "))
    for e in range (size-1):
        glist[1].append(("   "))
    for f in range (size-1):
        glist[2].append(("   "))
        

    def print_board():
        print("\n")
        matrix_size = size
        divisor = "----" * matrix_size
        p = 0
        while p <= matrix_size:
            print(*glist[p], sep="|")
            p += 1
            if p < matrix_size:
                print(divisor)
            else:
                break
        print("\n")


    def print_help():
        print("\n")
        matrix_size = size
        divisor = "----" * matrix_size
        p = 0
        while p <= matrix_size:
            print(*help[p], sep="|")
            p += 1
            if p < matrix_size:
                print(divisor)
            else:
                break
        print(f"\nWhen promped, type the number of the cell you want to place your charater\n")

    def decompile_list():
        for c in range(size):
            clist.append(glist[0][c])
        for c in range(size):
            clist.append(glist[1][c])
        for c in range(size):
            clist.append(glist[2][c])

    def compile_list():
        glist[0][0] = clist [0]
        glist[0][1] = clist [1]
        glist[0][2] = clist [2]
        glist[1][0] = clist [3]
        glist[1][1] = clist [4]
        glist[1][2] = clist [5]
        glist[2][0] = clist [6]
        glist[2][1] = clist [7]
        glist[2][2] = clist [8]

    def random_choice():
        cchallenge = True
        while cchallenge:
            challenge = random.randint(0,8)
            if clist[challenge] == "   ":
                clist[challenge] = " O "
                cchallenge = False
            else:
                cchallenge = True
    def win_check():
        if w1 == winx:
            win_condit = True
        elif w2 == winx:
            win_condit = True
        elif w3 == winx:
            win_condit = True
        elif w4 == winx:
            win_condit = True
        elif w5 == winx:
            win_condit = True
        elif w6 == winx:
            win_condit = True
        elif w7 == winx:
            win_condit = True
        elif w1 == wino:
            win_condit = True
        elif w2 == wino:
            win_condit = True
        elif w3 == wino:
            win_condit = True
        elif w4 == wino:
            win_condit = True
        elif w5 == wino:
            win_condit = True
        elif w6 == wino:
            win_condit = True
        elif w7 == wino:
            win_condit = True
        else:
            win_condit = False
        return win_condit


    try:
        print_help()
        time.sleep(3)
        if start == 0:
            turn = 0
            while not win_condition:
                if turn == 0:
                    print("Your turn!\n")
                    choice = int(input("Choose a cell to place X: "))
                    decompile_list()
                    clist[choice-1] = " X "
                    compile_list()
                    print_board()
                    w1 = [clist[0],clist[1],clist[2]]
                    w2 = [clist[3],clist[4],clist[5]]
                    w3 = [clist[6],clist[7],clist[8]]
                    w4 = [clist[0],clist[4],clist[8]]
                    w5 = [clist[2],clist[4],clist[6]]
                    w6 = [clist[1],clist[4],clist[7]]
                    w7 = [clist[0],clist[3],clist[6]]
                    w7 = [clist[2],clist[5],clist[8]]
                    win_check()
                    win_condition = win_check()
                    turn = 1
                else:
                    print("Computer's turn")
                    time.sleep(3)
                    decompile_list()
                    random_choice()
                    compile_list()
                    print_board()
                    w1 = [clist[0],clist[1],clist[2]]
                    w2 = [clist[3],clist[4],clist[5]]
                    w3 = [clist[6],clist[7],clist[8]]
                    w4 = [clist[0],clist[4],clist[8]]
                    w5 = [clist[2],clist[4],clist[6]]
                    w6 = [clist[1],clist[4],clist[7]]
                    w7 = [clist[0],clist[3],clist[6]]
                    w7 = [clist[2],clist[5],clist[8]]
                    win_check()
                    win_condition = win_check()
                    turn = 0
        else:
            turn = 1
            while not win_condition:
                if turn == 1:
                    print("Computer's turn!")
                    time.sleep(3)
                    decompile_list()
                    random_choice()
                    compile_list()
                    print_board()
                    w1 = [clist[0],clist[1],clist[2]]
                    w2 = [clist[3],clist[4],clist[5]]
                    w3 = [clist[6],clist[7],clist[8]]
                    w4 = [clist[0],clist[4],clist[8]]
                    w5 = [clist[2],clist[4],clist[6]]
                    w6 = [clist[1],clist[4],clist[7]]
                    w7 = [clist[0],clist[3],clist[6]]
                    w7 = [clist[2],clist[5],clist[8]]
                    win_check()
                    win_condition = win_check()
                    turn = 0
                else:
                    print("Your turn!\n")
                    choice = int(input("Choose a cell to place X: "))
                    decompile_list()
                    clist[choice-1] = " X "
                    compile_list()
                    print_board()
                    w1 = [clist[0],clist[1],clist[2]]
                    w2 = [clist[3],clist[4],clist[5]]
                    w3 = [clist[6],clist[7],clist[8]]
                    w4 = [clist[0],clist[4],clist[8]]
                    w5 = [clist[2],clist[4],clist[6]]
                    w6 = [clist[1],clist[4],clist[7]]
                    w7 = [clist[0],clist[3],clist[6]]
                    w7 = [clist[2],clist[5],clist[8]]
                    win_check()
                    win_condition = win_check()
                    turn = 1
    except ValueError:
        print("\nWrong value, type a number\n")
    print("GAME!\n")
