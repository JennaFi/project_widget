from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(user_input: str) -> str | None:
    """Функция общей маскировки карты и счета"""

    symbols = user_input.split()

    if symbols[0] == 'Счет':
        symbols[-1] = get_mask_account(symbols[-1])

    else:
        symbols[-1] = get_mask_card_number(symbols[-1])

    return ''.join(symbols)


print(mask_account_card('Visa Platinum 8990922113665229'))