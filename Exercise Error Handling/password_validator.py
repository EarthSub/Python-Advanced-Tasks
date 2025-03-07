# You will receive passwords as input on new lines, until the command "Done".
# Your task is to validate if the passwords are strong by applying the following validations:

#     · Each password should be at least 8 characters long, otherwise, PasswordTooShortError should be raised.
#     · If the password consists of only digits, only letters, or only special characters,
#         PasswordTooCommonError should be raised.
#     · Each password should have at least 1 special character, otherwise, PasswordNoSpecialCharactersError should be raised.
#         The special characters are "@", "*", "&", and "%".
#     · If the password contains empty spaces, PasswordContainsSpacesError should be raised.

# When an error is encountered, raise it with an appropriate message:

#     · PasswordTooShortError - "Password must contain at least 8 characters"
#     · PasswordTooCommonError -"Password must be a combination of digits, letters, and special characters"
#     · PasswordNoSpecialCharactersError - "Password must contain at least 1 special character"
#     · PasswordContainsSpacesError -"Password must not contain empty spaces"

# If the current password is valid, print "Password is valid" and read the next one.


#             Examples

# Input                       Output

# 1234qwer@                   Password is valid
# Done

# Input                       Output

# Qazxwj21                    Traceback (most recent call last):
# Done                            File ".\password_validator.py", line 65, in <module>
#                                     raise PasswordNoSpecialCharactersError('Password must contain
#                             at least 1 special character')
#                             PasswordNoSpecialCharactersError: Password must contain at least 1
#                             special character

# Input                       Output

# Password                    Traceback (most recent call last):
# Done                            File ".\password_validator.py", line 67, in <module>
#                                     raise PasswordTooCommonError('Password must be a combination
#                             of digits, letters, and special characters')
#                             PasswordTooCommonError: Password must be a combination of digits,
#                             letters, and special characters

# Input                       Output

# zjL2k 1#@                   Traceback (most recent call last):
# Done                            File ".\password_validator.py", line 66, in <module>
#                                     raise PasswordContainsSpacesError('Password must not contain
#                             empty spaces')
#                             PasswordContainsSpacesError: Password must not contain empty
#                             spaces

# Input                       Output

# 12345q#                     Traceback (most recent call last):
# Done                            File ".\password_validator.py", line 57, in <module>
#                                     raise PasswordTooShortError('Password must contain at least 8
#                             characters')
#                             PasswordTooShortError: Password must contain at least 8 characters



class PasswordTooShortError(Exception):
    pass


class PasswordTooCommonError(Exception):
    pass


class PasswordNoSpecialCharactersError(Exception):
    pass


class PasswordContainsSpacesError(Exception):
    pass


def password_too_common(pwd, special):
    only_digits = pwd.isdigit()
    only_letters = pwd.isalpha()
    only_special = all(c in special for c in pwd)
    return only_digits or only_letters or only_special


special_characters = ["@", "*", "&", "%"]

while True:
    password = input()
    if password == "Done":
        break

    if len(password) < 8:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if password_too_common(password, special_characters):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if not any(c in special_characters for c in password):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    print("Password is valid")
