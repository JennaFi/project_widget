import pytest

from src.read_csv import convert_csv_file_to_dict



@pytest.fixture
def path_csv():
    return '../data/transactions.csv'


@pytest.fixture
def transactions():
    return convert_csv_file_to_dict('../data/transactions.csv')


def test_convert_csv_file_to_dict(path_csv):
    assert convert_csv_file_to_dict(path_csv)[0] == {
        'id': '650703',
              'state': 'EXECUTED',
              'date': '2023-09-05T11:30:32Z',
              'operationAmount': {
                  'amount': '16210', 'currency': {'name': 'Sol', 'code': 'PEN'}
              },
              'description': 'Перевод организации',
              'from': 'Счет 58803664561298323391',
              'to': 'Счет 39745660563456619397'
        }
