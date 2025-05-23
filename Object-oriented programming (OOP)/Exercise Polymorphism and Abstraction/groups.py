# Create a class called Person. Upon initialization, it will receive a name (str) and a surname (str).
# Implement the needed magic methods so that:

#     · Each person could be represented by their names, separated by a single space.
#     · When you concatenate two people, you should return a new instance of a person who will
#       take the first name from the first person and the surname from the second person.

# Create another class called Group. Upon initialization, it should receive a name (str) and
# people (list of Person instances). Implement the needed magic methods so that:

# · When you access the length of a group instance, you should receive the total number of people in the group.
# · When you concatenate two groups, you should return a new instance of a group which will have a name-string in the format
#   "{first_name} {second_name}" and all the people in the two groups will participate in the new one too.
# · Each group should be represented in the format "Group {name} with members {members' names separated by comma and space}"
# · You could iterate over a group, and each person (element of the group) should be represented in the format "Person {index}: {person's name}"


#                                 Examples

# Test Code                                                               Output

# p0 = Person('Aliko', 'Dangote')                                           3
# p1 = Person('Bill', 'Gates')                                              Group Special with members Elon Musk,Warren Musk
# p2 = Person('Warren', 'Buffet')                                           Person 0: Aliko Dangote
# p3 = Person('Elon', 'Musk')                                               Person 0: Aliko Dangote
# p4 = p2 + p3                                                              Person 1: Bill Gates
#                                                                           Person 2: Warren Buffet
# first_group = Group('__VIP__', [p0, p1, p2])                              Person 3: Elon Musk
# second_group = Group('Special', [p3, p4])                                 Person 4: Warren Musk
# third_group = first_group + second_group

# print(len(first_group))
# print(second_group)
# print(third_group[0])
#
# for person in third_group:
#     print(person)



from typing import List


class Person:

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other: "Person"):
        return Person(self.name, other.surname)



class Group:

    def __init__(self, name: str, people: List[Person]):
        self.name = name
        self.people = people


    def __len__(self):
        return len(self.people)

    def __add__(self, other: "Group"):
        return Group(f"{self.name} {other.name}", self.people + other.people)

    def __repr__(self):
        return f"Group {self.name} with members {', '.join(repr(n) for n in self.people)}"

    def __getitem__(self, index: int):
        return f"Person {index}: {self.people[index]}"


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3


first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group


print(len(first_group))
print(second_group)
print(third_group[0])


for person in third_group:
    print(person)
