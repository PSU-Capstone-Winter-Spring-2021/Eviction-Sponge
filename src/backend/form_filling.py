from dataclasses import dataclass


@dataclass
class FormData:
    county_name: str
    case_number: str

    plaintiff_line1: str
    plaintiff_line2: str

    defendant_line1: str
    defendant_line2: str
    defendant_line3: str
    defendant_line4: str

    full_name: str
    mailing_address: str
    city_state_zip: str
    phone_number: str




