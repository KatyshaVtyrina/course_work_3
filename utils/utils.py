import requests


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
