import os
from typing import Any

from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.read_csv import convert_csv_file_to_dict
from src.read_excel import convert_xlsx_to_dict
from src.result_output import get_result
from src.search_string import search_by_string
from src.utils import get_transactions_dictionary


print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
print("Выберите необходимый пункт меню:"
      "\n1. Получить информацию о транзакциях из JSON-файла"
      "\n2. Получить информацию о транзакциях из CSV-файла"
      "\n3. Получить информацию о транзакциях из XLSX-файла")

user_input = input().lower()

while True:

    if user_input == "1":
        print("Для обработки выбран JSON-файл")
        break
    elif user_input == "2":
        print("Для обработки выбран CSV-файл")
        break
    elif user_input == "3":
        print("Для обработки выбран XLSX-файл")
        break
    else:
        print("Данная операция недоступна, вернитесь в главное меню")
        print("Выберите необходимый пункт меню:"
              "\n1. Получить информацию о транзакциях из JSON-файла"
              "\n2. Получить информацию о транзакциях из CSV-файла"
              "\n3. Получить информацию о транзакциях из XLSX-файла")


def get_transactions_info(user_input: str) -> Any:
    if user_input == '1':
        transactions = get_transactions_dictionary(
            os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json"))
        return transactions
    elif user_input == '2':
        transactions = convert_csv_file_to_dict(
            os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions.csv"))
        return transactions
    elif user_input == '3':
        transactions = convert_xlsx_to_dict(os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "data", "transactions_excel.xlsx"))
        return transactions


transactions = get_transactions_info(user_input)


print(
    "Введите статус, по которому необходимо выполнить фильтрацию. "
    "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
)

user_input_2 = input().lower()

while True:

    if user_input_2 == "executed":
        print("Операции отфильтрованы по статусу EXECUTED")
        break
    elif user_input_2 == "canceled":
        print("Операции отфильтрованы по статусу CANCELED")
        break
    elif user_input_2 == "pending":
        print("Операции отфильтрованы по статусу PENDING")
        break
    else:
        print(f"Статус операции {user_input_2} недоступен")


transactions_filtred = filter_by_state(transactions, user_input_2)

print("Отсортировать операции по дате? Да/Нет")

user_input_3 = input().lower()

if user_input_3 == 'да':
    print("Отсортировать по возрастанию / по убыванию?")
    user_input_4 = input().lower()
    if user_input_4 == 'по возрастанию':
        transactions_filtred = sort_by_date(transactions_filtred, True)
    else:
        transactions_filtred = sort_by_date(transactions_filtred, False)


print("Выводить только рублевые транзакции? Да/Нет")

user_input_5 = input().lower()

if user_input_5 == 'да':
    transactions_filtred = list(filter_by_currency(transactions_filtred, 'RUB'))


print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")

user_input_6 = input().lower()

if user_input_6 == "да":
    print("Введите слово:")

    word = input().lower()

    transactions_filtred = search_by_string(transactions_filtred, word)


print("Распечатываю итоговый список транзакций...")


print(get_result(transactions_filtred))


