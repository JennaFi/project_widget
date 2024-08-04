from datetime import datetime

from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(user_input: str) -> str:
    """Функция общей маскировки карты и счета"""

    symbols = user_input.split()

    if symbols[0] == "Счет":
        symbols[-1] = get_mask_account(symbols[-1])

    else:
        symbols[-1] = get_mask_card_number(symbols[-1])

    return " ".join(symbols)


def get_data(user_data: str) -> str:
    """Функция преобразования даты"""

    new_data = datetime.fromisoformat(user_data).strftime("%d.%m.%Y")

    return new_data
