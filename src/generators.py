from typing import Generator


def filter_by_currency(transactions: list[dict], currency: str):
    """Функция, которая фильтрует список транзакций по заданному ключу currency"""

    if not transactions:
        print("There is no transactions")
    elif not currency:
        print("There is no transactions in that currency")
    else:
        for key in transactions:
            if key.get("operationAmount").get("currency", {}).get("code") == currency.upper():
                yield key


def transaction_descriptions(transactions: list[dict]):
    """Функция. которая показывает описания к транзакции"""

    if not transactions:
        print("There is no transactions")
    else:
        for key in transactions:
            yield key["description"]


def card_number_generator(start: int, stop: int) -> Generator:
    """Функция. которая генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне"""

    current = start
    if start < 1 or stop > 9999999999999999:
        yield "Range should be between 1 and 9999999999999999"
    else:
        while current <= stop:
            card_number = f"{current:016}"
            formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
            yield formatted_card_number
            current += 1






