# PyTerminal

PyTerminal is an interactive terminal in Python that allows you to navigate the file system, create folders and files, and perform basic file management operations. It provides a user-friendly interface to interact with the file system using familiar terminal commands.

## How to Use

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Alisson-Frota-Soares/PyTerminal.git
   ```

2. Navigate to the project directory:
   ```bash
   cd PyTerminal
   ```

### Execution

Run the Python script `pyterminal.py`:
```bash
python pyterminal.py
```

### Available Commands

- `list`: Lists the contents of the current directory.
- `cd <path>`: Navigates to the specified directory.
- `create <name>`: Creates a file or folder. The command automatically determines whether to create a file or a folder. Multiple files or folders can be created at once by passing more than one parameter. For example:
  ```bash
  $ create folder1 folder2 main.py
  ```
  This command will create folders named `folder1` and `folder2`, and a file named `main.py`.
  It's also capable of creating a directory and a file inside that directory, for example:
  ```bash
  $ create folder1/main.py
  ```
- `del <item_name>` or `delete <item_name>`: Deletes the specified item (file or folder).
- `clear` or `cls`: Clears the console screen.
- `exit`: Exits PyTerminal.

### Usage Examples

- List the contents of the current directory:
  ```bash
  $ list
  ```

- Navigate to a specific directory:
  ```bash
  $ cd destination_folder
  ```

- Create a new folder or file:
  ```bash
  $ create new_folder
  $ create new_file.txt
  ```

- Delete an item:
  ```bash
  $ del file.txt
  ```

- Clear the console screen:
  ```bash
  $ clear
  ```

### Contributing

Contributions are welcome! Feel free to open an issue to discuss changes or propose a pull request.

### License

This project is licensed under the [MIT License](LICENSE).

--- 