def filter_by_state(input_dict: list[dict], state: str | None = "EXECUTED") -> list[dict]:
    """Функция для сортировки списка словарей по ключу state"""

    new_dict = []

    for dictionary in input_dict:
        for key, value in dictionary.items():
            if dictionary[key] == state:
                new_dict.append(dictionary)
    return new_dict


def sort_by_date(input_dict: list[dict], ascending: bool | None = True) -> list[dict]:
    """Функция для сортировки списка словарей по дате"""

    for dictionary in input_dict:
        if ascending:
            sorted_dict = sorted(input_dict, key=lambda date: date.get("date", 0), reverse=True)
        else:
            sorted_dict = sorted(
                input_dict,
                key=lambda date: date.get("date", 0),
            )
    return sorted_dict
