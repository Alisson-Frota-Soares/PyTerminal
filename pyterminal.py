import os
import shutil

def list_directory():
    print("Current directory:", os.getcwd())
    contents = os.listdir('.')
    for item in contents:
        print(item)

def change_directory(directory):
    try:
        os.chdir(directory)
    except FileNotFoundError:
        print("Directory not found")
    except PermissionError:
        print("Permission denied to access directory")
    else:
        print("Current directory:", os.getcwd())

def create_item(*names):
    for name in names:
        if '/' in name:
            directory, filename = name.split('/')
            if directory not in os.listdir('.'):
                os.mkdir(directory)
            if filename:
                with open(os.path.join(directory, filename), 'w'):
                    pass
        else:
            if '.' in name:
                with open(name, 'w'):
                    pass
            else:
                os.mkdir(name)

def delete_item(name):
    try:
        if os.path.isdir(name):
            shutil.rmtree(name)
        else:
            os.remove(name)
    except FileNotFoundError:
        print("Item not found")
    except PermissionError:
        print("Permission denied to delete item")
    else:
        print("Item deleted successfully")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    print("Welcome to PyTerminal!")
    while True:
        command = input("$ ")
        parts = command.split()

        if not parts:
            continue

        if parts[0] == 'list':
            list_directory()
        elif parts[0] == 'cd':
            if len(parts) == 2:
                change_directory(parts[1])
            else:
                print("Usage: cd <path>")
        elif parts[0] == 'create':
            if len(parts) >= 2:
                create_item(*parts[1:])
            else:
                print("Usage: create <name>")
        elif parts[0] == 'del' or parts[0] == 'delete':
            if len(parts) == 2:
                delete_item(parts[1])
            else:
                print("Usage: del <item_name>")
        elif parts[0] == 'clear' or parts[0] == 'cls':
            clear_screen()
        elif parts[0] == 'exit':
            break
        else:
            print("Unknown command:", parts[0])

if __name__ == "__main__":
    main()
