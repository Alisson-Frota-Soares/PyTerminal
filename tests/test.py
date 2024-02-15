import os
import time

def test_list():
    print("Testing 'list' command:")
    os.system("python ../pyterminal.py list")

def test_cd():
    print("\nTesting 'cd' command:")
    os.system("python ./pyterminal.py cd test_folder")

def test_create():
    print("\nTesting 'create' command:")
    os.system("python ./pyterminal.py create test_folder")
    os.system("python ./pyterminal.py create test_folder/test_file.txt")

def test_delete():
    print("\nTesting 'delete' command:")
    os.system("python ./pyterminal.py delete test_folder/test_file.txt")

def test_clear():
    print("\nTesting 'clear' command:")
    os.system("python ./pyterminal.py clear")

def main():
    os.system("cd ..")
    test_list()
    time.sleep(3)
    test_cd()
    time.sleep(3)
    test_create()
    time.sleep(3)
    test_delete()
    time.sleep(3)
    test_clear()

if __name__ == "__main__":
    main()
