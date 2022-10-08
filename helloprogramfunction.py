def program_name(pname):
    challenge = False
    first_action = ""
    program_states = ["Q","QUIT"]
    print(f"Welcome to {pname}")
    first_action = str.upper(input("Press ENTER to continue, write QUIT to exit "))
    while challenge is False:
        if first_action in program_states:
            exit()
        elif len(first_action) == 0:
            challenge = True
        else:
            first_action = str.upper(input("Press ENTER to continue, write QUIT to exit "))


program_name("")


