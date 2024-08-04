import pytest

from src.read_excel import convert_xlsx_to_dict


@pytest.fixture
def path_xlsx():
    return '../data/transactions_excel.xlsx'


def test_convert_xlsx_to_dict(path_xlsx):
    assert convert_xlsx_to_dict(path_xlsx)[0] == {
        'id': 650703.0,
        'state': 'EXECUTED',
        'date': '2023-09-05T11:30:32Z',
        'operationAmount': {'amount': 16210.0,
                            'currency': {'name': 'Sol', 'code': 'PEN'}
                            },
        'description': 'Перевод организации',
        'from': 'Счет 58803664561298323391',
        'to': 'Счет 39745660563456619397'
    }
