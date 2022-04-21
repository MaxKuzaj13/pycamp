from main import HasSpecialValidator, HasNumberValidator, HasUpperCharacterValidator, \
    HasLowerCharacterValidator, HasEenoughCharacterValidator, HaveIBeenPwndValidator

import requests_mock

# HasNumberValidator
def test_if_number_validator_positive():
    validator = HasNumberValidator('abc1')
    result = validator.is_valid()
    assert result is True


def test_if_number_validator_negative():
    validator = HasNumberValidator('abc')
    result = validator.is_valid()
    assert result is False

# HasSpecialValidator
def test_if_contain_special_validator_positive():
    validator = HasSpecialValidator('abc1@')
    result = validator.is_valid()
    assert result is True


def test_if_contain_special_validator_negative():
    validator = HasSpecialValidator('abc')
    result = validator.is_valid()
    assert result is False


# HasUpperCharacterValidator
def test_if_contain_upper_character_validator_positive():
    validator = HasUpperCharacterValidator('aBc1@')
    result = validator.is_valid()
    assert result is True


def test_if_contain_upper_character_validator_negative():
    validator = HasUpperCharacterValidator('abc')
    result = validator.is_valid()
    assert result is False


# HasLowerCharacterValidator
def test_if_contain_lower_character_validator_positive():
    validator = HasLowerCharacterValidator('aBc1@')
    result = validator.is_valid()
    assert result is True


def test_if_contain_lower_character_validator_negative():
    validator = HasLowerCharacterValidator('ABC')
    result = validator.is_valid()
    assert result is False

# HasEenoughCharacterValidator
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

# HaveIBeenPwndValidator
def test_if_pwnd_validator_positive(requests_mock):
    response_from_mock_positive = """00455B0BEBAEE52B0ECE2B8710B3CD24E4D:1\r\n00F6D916E15C30B40F55BECE496DF413619:2\r\n"""
    requests_mock.get('https://api.pwnedpasswords.com/range/3EFF6', text=response_from_mock_positive)
    validator = HaveIBeenPwndValidator('maxjestfajny')
    result = validator.is_valid()
    assert result is True


def test_if_pwnd_validator_negative(requests_mock):
    response_from_mock = "00455B0BEBAEE52B0ECE2B8710B3CD24E4D:1\r\nB21BAEC4E0B569BA0E3F434214E6D7DF599:2\r\n"
    requests_mock.get('https://api.pwnedpasswords.com/range/3EFF6', text=response_from_mock)
    validator = HaveIBeenPwndValidator('maxjestfajny')
    assert validator.is_valid() is False

