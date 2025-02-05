# White a function called sorting_cheeses that receives keywords arguments:

#     · The key represents the name of the cheese
#     · The value is a list of quantities (integers) of the pieces of the given cheese

# The function should return the cheeses and their pieces quantities sorted by the number of pieces of a cheese kind in descending order.
# If two or more cheeses have the same number of pieces, sort them by their names in ascending order (alphabetically).
# For each kind of cheese, return their piece quantities in descending order.

# For more clarifications, see the examples below.


#                                 Examples

# Input                                                           Output

# print(                                                          Camembert
#     sorting_cheeses(                                            500
#         Parmesan=[102, 120, 135],                               430
#         Camembert=[100, 100, 105, 500, 430],                    105
#         Mozzarella=[50, 125],                                   100
#     )                                                           100
# )                                                               Parmesan
#                                                                 135
#                                                                 120
#                                                                 102
#                                                                 Mozzarella
#                                                                 125
#                                                                 50

# Input                                                           Output

# print(                                                          Brie
#     sorting_cheeses(                                            150
#     Parmigiano=[165, 215],                                      125
#     Feta=[150, 515],                                            Feta
#     Brie=[150, 125]                                             515
#     )                                                           150
# )                                                               Parmigiano
#                                                                 215
#                                                                 165





def sorting_cheeses(**kwargs):
    sorted_data = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    result = ""

    for cheese_name, quantity in sorted_data:
        result += cheese_name + "\n"
        for element in sorted(quantity, reverse=True):
            result += f"{element}\n"
    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)

print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)
