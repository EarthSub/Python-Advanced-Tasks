# Create a class called Programmer. Upon initialization, it should receive - name (string), language (string),
# and skills (integer). The class should have two methods:

#     - watch_course(course_name, language, skills_earned)
#         o If the programmer's language is the same as the one on the course, increase his skills with the given amount and return a message "{name} watched {course_name}".
#         o Otherwise return "{name} does not know {language}".
#     - change_language(new_language, skills_needed)
#         o If the programmer has the skills and the new language is not the same as his,
#           change his language to the new one and return "{name} switched from {previous_language} to {new_language}".
#         o If the programmer has the skills, but the given language is equal to his return "{name} already knows {language}".
#         o In the last case, the programmer does not have enough skills, so return "{name} needs {needed_skills} more skills" and do not change his language.

# Submit only the class in the judge system.


#                                 Examples

# Test Code                                                           Output

# programmer = Programmer("John", "Java", 50)                         John does not know Python
# print(programmer.watch_course("Python                               John already knows Java
# Masterclass", "Python", 84))                                        John needs 50 more skills
# print(programmer.change_language("Java", 30))                       John watched Java: zero to hero
# print(programmer.change_language("Python", 100))                    John switched from Java to Python
# print(programmer.watch_course("Java: zero to                        John watched Python Masterclass
# hero", "Java", 50))
# print(programmer.change_language("Python", 100))
# print(programmer.watch_course("Python
# Masterclass", "Python", 84))


class Programmer:
    def __init__(self, name: str, language: str, skills: int):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self,course_name: str, language: str, skills_earned: int) -> str:
        if self.language == language:
            self.skills += skills_earned
            return f"{self.name} watched {course_name}"
        return f"{self.name} does not know {language}"

    def change_language(self,new_language: str, skills_needed: int) -> str:
        if self.skills >= skills_needed and self.language != new_language:
            previous_language = self.language
            self.language = new_language
            return f"{self.name} switched from {previous_language} to {new_language}"
        if self.skills >= skills_needed and self.language == new_language:
            return f"{self.name} already knows {new_language}"
        return f"{self.name} needs {skills_needed - self.skills} more skills"



programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))
