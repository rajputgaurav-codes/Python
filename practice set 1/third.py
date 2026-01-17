"""write a program to print the contents of a directory using the os module.
search online for the function which does that"""

import os

# specify the directory you want to list
directory_path = "/"  # change this to any folder you want

# get list of files and folders
contents = os.listdir(directory_path)

# print each item
for item in contents:
    print(item)
