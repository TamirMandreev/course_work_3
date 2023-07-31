import pytest

data_1 = [
        {
            "state": "EXECUTED",
            "date": "2023.06.29",
        },
        {
            "state": "EXECUTED",
            "date": "2023.07.28",
        },
        {
            "state": "EXECUTED",
            "date": "2023.05.27",
        },
        {
            "state": "EXECUTED",
            "date": "2023.04.26",
        },
        {
            "state": "EXEC",
            "date": "2023.07.26",
        },
        {
            "state": "EXECUTED",
            "date": "2023.07.29",
        }
    ]

data_2 = {
            "description": "Перевод со счета на счет",
            "date": "2019-01-05T00:52:30.108534",
        }

data_31 = {
            "from": "Счет 26406253703545413262",
            "to": "Счет 20735820461482021315",
        }

data_32 = {
            "from": "Maestro 1308795367077170",
            "to": "МИР 5211277418228469",
        }

data_33 = {
            "to": "МИР 5211277418228469"
        }


data_4 = {
    "operationAmount": {
        "amount": "6381.58",
        "currency": {
            "name": "Рубль",
            "code": "Рубля"
        }
    }
}

# @pytest.fixture
# def data_1():
#     data = data_1
#     return data

