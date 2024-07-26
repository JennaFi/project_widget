import json
from typing import Any

from src.external_api import convert_eur_to_rub, convert_usd_to_rub


def get_transactions_dictionary(path: str) -> Any:
    """Принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, "r", encoding="utf-8") as operations:
            try:
                transactions_data = json.load(operations)
                return transactions_data
            except json.JSONDecodeError:
                transactions_data = []
                return transactions_data
    except FileNotFoundError:
        transactions_data = []
        return transactions_data


def return_transaction_amount_in_rub(transactions: list, transaction_id: int) -> Any:
    """Функция принимает сумму транзакции и возвращает сумму в рублях, либо конвертирует сумму в иной валюте в рубли"""

    for transaction in transactions:

        if transaction["id"] == transaction_id:

            if transaction["operationAmount"]["currency"]["code"] == "RUB":

                return transaction["operationAmount"]["amount"]

            elif transaction["operationAmount"]["currency"]["code"] == "USD":

                usd_amount = transaction["operationAmount"]["amount"]

                rub_amount = convert_usd_to_rub(usd_amount)

                return round(rub_amount, 2)

            elif transaction["operationAmount"]["currency"]["code"] == "EUR":

                eur_amount = transaction["operationAmount"]["amount"]

                rub_amount = convert_eur_to_rub(eur_amount)

                return round(rub_amount, 2)

