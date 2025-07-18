import time
import function

now = time.strftime("%B %d, %Y %H:%M:%S")
print("It is : ", now)
while True:
    user_action =  input("Type Add, Show, Edit, Complete or Exit: ")
    user_action = user_action.strip()

    if user_action.startswith("Add"):
        todo = user_action[4:]

        todos = function.get_todos('todos.txt')

        todos.append(todo + '\n')

        function.write_todos('todos.txt', todos)

    elif user_action.startswith("Show"):
        
        todos = function.get_todos('todos.txt')

        for index, item in enumerate(todos):
            item = item.title()
            item =  item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("Edit"):
        try:
            number_action = int(user_action[5:])
            number_action = number_action - 1;

            todos = function.get_todos('todos.txt')

            new_todo = input("Enter New Todo: ")
            todos[number_action] = new_todo + '\n'

            function.write_todos('todos.txt', todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("Complete"):
        try:
            number =  int(user_action[9:])

            todos = function.get_todos('todos.txt')
            index = number - 1;
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            function.write_todos('todos.txt', todos)

            massage = f"Todo {todo_to_remove} was removed from the list"
            print(massage)
        except IndexError:
            print("Index is out of list.")
            continue

    elif 'Exit'  in user_action:
        print("Bye")
        break
    else:
        print("Command is not valid")
