import string
from django.core.exceptions import ValidationError

# value에 특수문자가 있는지 확인
def contains_special_character(value):
    for char in value:
        if char in string.punctuation:
            return True
    return False

# check there is upperletter
def contains_uppercase_letter(value):
    for char in value:
        if char.isupper():
            return True
    return False

# check there is lower letter
def contains_lowercase_letter(value):
    for char in value:
        if char.islower():
            return True
    return False

# check there is number
def contains_number(value):
    for char in value:
        if char.isdigit():
            return True
    return False

# check there is special character
def contains_special_character(value):
    for char in value:
        if char in string.punctuation:
            return True
    return False

# user can`t include special characters
def validate_no_special_characters(value):
    if contains_special_character(value):
        raise ValidationError("you can`t include special characters.")

class CustomPasswordValidator:
    # at least 8 letters mix number and upper/lower letters
    def validate(self, password, user=None):
        if (
                len(password) < 8 or
                not contains_uppercase_letter(password) or
                not contains_lowercase_letter(password) or
                not contains_number(password) 
        ):
            raise ValidationError("at least 8 letters mix number and upper/lower letters.")

    def get_help_text(self):
        return "at least 8 letters mix number and upper/lower letters."
