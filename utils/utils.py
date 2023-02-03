import requests
from datetime import datetime


def get_data(path):
    """
    Возвращает данные с внешнего ресурса в формате json
    """
    response = requests.get(path)
    data = response.json()
    return data


def filter_by_transaction_type(data: list[dict[str, str]],
                               transaction_type: str) -> list[dict[str, str]]:
    """
    Фильтрует по статусу перевода
    """
    filtered_data_by_transaction = []
    for transaction in data:
        if transaction.get('state') == transaction_type:
            filtered_data_by_transaction.append(transaction)
    return filtered_data_by_transaction


def filter_by_key(data: list[dict[str, str]],
                  key: str) -> list[dict[str, str]]:
    """
    Фильтрует по наличию ключа
    """
    filtered_data = []
    for transaction in data:
        if key in transaction:
            filtered_data.append(transaction)
    return filtered_data


def sort_by_date(data: list[dict[str, str]]) -> list[dict[str, str]]:
    """
    Сортирует по дате, от большей к меньшей
    """
    return sorted(data, key=lambda x: x['date'], reverse=True)


def get_last_transaction(data: list[dict[str, str]],
                         amount: int) -> list[dict[str, str]]:
    """
    Возвращает список последних операций в указанном количестве
    """
    if amount > 0:
        if amount < len(data):
            return data[:amount]
        return data[:len(data)]
    return []


def get_format_date(transaction: dict[str, str]) -> str:
    """
    Возвращает дату в формате ДД.ММ.ГГГГ
    """
    date_format = datetime.fromisoformat(transaction["date"])
    return date_format.strftime("%d.%m.%Y")


def get_description(data: dict[str, str]) -> str:
    """
    Возвращает описание типа перевода
    """
    return data["description"]


def get_info_from(transaction: dict[str, str]) -> str:
    """
    Получает информацию о получателе в замаскированном виде
    """
    words = ""
    numbers = ""
    for symbol in transaction["from"]:
        if not symbol.isdigit():
            words += symbol
        else:
            numbers += symbol
    return f"{words}{get_hide_number(numbers)}"


def get_info_to(transaction: dict[str, str]) -> str:
    """
    Получает информацию о получателе в замаскированном виде
    """
    words = ""
    numbers = ""
    for symbol in transaction["to"]:
        if not symbol.isdigit():
            words += symbol
        else:
            numbers += symbol
    return f"{words}{get_hide_number(numbers)}"


def get_hide_number(numbers: str) -> str:
    """
    Маскирует номер счета или карты
    :param numbers: номер счета или карты (str)
    :return: Возвращает номер карты в формате XXXX XX** **** XXXX или
    номер счета в формате в формате **XXXX
    """
    hide_number = ""
    for numb in numbers:
        if numb.isdigit():
            hide_number += numb
    if len(numbers) == 16:
        return numbers[:4] + " " + numbers[4:6] + "** **** " + numbers[12:]
    elif len(numbers) == 20:
        return "**" + numbers[16:]


def get_summ(transaction: dict[str, dict[str, str]]) -> str:
    """
    Возвращает сумму операции
    """
    return f'{transaction["operationAmount"]["amount"]}'


def get_currency(transaction: dict[str, dict[str, dict[str, str]]]) -> str:
    """
    Возвращает валюту
    """
    return f'{transaction["operationAmount"]["currency"]["name"]}'


def get_result_transaction(transaction: dict) -> str:
    """
    Возвращает информацию об операции
    :param transaction: dict
    :return: Возвращает информацию об операции в формате:
    <дата перевода> <описание перевода>
    <откуда> -> <куда>
    <сумма перевода> <валюта>
    """
    result = f"{get_format_date(transaction)} {get_description(transaction)}\n" \
             f"{get_info_from(transaction)} -> {get_info_to(transaction)}\n" \
             f"{get_summ(transaction)} {get_currency(transaction)}"
    return result
