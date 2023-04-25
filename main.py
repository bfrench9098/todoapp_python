import os.path
import sys

# Very simple command line based menu to enter strings

# When prompted enter either "enter" or "list" or press enter to exit.
#  If you are entering todos, you will be prompted to enter a string.
#  (1) Strings are "stripped" of leading and trailing spaces.
#  (2) Strings are "capitalized".

# Strings go into a list but are currently not saved to a file

# If you are listing, you will see the string you entered or you
#   will see "You don't have any todos" if you did not enter any
#   strings.

### START OF FUNCTIONS
#--------------------------------------------------
#listTodos - List all todos entered by the user
#--------------------------------------------------
def listTodos():
    print('\nYour Todos:')

    if (len(todos) > 0):
        itemNo = 0

        for idx, item in enumerate(todos):
            itemNo = itemNo + 1
            print("\t", "(", (idx + 1), ")", item)

        print("")
    else:
        print('\t', "You don't have any todos\n")

#--------------------------------------------------
#enterTodos - Allow the user to enter todos
#--------------------------------------------------
def enterTodos():
    response = input(prompt_enter).strip()

    if len(response) > 0:
        todos.append(response.capitalize())

    while len(response) > 0:
        response = input(prompt_enter).strip()

        if len(response) > 0:
            todos.append(response.capitalize())

#--------------------------------------------------
#editTodos - Allow the user to edit their todos
#--------------------------------------------------
def editTodos():
    listTodos()
    response = input(prompt_edit).strip()

    if len(response) > 0:
        if response.isnumeric():
            itemNo = int(response)
            if itemNo > len(todos) or itemNo == 0:
                print('ERROR! - Item number ', itemNo, ' is not in the list')
            else:
                itemNo = itemNo - 1

                strResponse = input(prompt_replace).strip()
                if len(strResponse) > 0:
                    todos[itemNo] = strResponse.capitalize()
                    print('Your todos have been updated')
                    listTodos()
        else:
            print('ERROR! - ', response, ' is not valid. Enter an item number from the list')

#--------------------------------------------------
#completeTodos - Allow the user to edit their todos
#--------------------------------------------------
def completeTodos():
    listTodos()
    response = input(prompt_complete).strip()

    if len(response) > 0:
        if response.isnumeric():
            itemNo = int(response)
            if itemNo > len(todos) or itemNo == 0:
                print('ERROR! - Item number ', itemNo, ' is not in the list')
            else:
                itemNo = itemNo - 1
                todos.pop(itemNo)
                print('Item ', response, ' marked complete and removed. Todos updated.')
                listTodos()
        else:
            print('ERROR! - ', response, ' is not valid. Enter an item number from the list')

#--------------------------------------------------
#loadFromFile - Load todos from text file
#--------------------------------------------------
def loadFromFile(todos):
    ### first see if the file exists - using default name "todos.txt"
    myFile = 'todos.txt'
    f = None

    if os.path.exists(myFile):
        ### if found then load todos[] from file
        try:
            f = open(myFile, "r+")
        except:
            print("ERROR! Could not open ", myFile)
            sys.exit(1)

        for line in f:
            line = line.strip('\n')
            todos.append(line)

    return f

#--------------------------------------------------
#writeToFile - Write todos to a file
#--------------------------------------------------
def writeToFile(f, todos):
    ### first see if the file exists - using default name "todos.txt"
    myFile = 'todos.txt'

    ### if found then truncate file and write any data in todos[]
    if f == None:
        try:
            f = open(myFile, 'w')
        except:
            print('ERROR! Error opening ', myFile, 'for write')
            sys.exit(1)
    else:
        f.seek(0)
        f.truncate()

    if len(todos) > 0:
        for todo in todos:
            todo = todo + '\n'
            f.write(todo)

        f.close()
### END OF FUNCTIONS

prompt_enter = 'Enter a todo (blank to exit):'
prompt_edit = 'Enter the number of the todo to edit (blank to exit):'
prompt_complete = 'Enter the number of the todo to mark completed (blank to exit):'
prompt_replace = 'Enter the replacement todo (blank to exit):'
prompt_ask = 'Enter, Edit, Complete or List todos? (blank to exit):'

todos = []

f = loadFromFile(todos)

print('PROGRAM START: todos loaded from file', len(todos), '\n')

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
        case 'edit':
            actionValid = True
        case 'list':
            actionValid = True
        case 'complete':
            actionValid = True
        case 'exitApp':
            try:
                writeToFile(f, todos)
            except:
                print('ERROR! Error writing to or closing todos file')
                sys.exit(1)

            print('\nPROGRAM END: todos written to file', len(todos), '\n')

            break
        case other:
            print('ERROR! That is not a valid option.')

    if ((actionValid == True) and (exit == False)):
        if (action == 'enter'):
            enterTodos()
        elif (action == 'list'):
            listTodos()
        elif (action == 'edit'):
            editTodos()
        elif (action == 'complete'):
            completeTodos()

