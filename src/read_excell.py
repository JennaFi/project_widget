from typing import Dict, List

import pandas as pd


def convert_xlsx_to_dict(filename: str) -> List[Dict]:
    """
      Считывает данные о финансовых операциях из xslx файла и преобразует их в список словарей
    """

    # try:
    data_excell = pd.read_excel(filename)
    data_list = data_excell.apply(
        lambda row: {
            "id": row["id"],
            "state": row["state"],
            "date": row["date"],
            "operationAmount": {
                "amount": row["amount"],
                "currency": {
                    "name": row["currency_name"],
                    "code": row["currency_code"],
                },
            },
            "description": row["description"],
            "from": row["from"],
            "to": row["to"],
        },
        axis=1,
    )
    new_dict_transactions = list()
    index = 0
    for row in data_list:
        new_dict_transactions.append(data_list[index])
        index += 1
    return new_dict_transactions

    # except Exception:
    #     return [{}]


print(convert_xlsx_to_dict("../data/transactions_excel.xlsx"))

