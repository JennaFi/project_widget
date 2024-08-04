import logging
import os

log_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "masks.log")

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(log_file_path, mode="w")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(user_input_card: str) -> str:
    """Функция  маскировки номера карты"""

    if user_input_card.isdigit() and len(user_input_card) == 16:

        return f"{user_input_card[:4]} {user_input_card[4:6]}** **** {user_input_card[-4:]}"
    else:
        return 'Incorrect data'


def get_mask_account(user_input_account: str) -> str:
    """Функция маскировки номера счета"""

    if user_input_account.isdigit() and len(user_input_account) == 20:

        return f"**{user_input_account[-4:]}"
    else:
        return 'Incorrect data'
