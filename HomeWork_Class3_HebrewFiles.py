try:
    a = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero")

# files homework
import os.path
from os import path

file_path = "E:\\temp\\words.txt"
# create file if not exist and open for write OR open file if exists for append mode 'a'
if (path.exists(file_path)):
    f = open(file_path, "a", encoding='utf-8')
else:
    f = open(file_path, "x", encoding='utf-8')

f.write("Eran Appel \n")
f.write("אלון אפל")
f.write("\n")

# open file for read utf-8
f = open(file_path, "r", encoding='utf-8')
print("----------------------")
print("File content: ")
print(f.read())
f.close()
