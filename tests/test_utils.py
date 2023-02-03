from utils import utils


def test_get_data(response):
    assert utils.get_data('https://www.jsonkeeper.com/b/RQUY') == response


def test_filter_by_transaction_type(transaction_list, transaction_list_filter_by_executed):
    assert utils.filter_by_transaction_type(transaction_list, 'EXECUTED') == transaction_list_filter_by_executed


def test_filter_by_key(transaction_list_filter_by_executed, transaction_list_by_key):
    assert utils.filter_by_key(transaction_list_filter_by_executed, 'from') == transaction_list_by_key


def test_sort_by_date(transaction_list_by_key, transaction_list_sort_by_date):
    assert utils.sort_by_date(transaction_list_by_key) == transaction_list_sort_by_date


def test_get_last_transaction(transaction_list_sort_by_date, last_transaction):
    assert utils.get_last_transaction(transaction_list_sort_by_date, 1) == last_transaction
    assert utils.get_last_transaction(transaction_list_sort_by_date, 5) == transaction_list_sort_by_date
    assert utils.get_last_transaction(transaction_list_sort_by_date, -2) == []


def test_get_format_date(transaction):
    assert utils.get_format_date(transaction) == '29.09.2019'


def test_get_description(transaction):
    assert utils.get_description(transaction) == "Перевод со счета на счет"


def test_get_info_from(transaction):
    assert utils.get_info_from(transaction) == "Visa Platinum 2241 65** **** 8487"


def test_get_info_to(transaction):
    assert utils.get_info_to(transaction) == "Счет **4961"


def test_get_hide_number():
    assert utils.get_hide_number('1929393949574830') == '1929 39** **** 4830'
    assert utils.get_hide_number('19293939495748300000') == '**0000'


def test_get_summ(transaction):
    assert utils.get_summ(transaction) == "45849.53"


def test_get_currency(transaction):
    assert utils.get_currency(transaction) == "USD"


def test_get_result_transaction(transaction):
    assert utils.get_result_transaction(transaction) == "29.09.2019 Перевод со счета на счет\n" \
                                                        "Visa Platinum 2241 65** **** 8487 -> Счет **4961\n"\
                                                        "45849.53 USD"
