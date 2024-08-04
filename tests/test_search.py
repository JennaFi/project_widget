import pytest

from src.search_string import search_by_string


@pytest.mark.parametrize(
    "search_str, transaction_index, number_of_transactions",
    [
        ("Перевод", 0, 5),
        ("Переводить", 0, 5),
        ("Перевести", 0, 5),
        ("перев", 0, 5),
        ("карта", 3, 1),
        ("открыть", 5, 1),
        ("открывать", 5, 1),
        ("Орг", 0, 2),
        ("со счета", 1, 2),
    ],
)
def test_search_by_string(transactions, search_str, transaction_index, number_of_transactions):

    assert search_by_string(transactions, search_str)[0] == transactions[transaction_index]
    assert len(search_by_string(transactions, search_str)) == number_of_transactions


def test_search_by_string_no_description():

    data = [
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]
    assert search_by_string(data, "Перевод организации") == []


def test_search_by_string_no_transactions(transactions):
    
    assert search_by_string(transactions, "not such word in description") == []
