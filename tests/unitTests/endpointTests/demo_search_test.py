import csv
import os
import sys
from datetime import datetime
from unittest import mock
from flask import json

import pytest

# Need this little tidbit for pytest to work
from src.backend import eligibility_eval
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


def demo_search(client, first_name, last_name, middle_name):
    data = {
        'first_name': first_name,
        'last_name': last_name,
        'middle_name': middle_name
    }
    return client.post('/demo', json=data, follow_redirects=True)


def mock_csv_reader(file, delimiter):
    return ['case num', 'style', 'location', 'type', 'status', 'complaint date',
            '10/10/2010', 'judgement']


def mock_is_eligible(current_status, closed_date, judgements):
    return True, "Eligible"


def mock_datetime_strptime(date_string, format):
    return date_string


def mock_json_dump(data):
    return data


def test_successful_demo(client, monkeypatch):
    monkeypatch.setattr(csv, 'reader', mock_csv_reader)
    monkeypatch.setattr(json, 'dumps', mock_json_dump)
    monkeypatch.setattr(eligibility_eval, 'is_eligible', mock_is_eligible)
    # datetime.strptime('10/10/2010', '%m/%d/%Y').date() works fine here...

    with mock.patch('builtins.open', mock.mock_open(read_data=None)):
        cases = (demo_search(client, 'first_name', 'last_name', 'middle_name'))
        assert cases == 5
