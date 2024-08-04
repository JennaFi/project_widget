from typing import Dict
from collections import Counter


def category_counter(transactions_dict: list[dict], category_list: list) -> Dict:
    """ Функция, которая подсчитывает количество операций в каждой категории """
    result = {}
    transactions_list = [transaction.get("description") for transaction in transactions_dict]
    counted_transactions = Counter(transactions_list)

    for category in category_list:
        result[category] = counted_transactions.get(category, 0)

    return result

