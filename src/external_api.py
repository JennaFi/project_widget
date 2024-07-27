import json
import os
from typing import Any

import requests
from dotenv import load_dotenv
from requests import RequestException

load_dotenv()

api_key = os.getenv("API_KEY")


def convert_to_rub(transaction_dict: dict) -> Any:
    """
    Функция, которая принимает значение в долларах или евро, обращается к внешнему API и возвращает
    значение в рублях
    """

    amount = transaction_dict["amount"]
    currency = transaction_dict["currency"]

    try:
        if currency == "USD":
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={amount}"
            headers = {"apikey": api_key}
            response = requests.get(url, headers=headers)
            json_result = response.json()
            rub_amount = json_result["result"]
            return rub_amount
        elif currency == "EUR":
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount={amount}"
            headers = {"apikey": api_key}
            response = requests.get(url, headers=headers)
            json_result = response.json()
            rub_amount = json_result["result"]
            return rub_amount
    except RequestException:
        return 0


# def convert_usd_to_rub(amount: float) -> Any:
#     """Функция, которая принимает значение в долларах, обращается к API и возвращает значение в рублях"""
#
#     url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={amount}"
#     headers = {"apikey": api_key}
#     response = requests.request("GET", url, headers=headers)
#     json_result = response.text
#     rub_amount = json.loads(json_result)["result"]
#
#     return rub_amount
#
#
# def convert_eur_to_rub(amount: float) -> Any:
#     """Функцияб ктоорая принимает значение в евро, обращается к API и возвращает значение в рублях"""
#
#     url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount={amount}"
#     headers = {"apikey": api_key}
#     response = requests.request("GET", url, headers=headers)
#     json_result = response.text
#     rub_amount = json.loads(json_result)["result"]
#
#     return rub_amount
