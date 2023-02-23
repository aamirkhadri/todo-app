#from functions import get_todos,set_todos
import functions
import time

now = time.strftime("%b %d %Y %H:%M:%S")
print("It is "+ now)
while True:

    user_action = input("enter add,show,exit,complete or edit: ")
    user_action = user_action.strip()
    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo+'\n')

        functions.set_todos(todos)
    elif user_action.startswith('show'):
        todos = functions.get_todos('todos.txt')

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}.{item}")
    elif user_action.startswith('edit'):
        try:
            indx = int(user_action[5:])
            indx = indx - 1

            todos = functions.get_todos()

            new_todo = input("Enter a new_todo")
            todos[indx] = new_todo

            functions.set_todos(todos)
        except ValueError:
            print("Your command is wrong")
            continue

    elif user_action.startswith('complete'):
        try:
            num = int(user_action[9:])

            todos = functions.get_todos()
            index = num - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            functions.set_todos(todos)
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("Index is out of range")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("command is not valid")

print("!bye")