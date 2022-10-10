#-------------------------------------------------
# import hello
#
# program_state = True           # Insert the heading in new app
#                                # Replace "app" with your app's name
# while program_state:
#
#     hello.program_name("app")
#--------------------------------------------------

import time


def program_name(pname):
    app_challenge = True
    program_states = ["Q", "QUIT"]
    print(f"Welcome to {pname}")
    first_action = str.upper(input("Press ENTER to continue, write QUIT to exit "))
    while app_challenge:
        if first_action in program_states:
            print(f"Thank you for using {pname}")
            time.sleep(5)
            exit()
        elif len(first_action) == 0:
            break
        else:
            print("Wrong command")
            first_action = str.upper(input("Press ENTER to continue, write QUIT to exit "))
