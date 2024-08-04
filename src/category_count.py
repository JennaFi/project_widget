from typing import Dict
from collections import Counter

from src.read_csv import convert_csv_file_to_dict


def category_counter(transactions_dict: list[dict], category_list: list) -> Dict:
    """ Функция, которая подсчитывает количество операций в каждой категории """

    operations = []
    counted_operations = {}

    for dict in transactions_dict:
        if dict['description'] in category_list:
            operations.append(dict['description'])
        counted_operations = Counter(operations)
    return counted_operations

