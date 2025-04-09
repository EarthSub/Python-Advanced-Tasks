# Create a function named list_roman_emperors that receives information about various Roman emperors,
# their success status, and their rule length and returns a sorted result as one formatted string.
# It will receive an unknown number of arguments (tuples) and keyword arguments (key-value pairs).
# See the examples below.

# The arguments will be passed as follows:

#     · The first group of arguments will contain an unknown number of tuples with two elements
#         o The first element represents the Roman emperor's name (a valid string)
#         o The second element represents the success status of the emperor (a Boolean value)
#     · The second group will contain an unknown number of keyword arguments (key-value pairs)
#         o The key will represent the name of the emperor (a valid string)
#         o The value will represent the length of their rule (a positive integer)

# After receiving the data and calling the function:

#     · You should check each emperor's success status (True or False) and keep the information about them in
#       separate collections (you will have to sort them in the next steps)
#     · Sort the successful emperors by the length of their rule in descending order
#         o If there are emperors with the same length of rule, sort them alphabetically, in ascending order
#     · Sort the unsuccessful emperors by the length of their rule in ascending order
#         o If there are emperors with the same length of rule, sort them alphabetically, in ascending order
#     · The first line of your output string should contain the total number of all emperors:
#         o "Total number of emperors: {num_of_all_emperors}"
#     · Next, arrange the sorted data under the appropriate headings:
#         o For successful emperors (if any), use the heading "Successful emperors:"
#             § Skip the heading if there are no successful emperors
#         o For unsuccessful emperors (if any), use the heading "Unsuccessful emperors:"
#             § Skip the heading if there are no unsuccessful emperors
#         o Note that you may receive data either for successful or unsuccessful emperors and your output
#           should contain sorted information for the received type only. See the examples below.


# In the end, return the output as described below.

# Input

#     · There will be no input from the console, just parameters passed to your function

# Output

# · The returned output should look like this (each on a new line):
# "Total number of emperors: {num_of_all_emperors}"
# "Successful emperors:"
# "****{emperor_name1}: {number_of_years}"
# "****{emperor_name2}: {number_of_years}"
# ...
# "****{emperor_nameN}: {number_of_years}"
# "Unsuccessful emperors:"
# "****{emperor_name1}: {number_of_years}"
# "****{emperor_name2}: {number_of_years}"
# ...
# "****{emperor_nameN}: {number_of_years}"
#     o Prefix the name of each emperor with exactly four asterisks "****"
#     o Separate the name of the emperor and his years of rule with a colon and a single space ": "
#     o If you receive only one type of emperor (successful or unsuccessful), return only the type you've
#       got. Do not include the heading for the missing type in your formatted string. See the examples
#       below for clarification.

# Constraints

#     · The arguments will always be before the keyword arguments.
#     · Each tuple will always provide a unique name (a valid string) of the emperor and his status (a valid Boolean value).
#     · Each keyword argument will always provide a valid emperor's name
#       (a string that corresponds to the same emperor's name that will be in one of the tuples) and
#       his length of rule (a positive integer).

#     · You will always receive at least one tuple with the emperor's name and status and at least one valid
#       keyword argument containing the same emperor's name as a key.


#                                 Examples

# Test Code                                                       Output

# print(list_roman_emperors(("Augustus",                          Total number of emperors: 2
# True), ("Nero", False), Augustus=40,                            Successful emperors:
# Nero=14,))                                                      ****Augustus: 40
#                                                                 Unsuccessful emperors:
#                                                                 ****Nero: 14

# Test Code                                                       Output

# print(list_roman_emperors(("Augustus",                          Total number of emperors: 6
# True), ("Trajan", True), ("Nero", False),                       Successful emperors:
# ("Caligula", False), ("Pertinax", False),                       ****Augustus: 40
# ("Vespasian", True), Augustus=40,                               ****Trajan: 19
# Trajan=19, Nero=14, Caligula=4,                                 ****Vespasian: 19
# Pertinax=4, Vespasian=19,))                                     Unsuccessful emperors:
#                                                                 ****Caligula: 4
#                                                                 ****Pertinax: 4
#                                                                 ****Nero: 14

# Test Code                                                       Output

# print(list_roman_emperors(("Augustus",                          Total number of emperors: 3
# True), ("Trajan", True), ("Claudius",                           Successful emperors:
# True), Augustus=40, Trajan=19,                                  ****Augustus: 40
# Claudius=13,))                                                  ****Trajan: 19
#                                                                 ****Claudius: 13



def list_roman_emperors(*args, **kwargs):
    successful_emperors = {}
    unsuccessful_emperors = {}
    for name, success in args:
        if success:
            successful_emperors[name] = kwargs[name]
        else:
            unsuccessful_emperors[name] = kwargs[name]

    result = [f"Total number of emperors: {len(args)}"]

    if successful_emperors:
        result.append("Successful emperors:")
        sorted_successful_emperors = sorted(successful_emperors.items(), key=lambda x: (-x[1], x[0]))
        for name, years in sorted_successful_emperors:
            result.append(f"****{name}: {years}")

    if unsuccessful_emperors:
        result.append("Unsuccessful emperors:")
        sorted_unsuccessful_emperors = sorted(unsuccessful_emperors.items(), key=lambda x: (x[1], x[0]))
        for name, years in sorted_unsuccessful_emperors:
            result.append(f"****{name}: {years}")

    return "\n".join(result)



print(list_roman_emperors(("Augustus",
True), ("Nero", False), Augustus=40,
Nero=14,))

print(list_roman_emperors(("Augustus",
True), ("Trajan", True), ("Nero", False),
("Caligula", False), ("Pertinax", False),
("Vespasian", True), Augustus=40,
Trajan=19, Nero=14, Caligula=4,
Pertinax=4, Vespasian=19,))

print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Claudius", True),
                          Augustus=40, Trajan=19, Claudius=13,))
