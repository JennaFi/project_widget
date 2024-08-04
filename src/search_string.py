import re
from typing import List, Dict


def search_by_string(transactions_dict: list[dict], user_input: str) -> List[Dict]:
    """
    Функция принимает список словарей и строку для поиска и возвращает список словарей, гле есть эта строка
    """

    new_dict_transactions_list = []

    for transaction in transactions_dict:
        text = transaction["description"]
        seeking_str = re.findall(user_input, text, flags=re.IGNORECASE)

        if seeking_str:
            new_dict_transactions_list.append(transaction)
    return new_dict_transactions_list

