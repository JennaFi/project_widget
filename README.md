# project_widget
## python studying project
### Учебный открытый проект в рамках изучения python.

IT-отдел крупного банка делает новую фичу для личного кабинета клиента. Это виджет, который показывает несколько последних успешных банковских операций клиента. Мы реализуемм этот проект, который на бэкенде будет готовить данные для отображения в новом виджете.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/JennaFi/project_widget.git
```
2. Установите зависимости
```
pip install -r requirements.txt
```
3. Создайте базу данных и выполните миграции:
```
python manage.py migrate
```
4. Запустите локальный сервер:
```
python manage.py runserver
```
## Использование:

1. Перейдите на страницу в вашем веб-браузере.
2. Создайте новую учетную запись или войдите существующей.
3. Введите номер карты или банковского счета

## Документация:

Дополнительную информацию о структуре проекта и API можно найти в [документации](docs/README.md).

## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE).


