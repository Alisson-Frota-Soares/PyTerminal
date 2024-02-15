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
            directories = name.split('/')
            for i in range(len(directories) - 1):
                if not os.path.exists('/'.join(directories[:i + 1])):
                    os.mkdir('/'.join(directories[:i + 1]))
            with open(name, 'w'):
                pass
        else:
            if '.' in name:
                with open(name, 'w'):
                    pass
            else:
                os.mkdir(name)

def delete_item(*names):
    for name in names:
        if '/' in name:
            if os.path.exists(name):
                if os.path.isdir(name):
                    shutil.rmtree(name)
                else:
                    os.remove(name)
            else:
                print("Item not found:", name)
        else:
            if os.path.exists(name):
                if os.path.isdir(name):
                    shutil.rmtree(name)
                else:
                    os.remove(name)
            else:
                for root, dirs, files in os.walk(".", topdown=False):
                    for file in files:
                        if file == name:
                            os.remove(os.path.join(root, file))
                    for dir in dirs:
                        if dir == name:
                            shutil.rmtree(os.path.join(root, dir))

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
            if len(parts) >= 2:
                delete_item(*parts[1:])
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
