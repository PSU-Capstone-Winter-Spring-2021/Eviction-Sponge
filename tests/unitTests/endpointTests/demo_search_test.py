import csv
import os
import sys

import pytest
import builtins


# Need this little tidbit for pytest to work
from src.backend.endpoints.search import Search

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from src.backend.app import create_app


@pytest.fixture
def client():
    app = create_app('development')
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def search(client, first_name, last_name, middle_name):
    data = {
        'first_name': first_name,
        'last_name': last_name,
        'middle_name': middle_name
    }
    return client.post('/demo', json=data, follow_redirects=True)


def mock_open(path, newline):
    return None


def mock_csv_reader(file, delimiter):
    return ['case num', 'style', 'location', 'type', 'status', 'closed_date', 'Judgement', 'True', 'Eligible']


def test_successful_demo(client, monkeypatch):
    monkeypatch.setitem(__builtins__, 'open', mock_open)
    monkeypatch.setitem(csv, "reader", mock_csv_reader)
    #cases = list((search(client, "first_name", "last_name", "middle_name")).json)
    #assert cases == 5
