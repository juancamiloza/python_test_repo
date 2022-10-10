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


print_board()

print_help()