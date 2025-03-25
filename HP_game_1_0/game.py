Saves = []
Available_cmds = []
current_level = 0
Prompt = ''
def menu():
    global Saves
    global Available_cmds
    global Prompt
    print('Hello!\nWelcome to the HP game 1!')
    if Saves:
        print('You have saved progress!\nIf you wanna continue, enter "C".')
        Available_cmds = ['C', 'N']
    else:
        Available_cmds = ['N']
    print('If you wanna start new game, enter "N".')
    Prompt = input()
    if Prompt in Available_cmds:
        if Prompt == 'N':
            print('Ok! Let\'s start!')
    else:
        print('Invalid input!!!')
        Prompt = input()
        if Prompt in Available_cmds:
            if Prompt == 'N':
                print('Ok! Let\'s start!')
        else:
            print('Invalid input!!! Please, restart the program!!!')
def game():
    menu()
