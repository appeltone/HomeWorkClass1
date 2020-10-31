import os.path
from os import path

file_path = "E:\\temp\\names.txt"


def write_to_file():
    # create file if not exist and open for write OR open file if exists for append mode 'a'
    if (path.exists(file_path)):
        f = open(file_path, "a", encoding='utf-8')
    else:
        f = open(file_path, "x", encoding='utf-8')

    name = input("Please write your name: ")
    f.write(name + '\n')


def print_names_From_file():
    lines = []
    try:
        f = open(file_path, 'r', encoding='utf-8')
        lines = f.read().split('\n') # Instead of f.readlines(), because f.readlines() will print blank line for each \n
        for line in lines:
            if (line): # Prevent from the last \n (blank line) from being printed
                print("hello dear %s" % line)
    except FileNotFoundError:
        print("Given file does not exist!")
    finally:
        f.close()


for i in range(3):
    write_to_file()
print_names_From_file()
