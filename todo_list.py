import json
from typing import List


def is_empty() -> bool:
    todos: List[str] = data.get("todos", [])
    return not bool(todos)


def save_list():
    with open('todo_list.json', "w") as file:
        json.dump(data, file)


def list_todos():
    todos: List[str] = data.get("todos", [])

    if not todos:
        print("❌ No todos")
        return

    for count, list_item in enumerate(todos, start=1):
        print(f"{count}. {list_item}")


def should_cancel(input_text: str) -> bool:
    return input_text in ["back"]


def new_todo():
    user_input = input("Input todo: ")

    if should_cancel(user_input):
        return

    data["todos"].append(user_input)

    print("\n✅ Todo added")
    save_list()


def remove_todo():
    if is_empty():
        print("❌ No todos")
        return

    while True:
        list_todos()
        user_input = input("\nWhich item do you want to remove? ")

        if should_cancel(user_input):
            return

        try:
            item_pos = int(user_input) - 1
        except ValueError:
            print("❌ Not a valid item")
            continue
        try:
            if item_pos < 0:
                raise IndexError

            data["todos"].pop(item_pos)
            break
        except IndexError:
            print("❌ Not a valid item")

    print("\n✅ Removed")
    save_list()


def edit_todo():
    if is_empty():
        print("❌ No todos")
        return

    while True:
        list_todos()

        user_input = input("\nWhich item do you want to edit? ")

        if should_cancel(user_input):
            return

        try:
            item_pos = int(user_input)
        except ValueError:
            print("❌ Not a valid item")
            continue
        try:
            if item_pos > len(data["todos"]) or item_pos < 1:
                raise IndexError

            data["todos"][item_pos - 1] = input("Edit: ")
            break
        except IndexError:
            print("❌ Not a valid item")

    print("\n✅ Changed")
    save_list()


try:
    with open('todo_list.json', "r") as json_file:
        data = json.load(json_file)
except FileNotFoundError:
    data = {"todos": []}

while True:
    option: str = input("\n✨ What would you like to do?\n(n) - new todo\n(l) - list todos" +
                        "\n(r) - remove todo\n(e) - edit todo" +
                        "\n(q) - quit\nType 'back' at any time to return\n> ").lower()
    print("")

    if option in ["n", "new", "new todo"]:
        new_todo()

    elif option in ["l", "list", "list todo", "list todos"]:
        list_todos()

    elif option in ["r", "remove", "remove todo"]:
        remove_todo()

    elif option in ["e", "edit", "edit todo"]:
        edit_todo()

    elif option in ["q", "quit", "exit", "bye"]:
        break

    elif should_cancel(option):
        print("❓ Did you mean to exit the program?  If so, type 'quit'")

    else:
        print("❌ Invalid option")
