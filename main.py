#print("Enter a todo:")
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
