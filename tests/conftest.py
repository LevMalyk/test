import pytest


@pytest.fixture
def my_list_masks_test():
    return [
        "1596837868705199",
        "64686473678894779589",
        "7158300734726758",
        "35383033474447895560",
        "6831982476737658",
        "8990922113665229",
        "5999414228426353",
        "73654108430135874305",
    ]


@pytest.fixture
def result_list_card_number():
    return [
        "1596 83** **** 5199",
        "Введен некоректный номер карты",
        "7158 30** **** 6758",
        "Введен некоректный номер карты",
        "6831 98** **** 7658",
        "8990 92** **** 5229",
        "5999 41** **** 6353",
        "Введен некоректный номер карты",
    ]


@pytest.fixture
def result_list_account_number():
    return [
        "Введен некоректный номер счета",
        "**9589",
        "Введен некоректный номер счета",
        "**5560",
        "Введен некоректный номер счета",
        "Введен некоректный номер счета",
        "Введен некоректный номер счета",
        "**4305",
    ]


@pytest.fixture
def user_data_list():
    return [
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "MasterCard 7158300734726758",
        "Счет 35383033474447895560",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
        "Счет 73654108430135874305",
    ]


@pytest.fixture
def result_user_data_list():
    return [
        "Maestro 1596 83** **** 5199",
        "Счет **9589",
        "MasterCard 7158 30** **** 6758",
        "Счет **5560",
        "Visa Classic 6831 98** **** 7658",
        "Visa Platinum 8990 92** **** 5229",
        "Visa Gold 5999 41** **** 6353",
        "Счет **4305",
    ]