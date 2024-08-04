def filter_by_state(transactions_list: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Функция для сортировки списка словарей по ключу state"""

    if not transactions_list:
        return []

    else:
        return [transaction for transaction in transactions_list if transaction.get('state') == state.upper()]


def sort_by_date(transactions_list: list[dict], is_ascending: bool = True) -> list[dict]:
    """Функция для сортировки списка словарей по дате"""

    for transaction in transactions_list:
        if is_ascending:
            sorted_list = sorted(transactions_list, key=lambda date: date.get("date", 0), reverse=True)
        else:
            sorted_list = sorted(
                transactions_list,
                key=lambda date: date.get("date", 0),
            )
    return sorted_list


