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
