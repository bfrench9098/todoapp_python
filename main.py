# Very simple command line based menu to enter strings

# When prompted enter either "enter" or "list" or press enter to exit.
#  If you are entering todos, you will be prompted to enter a string.
#  (1) Strings are "stripped" of leading and trailing spaces.
#  (2) Strings are "capitalized".

# Strings go into a list but are currently not saved to a file

# If you are listing, you will see the string you entered or you
#   will see "You don't have any todos" if you did not enter any
#   strings.

prompt_enter = 'Enter a todo (blank to exit):'
prompt_ask = 'Enter or List todos? ([Ee]nter | [Ll]ist |  blank to exit:'

todos = []

exit = False
actionValid = False

while (exit == False):
    response = input(prompt_ask).strip()
    action = response.lower()

    if len(action) == 0:
        action = 'exitApp'

    match action:
        case 'enter':
            actionValid = True
        case 'list':
            actionValid = True
        case 'exitApp':
            break

    if ((actionValid == True) and (exit == False)):
        if (action == 'enter'):
            response = input(prompt_enter).strip()

            if len(response) > 0:
                todos.append(response.capitalize())

            while len(response) > 0:
                response = input(prompt_enter).strip()

                if len(response) > 0:
                    todos.append(response.capitalize())

        elif (action == 'list'):
            print('\nYour Todos:')

            if (todos.__len__() > 0):
                for item in todos:
                    print("\t", item)

                print("")
            else:
                print('\t', "You don't have any todos\n")
