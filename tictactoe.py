import random
import copy

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

size = 3
help = [[" 1 "," 2 "," 3 "],[" 4 "," 5 "," 6 "],[" 7 "," 8 "," 9 "]]
glist = []
clist = []
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
            clist[challenge] = " X "
            cchallenge = False
        else:
            cchallenge = True

decompile_list()
random_choice()
compile_list()
print_board()


