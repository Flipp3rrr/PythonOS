print("""
Welcome to

  _____            _____                         _       _
 / ___ \          |  __ \                       | |   __| |__
| |   | |         | |  \ \                      | |  |__   __|
| |   | |         | |   \ \    ______   _______ | |  __ | |       ______     _____
| |___| | _    _  | |    | |  /  ___/  /  ____/ | | / / | |      /  __  \   / ___ \ 
|  ____/ | |  | | | |    | | | |_____  \____ \  | |/ /  | |     |  /  \  | | |   | |
| |      | |  | | | |   / /  |  ____/       \ \ |   <   | |     | |    | | | |   | |
| |      | |__| | | |__/ /   | |_____  _____/ / | |\ \  | |____ |  \__/  | | |___| |
|_|       \___  | |_____/     \_____/  \_____/  |_| \_\ \_____/  \______/  |  ____/
         _____| |                                                          | |
         \______/                                                          |_|

The free and open-source cross-platform desktop environment written in Python.

===
""")

# import modules which are needed later
# - sys
# - time
print("Importing modules...")
try:
    import sys
    import time
    print("Imported modules succesfully!")

except Exception as error: 
    print('ERR$', error) 

# random gibberish that looks cool
print("PythonOS booted succesfully!")
print("Looking for desktop environment...")
print("No desktop environment found!")
print("Booting to shell...")
print("Shell ready!")
print()
print("WARN$ Files are not encrypted!")
print()
print("Welcome to PythonOS!")

# login screen, asks for user and password


# basic shell, maybe this shouldn't be here but it is for now
while True:
    cmd = input("SHELL> ")
    
    if cmd == "help":
        print("""
        Basic commands:
            help: display help text
            exit: stop PythonOS
            ls: Show directory contents
            cd: Go to direcotry
        """)

    if cmd == "shutdown":
        # TO DO!!
        print("FEATURE IS //TBD//")
        sys.exit()

    if cmd == "ls":
        # TO DO!!
        print("FEATURE IS //TBD//")
    
    if cmd == "cd":
        # TO DO!!
        print("FEATURE IS //TBD//")
