import pytest
from unittest.mock import patch
from src.utils import get_transactions_dictionary


@pytest.fixture
def get_path():
    return '../data/operations.json'


@pytest.fixture
def get_wrong_path():
    return 'wrong path'


@pytest.fixture
def transactions():
    return get_transactions_dictionary('../data/operations.json')



def test_get_transactions_dictionary(get_path):
    assert get_transactions_dictionary(get_path)[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }


def test_get_transactions_dictionary_wrong_path(get_wrong_path):
    assert get_transactions_dictionary(get_wrong_path) == []





