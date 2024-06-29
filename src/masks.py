def get_mask_card_number(user_input_card: str) -> str | None:
    """Функция  маскировки номера карты"""

    if user_input_card.isdigit() and len(user_input_card) == 16:
        card_number_mask = "{0} {1}** **** {2}".format(user_input_card[:4], user_input_card[4:6], user_input_card[-4:])
    else:
        return "Введенный номер карты некорректен"

    return card_number_mask


def get_mask_account(user_input_account: str) -> str | None:
    """Функция маскировки номера счета"""

    if user_input_account.isdigit() and len(user_input_account) == 20:
        account_number_mask = "**{0} ".format(user_input_account[-4:])
    else:
        return "Введенный номер счета некорректен"

    return account_number_mask
