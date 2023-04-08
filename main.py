#print("Enter a todo:")
prompt_enter = 'Enter a todo (blank to exit):'
prompt_ask = '(E)nter or (L)ist todos? (blank to exit):'

todos = []

response = input(prompt_ask)
response.lower()

while (not response.startswith('e') and not response.startswith('l')):
    response = input(prompt_ask)
    response.lower()

if (response.startswith('e')):
    response = input(prompt_enter)

    if len(response) > 0:
        todos.append(response.capitalize())

    while len(response) > 0:
        response = input(prompt_enter)
        if len(response) > 0:
            todos.append(response.capitalize())

    print("\nYour todos: ", todos)
else:
    print ("Your todos: ", todos)