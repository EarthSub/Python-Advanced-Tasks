# Create a program that will receive commands until the command "End". The commands can be:

#     · "Create-{file_name}" - Creates the given file with empty content. If the file already exists,
#         remove the existing text in it (as if the file is created again)
#     · "Add-{file_name}-{content}" - Append the content and a new line after it.
#         If the file does not exist, create it, and add the content
#     · "Replace-{file_name}-{old_string}-{new_string}" - Open the file and replace all the occurrences of the old string
#         with the new string. If the file does not exist, print: "An error occurred"
#     · "Delete-{file_name}" - Delete the file. If the file does not exist, print: "An error occurred"


#                     Example

# Input                                   Comment

# Create-file.txt                         The first command creates the empty file
# Add-file.txt-First Line                 After the first and second Add command, the content is:
# Add-file.txt-Second Line                First Line
# Replace-random.txt-Some-some            Second Line
# Replace-file.txt-First-1st              On the first Replace command, an error must occur
# Replace-file.txt-Second-2nd             After the next two Replace commands, the content is:
# Delete-random.txt                       1st Line
# Delete-file.txt                         2nd Line
# End                                     After the first Delete command, an error occurs
#                                         Finally, the 'file.txt' file is deleted



import os



while True:
    command = input().strip()
    if command == "End":
        break

    command_parts = command.split("-")
    action = command_parts[0]
    file_name = command_parts[1]

    if action == "Create":
        with open(file_name, "w") as file:
            pass

    elif action == "Add":
        content = command_parts[2]
        with open(file_name, "a") as file:
            file.write(content + "\n")

    elif action == "Replace":
        old_string = command_parts[2]
        new_string = command_parts[3]
        try:
            with open(file_name, "r") as file:
                content = file.read()
            content = content.replace(old_string, new_string)
            with open(file_name, "w") as file:
                file.write(content)
        except FileNotFoundError:
            print("An error occurred")

    elif action == "Delete":
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")
