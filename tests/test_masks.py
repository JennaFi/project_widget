import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("string, expected_result", [
    ("12345678901234567340", "**7340"),
    ("12345678901234567890", "**7890"),

])
def test_get_mask_account(string, expected_result):
    assert get_mask_account(string) == expected_result


def test_get_mask_account_incorrect():
    assert get_mask_account('sddf') == "Incorrect data"
    assert get_mask_account('123') == "Incorrect data"
    assert get_mask_account('12345678901011121314151617') == "Incorrect data"


def test_get_mask_card_incorrect():
    assert get_mask_card_number('sddf') == "Incorrect data"
    assert get_mask_card_number('123') == "Incorrect data"
    assert get_mask_card_number('12345678901011121314151617') == "Incorrect data"


@pytest.mark.parametrize("string, expected_result", [
    ("7158300734726758", "7158 30** **** 6758"),
    ("7158300734726759", "7158 30** **** 6759"),
])
def test_get_mask_card_number(string, expected_result):
    assert get_mask_card_number(string) == expected_result



