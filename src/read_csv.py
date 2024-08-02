import csv
from typing import List, Dict


def convert_csv_file_to_dict(filename: str) -> List[Dict]:
    """
    Считывает данные о финансовых операциях из CSV файла и преобразует их в список словарей
    """

    try:
        with open(filename, "r", encoding="utf-8") as file:
            data_reader = csv.reader(file, delimiter=";")
            header = next(data_reader)
            new_dict_transactions = []
            for row in data_reader:
                row_new_dict = {
                    "id": row[header.index("id")],
                    "state": row[header.index("state")],
                    "date": row[header.index("date")],
                    "operationAmount": {
                        "amount": row[header.index("amount")],
                        "currency": {
                            "name": row[header.index("currency_name")],
                            "code": row[header.index("currency_code")],
                        },
                    },
                    "description": row[header.index("description")],
                    "from": row[header.index("from")],
                    "to": row[header.index("to")],
                }
                new_dict_transactions.append(row_new_dict)
            return new_dict_transactions
    except Exception:
        return [{}]


print(convert_csv_file_to_dict("../data/transactions.csv"))


