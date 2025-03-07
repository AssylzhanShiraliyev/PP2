# Python Directories and Files exercises

import os  

# 1. Write a Python program to list only directories, files and all directories, files in a specified path

path = input("Enter the path: ")

if os.path.exists(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    all_contents = os.listdir(path)

    print("Directories:", directories)
    print("Files:", files)
    print("All directories and files:", all_contents)
else:
    print("The specified path does not exist.")

# 2. Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
path = input("Enter the path: ")

print("Existence:", os.access(path, os.F_OK))
print("Readability:", os.access(path, os.R_OK))
print("Writability:", os.access(path, os.W_OK))
print("Executability:", os.access(path, os.X_OK))

# 3. Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path

path = input("Enter the path: ")

if os.path.exists(path):
    print("The path exists.")
    print("Filename:", os.path.basename(path))
    print("Directory portion:", os.path.dirname(path))
else:
    print("The path does not exist.")

# 4. Write a Python program to count the number of lines in a text file

filename = input("Enter the file name: ")

if os.path.exists(filename) and os.path.isfile(filename):
    with open(filename, "r") as file:
        counter = sum(1 for line in file)

    print("Number of lines in the file:", counter)
else:
    print("File not found.")

# 5. Write a Python program to write a list to a file

items = input("Enter the list items separated by commas: ").split(",")
filename = input("Enter the file name: ")

with open(filename, "w") as file:
    file.writelines(item.strip() + "\n" for item in items)

print("The list is written to a file:", filename)

# 6. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

directory = input("Enter the path to save the files (leave it empty for the current folder): ").strip()

for i in range(65, 91):  
    filename = os.path.join(directory, f"{chr(i)}.txt") if directory else f"{chr(i)}.txt"
    with open(filename, "w") as file:
        file.write(f"The {chr(i)}.txt file has been created.\n")

print("Files A-Z have been successfully created.")

# 7. Write a Python program to copy the contents of a file to another file

source = input("Enter the name of the source file: ")
destination = input("Enter the name of the destination file: ")

if os.path.exists(source) and os.path.isfile(source):
    with open(source, "r") as src, open(destination, "w") as dest:
        dest.write(src.read())

    print("The file was copied successfully:", destination)
else:
    print("The source file was not found.")

# 8. Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not

path = input("Enter the path: ")

if os.path.exists(path) and os.path.isfile(path):
    if os.access(path, os.W_OK):
        os.remove(path)
        print("The file was deleted successfully.")
    else:
        print("There are no rights to delete the file.")
else:
    print("The file does not exist or the wrong path is specified.")
