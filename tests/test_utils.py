import pytest

from tests.conftest import data_1, data_2, data_31, data_32, data_33, data_4
from utils.utils import json_load, get_5_last_transactions, get_date_and_description, get_transfer_from, \
    get_transfer_to, get_operation_amount


def test_json_load():
    path_to_json = '/home/tamir/PycharmProjects/course_work_3/json_data/test.json'
    assert json_load(path_to_json) == {'name': 'Tamir'}


def test_get_5_last_transactions():
    assert get_5_last_transactions(data_1) == [{'date': '2023.07.29', 'state': 'EXECUTED'},
 {'date': '2023.07.28', 'state': 'EXECUTED'},
 {'date': '2023.06.29', 'state': 'EXECUTED'},
 {'date': '2023.05.27', 'state': 'EXECUTED'},
 {'date': '2023.04.26', 'state': 'EXECUTED'}]

def test_get_date_and_description():
    assert get_date_and_description(data_2) == "05.01.2019 Перевод со счета на счет"


def test_get_transfer_from():
    assert get_transfer_from(data_31) == 'Счет XX3262'
    assert get_transfer_from(data_32) == 'Maestro 1308 79 XX XXXX 7170'
    assert get_transfer_from(data_33) == None


def test_get_transfer_to():
    assert get_transfer_to(data_31) == 'Счет XX1315'
    assert get_transfer_to(data_32) == 'МИР 5211 27 XX XXXX 8469'


def test_get_operation_amount():
    assert get_operation_amount(data_4) == '6381.58 Рубля'

