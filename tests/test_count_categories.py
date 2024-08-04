from src.category_count import category_counter


def test_category_counter(transactions):

    category_list = [
        "Перевод со счета на счет",
        "Перевод организации",
        "Перевод с карты на карту",
        "Открытие вклада",
    ]
    assert category_counter(transactions, category_list) == {
        "Перевод со счета на счет": 2,
        "Перевод организации": 2,
        "Перевод с карты на карту": 1,
        "Открытие вклада": 1,
    }


def test_analyze_categories_no_such_category(transactions):

    assert category_counter(transactions, ["Not existing category"]) == {"Not existing category": 0}


def test_analyze_categories_no_descriptions():

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
    assert category_counter(data, ["Перевод организации", "Перевод с карты на карту"]) == {
        "Перевод организации": 0,
        "Перевод с карты на карту": 0,
    }