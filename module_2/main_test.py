from main import HasSpecialValidator, HasNumberValidator, HasUpperCharacterValidator, \
    HasLowerCharacterValidator, HasEenoughCharacterValidator, HaveIBeenPwndValidator

import requests_mock

def test_if_number_validator_positive():
    validator = HasNumberValidator('abc1')
    result = validator.is_valid()
    assert result is True


def test_if_number_validator_negative():
    validator = HasNumberValidator('abc')
    result = validator.is_valid()
    assert result is False


def test_if_contain_special_validator_positive():
    validator = HasSpecialValidator('abc1@')
    result = validator.is_valid()
    assert result is True


def test_if_contain_special_validator_negative():
    validator = HasSpecialValidator('abc')
    result = validator.is_valid()
    assert result is False



def test_if_contain_upper_character_validator_positive():
    validator = HasUpperCharacterValidator('aBc1@')
    result = validator.is_valid()
    assert result is True


def test_if_contain_upper_character_validator_negative():
    validator = HasUpperCharacterValidator('abc')
    result = validator.is_valid()
    assert result is False



def test_if_contain_lower_character_validator_positive():
    validator = HasLowerCharacterValidator('aBc1@')
    result = validator.is_valid()
    assert result is True


def test_if_contain_lower_character_validator_negative():
    validator = HasLowerCharacterValidator('ABC')
    result = validator.is_valid()
    assert result is False

def test_if_contain_lower_character_validator_positive():
    validator = HasEenoughCharacterValidator('aBc1@09843hjv')
    result = validator.is_valid()
    assert result is True
    validator = HasEenoughCharacterValidator('aBc', 3)
    result = validator.is_valid()
    assert result is True

def test_if_contain_lower_character_validator_negative():
    validator = HasEenoughCharacterValidator('ABCabc7')
    result = validator.is_valid()
    assert result is False
    validator2 = HasEenoughCharacterValidator('', 1)
    result = validator2.is_valid()
    assert result is False

# TODO check this out
# def test_if_pwnd_validator_positive(requests_mock):
#     response_from_mock = "B21BAEC4E0B569BA0E3F434214E6D7DF500:2\r\n00455B0BEBAEE52B0ECE2B8710B3CD24E4D:2\r\n"
#     requests_mock.get('https://api.pwnedpasswords.com/range/3EFF6', text=response_from_mock)
#     validator = HaveIBeenPwndValidator('maxjestfajny')
#     result = validator.is_valid()
#     assert result is True


def test_if_pwnd_validator_negative(requests_mock):
    response_from_mock = "B21BAEC4E0B569BA0E3F434214E6D7DF599:1\r\n00455B0BEBAEE52B0ECE2B8710B3CD24E4D:2\r\n"
    requests_mock.get('https://api.pwnedpasswords.com/range/3EFF6', text=response_from_mock)
    validator = HaveIBeenPwndValidator('maxjestfajny')
    assert validator.is_valid() is False