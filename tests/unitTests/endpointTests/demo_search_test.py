import csv
import os
import sys
from unittest import mock
from flask import json
from src.backend import eligibility_eval
from src.backend.endpoints import demo_search
import pytest

# Need this little tidbit for pytest to work

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


def mock_csv_reader(file, delimiter):
    return [['case-num', 'style', 'location', 'type', 'status', 'complaint-date',
             '10/10/2010', 'judgement']]


def mock_is_eligible(current_status, closed_date, judgements):
    return True, "Eligible"


def mock_datetime_strptime(date_string, format):
    return date_string


def test_successful_demo(client, monkeypatch):
    monkeypatch.setattr(demo_search, "string_to_date", mock_datetime_strptime)
    monkeypatch.setattr(csv, 'reader', mock_csv_reader)
    monkeypatch.setattr(eligibility_eval, 'is_eligible', mock_is_eligible)

    with mock.patch('builtins.open', mock.mock_open(read_data=None)):
        response = (search(client, 'first_name', 'last_name', 'middle_name'))
        assert response.status_code == 200
        #  json.loads takes a json string dictionary and converts it to a python dictionary, undoing the json.dumps()
        contents = json.loads(response.data.decode("utf-8"))
        assert contents == {'case-num': {'closed_date': '10/10/2010',
                                         'complaint_date': 'complaint-date',
                                         'eligibility': [True, 'Eligible'],
                                         'judgements': ['judgement'],
                                         'location': 'location',
                                         'status': 'status',
                                         'style': 'style',
                                         'violation_type': 'type'}}
