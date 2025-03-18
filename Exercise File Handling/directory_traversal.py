# Write a program that traverses a given directory for all files.
# Search through to the first nested level of the directory (inclusive)
# and write information about each file you find into the report.txt file.
# The files should be grouped by their extension.
# Extensions should be ordered by name alphabetically.
# The files with extensions should also be sorted by name.
# The report.txt file should be saved in the chosen directory.


# Examples
# Input
# .


import os


directory_path = input()

files_by_extension = {}

try:
    for file in os.listdir(directory_path):
        path = os.path.join(directory_path, file)
        if os.path.isfile(path):
            file_name, extension = file.split(".")
            if extension not in files_by_extension:
                files_by_extension[extension] = []
            files_by_extension[extension].append(file)
except FileNotFoundError:
    print("Invalid dir name or path to dir!")


result = ""
for extension, files in sorted(files_by_extension.items(), key=lambda x: x[0]):
    result += f".{extension}\n"
    for file_name in sorted(files):
        result += f"- - - {file_name}\n"

with open("report.txt", "w") as file:
    file.write(result)
