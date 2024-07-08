def get_mask_card_number(user_input_card: str) -> str:
    """Функция  маскировки номера карты"""

    if user_input_card.isdigit() and len(user_input_card) == 16:

        return f"{user_input_card[:4]} {user_input_card[4:6]}** **** {user_input_card[-4:]}"


def get_mask_account(user_input_account: str) -> str:
    """Функция маскировки номера счета"""

    if user_input_account.isdigit() and len(user_input_account) == 20:

        return f"**{user_input_account[-4:]}"
