#print("Enter a todo:")
prompt_enter = 'Enter a todo (blank to exit):'
prompt_ask = 'Enter or List todos? ([Ee]nter | [Ll]ist |  blank to exit:'

todos = []

exit = False

while (exit == False):
    response = input(prompt_ask)
    action = response.lower()

    if len(action) == 0:
        action = 'exit'

    match action:
        case 'enter':
            exit = True
        case 'list':
            exit = True
        case 'exit':
            exit = True
            action = ''

if (action.startswith('e')):
    response = input(prompt_enter)

    if len(response) > 0:
        todos.append(response.capitalize())

    while len(response) > 0:
        response = input(prompt_enter)
        if len(response) > 0:
            todos.append(response.capitalize())

    print('\nYour Todos:')
    for item in todos:
        print("\t", item)

    # print("\nYour todos: ", todos)
elif (action.startswith('l')):
    print('\nYourTodos:')
    for item in todos:
        print("\t", item)

    # print ("\nYour todos: ", todos)