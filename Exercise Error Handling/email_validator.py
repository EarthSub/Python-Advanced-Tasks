# You will be given some emails until you receive the command "End".
# Create the following custom exceptions to validate the emails:

#     · NameTooShortError - raise it when the name in the email is less than or equal to 4 ("peter" will be the name in the email "peter@gmail.com")
#     · MustContainAtSymbolError - raise it when there is no "@" in the email
#     · InvalidDomainError - raise it when the domain of the email is invalid (valid domains are: .com, .bg, .net, .org)

# When an error is encountered, raise it with an appropriate message:

#     · NameTooShortError - "Name must be more than 4 characters"
#     · MustContainAtSymbolError - "Email must contain @"
#     · InvalidDomainError - "Domain must be one of the following: .com, .bg, .org, .net"

# Hint: use the following syntax to add a message to the Exception: MyException("Exception Message")
# If the current email is valid, print "Email is valid" and read the next one.


#             Examples

# Input                   Output

# abc@abv.bg              Traceback (most recent call last):
# End                         File ".\email_validator.py", line 20, in <module>
#                                 raise NameTooShortError("Name must be more than 4 characters")
#                         __main__.NameTooShortError: Name must be more than 4 characters

# Input                   Output

# peter@gmail.com         Email is valid
# petergmail.com          Traceback (most recent call last):
# End                         File ".\email_validator.py", line 18, in <module>
#                                 raise MustContainAtSymbolError("Email must contain @")
#                         __main__.MustContainAtSymbolError: Email must contain @

# Input                   Output

# peter@gmail.hotmail     Traceback (most recent call last):
# End                         File ".\email_validator.py", line 22, in <module>
#                                 raise InvalidDomainError("Domain must be one of the folowing:
#                         .com, .bg, .org, .net")
#                         __main__.InvalidDomainError: Domain must be one of the folowing:
#                         .com, .bg, .org, .net


class MustContainAtSymbolError(Exception):
    pass


class NameTooShortError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


HOST_PART_MIN_LENGTH = 5
VALID_DOMAINS = {".com", ".bg", ".net", "org"}

while True:
    email = input()
    if email == "End":
        break

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    host_part = email.split("@")[0]
    if len(host_part) < HOST_PART_MIN_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")

    valid = False
    for domain in VALID_DOMAINS:
        if domain in email:
            valid = True
    if not valid:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
