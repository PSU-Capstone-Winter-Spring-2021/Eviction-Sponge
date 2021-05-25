
from src.backend.pdf_creator import CreatePDF
import pytest
import datetime

test_dict_2 = {
    'county_name': "Clark",
    'case_number': "11001001",
    'case_name': 'Charles Cheese v Caesar Jr',
    'date_of_judgment': '6/26/11',

    'plaintiff_line1': 'Charles Cheese',
    'plaintiff_line2': 'Nolan Bushnell',

    'defendant_line1': 'Caesar Jr',
    'defendant_line2': 'Ilitch Holdings',
    'defendant_line3': '',
    'defendant_line4': '',

    'def_full_name': 'Caesar Jr',
    'def_mailing_address': '12020 SW Allen Blvd',
    'city_state_zip': 'Beaverton, OR 97005',
    'phone_number': '(503) 646-2900',

    'plaintiff_address': '4145 SW 110th Ave, Beaverton, OR 97005',

    'dismissal': False,
    'restitution': False,
    'money': False,
    'judgment': False,
    'stipulation': False,
    'terms': True
}


def test_name_maker():
    test_dict = {
        'defendant_line1': 'Bon Jovi'
    }
    result = CreatePDF.create_form_name(test_dict)
    assert result == "Bon_Jovi.pdf"


def test_fit_address():
    the_first_line = "This line has twenty"
    the_second_line = "This line is very long, up to seventy-seven characters. It's a bunch."
    the_third_line = "This line is still long, it can hold up to sixty-five, and extra"
    fake_address_line = the_first_line + " " + the_second_line + " " + the_third_line
    result_list = CreatePDF.fit_address(fake_address_line)
    assert result_list[0] == (the_first_line + " ")
    assert result_list[1] == (the_second_line + " ")
    assert result_list[2] == (the_third_line + " ")


def test_dict_converter():
    result = CreatePDF.data_dict_to_pdf_dict(test_dict_2)
    assert result['COUNTY_1'] == 'Clark'
    assert result['PLAINTIFF_1_1'] == 'Charles Cheese'
    assert result['PLAINTIFF_1_2'] == 'Nolan Bushnell'
    assert result['CASE_NO_1'] == "11001001"
    assert result['DEFENDANT_1_1'] == 'Caesar Jr'
    assert result['DEFENDANT_1_2'] == 'Ilitch Holdings'
    assert result['DEFENDANT_1_3'] == ''
    assert result['DEFENDANT_1_4'] == ''
    assert result['DEFENDANT_NAME_1'] == 'Caesar Jr'
    assert result['CASE'] == 'Charles Cheese v Caesar Jr'
    assert result['DISMISSAL'] == False
    assert result['RESTITUTION'] == False
    assert result['MONEY'] == False
    assert result['DATE_OF_JUDGMENT'] == '6/26/11'
    assert result['STIPULATION'] == False
    assert result['TERMS'] == True
    assert result['DATE_1'] == str(datetime.date.today().strftime('%m-%d-%Y'))
    assert result['DEFENDANT_NAME_2'] == 'Caesar Jr'
    assert result['DEFENDANT_ADDRESS'] == '12020 SW Allen Blvd'
    assert result['CITY_STATE_ZIP'] == 'Beaverton, OR 97005'
    assert result['PHONE'] == '(503) 646-2900'
    assert result['DATE_2'] == str(datetime.date.today().strftime('%m-%d-%Y'))
    assert result['PLAINTIFF_ADDRESS_1'] == '4145 SW 110th Ave, '
    assert result['PLAINTIFF_ADDRESS_2'] == 'Beaverton, OR 97005 '
    assert result['PLAINTIFF_ADDRESS_3'] == ''
    assert result['DATE_3'] == str(datetime.date.today().strftime('%m-%d-%Y'))
    assert result['DEFENDANT_NAME_3'] == 'Caesar Jr'
