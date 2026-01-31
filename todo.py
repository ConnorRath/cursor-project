# This list will store all todo items
todos = []


def show_menu():
    print("\nTodo App")
    print("1. Show todos")
    print("2. Add todo")
    print("3. Complete todo")
    print("4. Delete todo")
    print("5. Exit")


def show_todos():
    if len(todos) == 0:
        print("\nNo todos yet.")
        return

    print("\nTodos:")
    for index, todo in enumerate(todos):
        status = "✓" if todo["completed"] else " "
        print(f"{index + 1}. [{status}] {todo['text']}")


def add_todo():
    text = input("\nEnter todo text: ").strip()

    if text == "":
        print("Todo cannot be empty.")
        return

    todo = {
        "text": text,
        "completed": False
    }

    todos.append(todo)
    print("Todo added.")


def complete_todo():
    show_todos()

    if len(todos) == 0:
        return

    try:
        choice = int(input("\nEnter todo number to complete: "))
        index = choice - 1

        if index < 0 or index >= len(todos):
            print("Invalid todo number.")
            return

        todos[index]["completed"] = True
        print("Todo marked as completed.")

    except ValueError:
        print("Please enter a number.")


def delete_todo():
    show_todos()

    if len(todos) == 0:
        return

    try:
        choice = int(input("\nEnter todo number to delete: "))
        index = choice - 1

        if index < 0 or index >= len(todos):
            print("Invalid todo number.")
            return

        removed = todos.pop(index)
        print(f"Deleted todo: {removed['text']}")

    except ValueError:
        print("Please enter a number.")


def main():
    while True:
        show_menu()
        choice = input("\nChoose an option: ")

        if choice == "1":
            show_todos()
        elif choice == "2":
            add_todo()
        elif choice == "3":
            complete_todo()
        elif choice == "4":
            delete_todo()
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
