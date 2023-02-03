from utils.utils import get_data, \
    filter_by_transaction_type, \
    sort_by_date, get_last_transaction, \
    get_result_transaction, \
    filter_by_key


SOURSE = 'https://www.jsonkeeper.com/b/6DQ0'
AMOUNT_LAST_OPERATIONS = 5


def main():
    """
    Выводит последние операции в нужном формате
    """
    # Получаем данные с внешнего источника
    data = get_data(path=SOURSE)
    # Фильтруем по статусу перевода и по неполной информации по ключу 'from'
    filtered_data = filter_by_key(data=filter_by_transaction_type(data=data,
                                                                  transaction_type='EXECUTED'),
                                  key='from')
    # Сортируем по дате
    sort_data_by_date = sort_by_date(data=filtered_data)

    # Получаем последние транзакции (в количестве AMOUNT_LAST_OPERATIONS)
    last_transaction = get_last_transaction(data=sort_data_by_date, amount=AMOUNT_LAST_OPERATIONS)

    # Запускаем цикл для вывода информации по транзакциям
    for transaction in last_transaction:
        print()
        print(get_result_transaction(transaction=transaction))


if __name__ == '__main__':
    main()
