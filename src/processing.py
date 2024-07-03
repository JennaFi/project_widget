def filter_by_state(input_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция для сортировки списка словарей по ключу state"""

    new_list = []

    for item in input_list:
        for key, value in item.items():
            if item[key] == state:
                new_dict.append(item)
    return new_list


def sort_by_date(input_list: list[dict], is_ascending: bool = True) -> list[dict]:
    """Функция для сортировки списка словарей по дате"""

    for item in input_list:
        if is_ascending:
            sorted_list = sorted(input_list, key=lambda date: date.get("date", 0), reverse=True)
        else:
            sorted_list = sorted(
                input_list,
                key=lambda date: date.get("date", 0),
            )
    return sorted_list
