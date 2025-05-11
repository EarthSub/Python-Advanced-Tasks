# Create a class called EmailValidator. Upon initialization, it should receive:
#     · min_length (of the username; example: in "peter@gmail.com" "peter" is the username)
#     · mails (list of the valid mails; example: "gmail", "abv")
#     · domains (list of valid domains; example: "com", "net")

# Create three methods that should not be accessed outside the class:
#     · is_name_valid(name) - returns whether the name is greater than or equal to the min_length (True/False)
#     · is_mail_valid(mail) - returns whether the mail is in the possible mails list (True/False)
#     · is_domain_valid(domain) - returns whether the domain is in the possible domains list (True/False)

# Create one public method:
#     · validate(email) - using the three methods returns whether the email is valid (True/False)


# Examples

# Test Code                                                                   Output

# mails = ["gmail", "softuni"]                                                True
# domains = ["com", "bg"]                                                     False
# email_validator = EmailValidator(6, mails, domains)                         False
# print(email_validator.validate("pe77er@gmail.com"))                         False
# print(email_validator.validate("georgios@gmail.net"))
# print(email_validator.validate("stamatito@abv.net"))
# print(email_validator.validate("abv@softuni.bg"))



class EmailValidator:
    def __init__(self, min_length: int, _mails: list, _domains: list):
        self.min_length = min_length
        self.mails = _mails
        self.domains = _domains

    def __is_name_valid(self, name: str) -> bool:
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail) -> bool:
        return mail in self.mails

    def __is_domain_valid(self, domain: str) -> bool:
        return domain in self.domains

    def validate(self, email: str) -> bool:
        name, mail_part = email.split("@")
        mail, domain = mail_part.split(".")

        return self.__is_name_valid(name) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain)




mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
