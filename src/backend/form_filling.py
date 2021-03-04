from dataclasses import dataclass


@dataclass
class FormData:
    county_name: str
    case_number: str
    case_name: str
    date_of_judgement: str

    plaintiff_line1: str
    plaintiff_line2: str

    defendant_line1: str
    defendant_line2: str
    defendant_line3: str
    defendant_line4: str

    def_full_name: str
    def_mailing_address: str
    city_state_zip: str
    phone_number: str

    plaintiff_address: str

# Everything that says none is a checkbox, and I have not figured out how to make those work yet
@dataclass 
class PDF_form_template:
    COUNTY_1: str
    COUNTY_2: str
    PLAINTIFF_1_1: str
    PLAINTIFF_1_2: str
    DEFENDANT_1_1: str
    DEFENDANT_1_2: str
    DEFENDANT_1_3: str
    DEFENDANT_1_4: str
    PLAINTIFF_2_1: str
    PLAINTIFF_2_2: str
    DEFENDANT_2_1: str
    DEFENDANT_2_2: str
    DEFENDANT_2_3: str
    DEFENDANT_2_4: str
    MOTION: str
    CASE: str
    CASE_NO_1: str
    CASE_NO_2: str
    DISMISSAL: None
    RESTITUTION: None
    MONEY: None
    JUDGEMENT: None
    STIPULATION: None
    TERMS: None
    DATE_OF_JUDGEMENT: str
    DATE: str
    NAME_PRINTED: str
    DEFENDANT_ADDRESS: str
    CITY_STATE_ZIP: str
    PHONE: str
    DATE_2: str
    PLAINTIFF_ADDRESS_1: str
    PLAINTIFF_ADDRESS_2: str
    PLAINTIFF_ADDRESS_3: str
    DATE_3: str
    DEFENDANT_NAME_1: str
    DEFENDANT_NAME_2: str
    DEFENDANT_NAME_3: str
    DEFENDANT_ADDRESS: str
    PLAINTIFF_NAME: str
    DO_NOT_FILL: str
    DO_NOT_CLICK: None
