Claro! Aqui está o README.md atualizado com as novas features:

---

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
- `create <name>`: Creates a file or folder. The command automatically determines whether to create a file or a folder. It can create multiple folders, subfolders, and files with a single command. For example:
  ```bash
  $ create folder1/another_folder/etc.../file.py
  ```
  or:
  ```bash
  $ create folder1/another_folder/file.py folder2/file2.py etc....
  ```
- `del <item_name>` or `delete <item_name>`: Deletes the specified item (file or folder). It can delete multiple files or folders at once. Additionally, it can delete files or folders within a directory. For example:
  ```bash
  $ del folder1 folder2 main.py
  $ del folder1/main.py
  $ del folder1/folder2/main.py
  ```
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