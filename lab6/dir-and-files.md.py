#esep 1
import os

def list_contents(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    all_items = os.listdir(path)
    
    return directories, files, all_items

path = "."  # Change this to the desired path
dirs, files, all_items = list_contents(path)

print("Directories:", dirs)
print("Files:", files)
print("All items:", all_items)

#esep 2

import os

def check_access(path):
    return {
        "Exists": os.path.exists(path),
        "Readable": os.access(path, os.R_OK),
        "Writable": os.access(path, os.W_OK),
        "Executable": os.access(path, os.X_OK),
    }

path = "example.txt"  # Change this to the desired path
access_info = check_access(path)

for key, value in access_info.items():
    print(f"{key}: {value}")

#esep 3

import os

def path_info(path):
    if os.path.exists(path):
        return {
            "Directory": os.path.dirname(path),
            "Filename": os.path.basename(path),
        }
    else:
        return "Path does not exist."

path = "example.txt"  # Change this to the desired path
info = path_info(path)

print(info)

#esep 4

def count_lines(filename):
    with open(filename, 'r') as file:
        return sum(1 for _ in file)

filename = "example.txt"  # Change this to the desired file
print("Number of lines:", count_lines(filename))

#esep 5

def write_list_to_file(filename, data):
    with open(filename, 'w') as file:
        file.writelines("\n".join(data))

data = ["Apple", "Banana", "Cherry"]
filename = "output.txt"

write_list_to_file(filename, data)

#esep 6

import string

for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as file:
        file.write(f"This is {letter}.txt")

#esep 7 

def copy_file(source, destination):
    with open(source, 'r') as src, open(destination, 'w') as dest:
        dest.write(src.read())

source_file = "source.txt"  # Change this to the actual source file
destination_file = "destination.txt"  # Change this to the desired destination file

copy_file(source_file, destination_file)

#esep 8

import os

def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        print(f"{path} has been deleted.")
    else:
        print("File does not exist or access is denied.")

file_path = "example.txt"  # Change this to the desired file path
delete_file(file_path)
