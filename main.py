w1 = ["c","b","1"]
w2 = ["c","b","a"]
w3 = ["c","b","a"]
w4 = ["c","b","a"]
w5 = ["c","b","a"]
w6 = ["d","e","f"]
w7 = ["c","b","a"]
wlist = [w1,w2,w3,w4,w5,w6,w7]
winx = ["d","e","w"]
wino = ["d","e","g"]
win_condit = False

def win_check():
    ch = 0
    while ch != 7:
        if wlist[ch] == winx:
            win_condit = True
            ch = 7
            return win_condit
        elif wlist[ch] == wino:
            win_condit = True
            ch = 7
            return win_condit
        else:
            ch += 1
            win_condit = False
            return win_condit

print(wlist[5] == winx)
win_check()
win_condition = win_check()
print(win_condition)