from abc import ABC, abstractmethod
from hashlib import sha1
import requests
from string import punctuation

#
# class PasswordValidator:
#     """"""
#     def __init__(self, password):
#         self.password = password
#
#     def is_valid(self):
#         pass
#
#
# validator = PasswordValidator('query')
#
# print(validator.is_valid())



class Validator(ABC):
    """"""
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def is_valid(self):
        pass


class HasNumberValidator(Validator):
    """"""
    def __init__(self, text):
        self.text = text

    def is_valid(self):
        # for number in range(0,10):
        #     if str(number) in self.text:
        #         return True
        # return False
        # for number in range(0,10):
        #     if str(number) in self.text:
        numbers = [ number for number in range(0,10) if str(number) in self.text]
        if len(numbers) > 0:
            return True
        else:
            return False


class HasSpecialValidator(Validator):
    """"""
    def __init__(self, text):
        self.text = text

    def is_valid(self):
        special = [ character for character in list(punctuation) if str(character) in self.text]
        if len(special) > 0:
            return True
        else:
            return False


class HasUpperCharacterValidator(Validator):
    """"""
    def __init__(self, text):
        self.text = text

    def is_valid(self):
        upper = [character.isupper() for character in self.text]
        return any(upper)


class HasLowerCharacterValidator(Validator):
    """"""
    def __init__(self, text):
        self.text = text

    def is_valid(self):
        lower = [character.islower() for character in self.text]
        return any(lower)

class HasEenoughCharacterValidator(Validator):
    """"""
    def __init__(self, text, min_length=8):
        self.text = text
        self.min_length = min_length

    def is_valid(self):
        return len(self.text) >= self.min_length


class HaveIBeenPwndValidator(Validator):
    """"""
    def __init__(self, text):
        self.text = text


    def is_valid(self):
        hash = sha1(self.text.encode('utf-8')).hexdigest().upper()
        resp = requests.get(f'https://api.pwnedpasswords.com/range/{hash[:5]}')
        for line in resp.text.splitlines():
            found_hash, _ = line.split(':')
            if found_hash == hash[5:]:
                print(found_hash)
                return False





class PasswordValidator(Validator):
    def __init__(self, password):
        self.password = password
        self.validators = [
            HasSpecialValidator,
            HasNumberValidator,
            HasUpperCharacterValidator,
            HasLowerCharacterValidator,
            HasEenoughCharacterValidator,
            HaveIBeenPwndValidator
        ]
    def is_valid(self):
        for class_name in self.validators:
            validator = class_name(self.password)
            validator.is_valid()


validator = PasswordValidator('query')

print(validator.is_valid())
# class HasNumberValidator(Validator):
#     """"""
#     def __init__(self, text):
#         self.text = text
#
#     def is_valid(self):
#         pass