import re
from dataclasses import dataclass
from datetime import datetime, date
from typing import List, Dict, Optional, Tuple

from bs4 import BeautifulSoup
from more_itertools import split_at

SECTION_TITLE_CLASS = "ssCaseDetailSectionTitle"

PROBATION_REVOKED_SEARCH_TERMS = ["probation revoked", "prob revoked"]
EVENTS_TO_EXCLUDE = ["", "dispositions"]


@dataclass
class CaseParserData:
    # district_attorney_number: str
    # hashed_charge_data: Dict[int, Dict[str, str]]
    hashed_dispo_data: Dict[int, Dict[str, str]]
    # balance_due: str
    closed_date: date
    # probation_revoked: Optional[date]


# CaseParser parses detailed case info, whose links were gathered by RecordParser
class CaseParser:
    @staticmethod
    def feed(data) -> CaseParserData:
        soup = BeautifulSoup(data, "html.parser")

        # hashed_charge_data = CaseParser.__build_charge_table_data(soup)
        # (
        #    hashed_dispo_data,
        #    probation_revoked_date_string,
        # ) = CaseParser.__build_hashed_dispo_data_and_probation_revoked(soup)

        hashed_dispo_data = {1: {"hello": "world"}}  # CaseParser.__build_hashed_dispo_data(soup)
        closed_date = CaseParser.__parse_closed_date(soup)
        # ------------------- UPDATED THIS FAR, WORKING ON ABOVE LINE ------------------- #

        # if probation_revoked_date_string:
        #     probation_revoked = datetime.date(datetime.strptime(probation_revoked_date_string, "%m/%d/%Y"))
        # else:
        #     probation_revoked = None  # type: ignore
        # return CaseParserData(district_attorney_number, hashed_charge_data, hashed_dispo_data, balance_due,
        #                      probation_revoked)
        return CaseParserData(hashed_dispo_data, closed_date)

    @staticmethod
    def __parse_closed_date(soup) -> date:
        # Explanation:  Search the HTML of the page for <th class="ssTableHeaderLabel"...> tags
        # Loop through these and look for a <td header="COtherEventsAndHearings...> on the same level,
        # and check its string for the substring "Closed", which indicates we're looking at the right tag
        # When/if found, return the date string from the original tag (& convert to date data type)
        # If not found, return an impossible date
        CLOSED_DATE_KEY = "Closed"
        labels = soup.find_all("th", "ssTableHeaderLabel")
        for tag in labels:
            inner_string = tag.parent.find("td", header="COtherEventsAndHearings").string
            if CLOSED_DATE_KEY in inner_string:
                # date format: 0-padded decimal month, 0-padded decimal day, 4-digit year
                return datetime.strptime(tag.string, "%m/%d/%Y")
        return datetime(0000, 00, 00)

    @staticmethod
    def __build_charge_table_data(soup) -> Dict[int, Dict[str, str]]:
        hashed_charge_data = {}
        charge_information = soup.find("div", class_=SECTION_TITLE_CLASS, string="Charge Information")
        for charge_row in charge_information.parent.next_siblings:
            charge_row_tds = charge_row.findAll("td")
            cells = [cell.text for cell in charge_row_tds if len(cell.text.replace("\xa0", "")) != 0]
            if len(cells) > 0:
                charge_id_string = cells[0]
                charge_id_match = re.compile("\d*").match(charge_id_string)
                if charge_id_match:
                    charge_id = int(charge_id_match.group())
                    charge_data = {"name": cells[1], "statute": cells[2], "level": cells[3], "date": cells[4]}
                    hashed_charge_data[charge_id] = charge_data
                else:
                    raise ValueError(f"Could not parse charge id from {charge_id_string}.")
        return hashed_charge_data

    # Note that one disposition event may have rulings for one or more charges
    # and thus the accumulator pattern.
    # @staticmethod
    # def __build_hashed_dispo_data_and_probation_revoked(soup) -> Tuple[Dict[int, Dict[str, str]], Optional[str]]:
    #    disposition_events, other_events = CaseParser.__parse_events(soup)
    #    acc: Dict[int, Dict[str, str]] = {}
    #    for event in disposition_events:
    #        if CaseParser.__valid_event_table(event):
    #            disposition_data = CaseParser.__parse_event_table(event)
    #            if disposition_data:
    #                acc = {**acc, **disposition_data}
    #    latest_probation_revoked_date = None
    #    for event in other_events:
    #        if CaseParser.__valid_event_table(event):
    #            probation_revoked_date = CaseParser.__parse_probation_revoked(event)
    #            if probation_revoked_date:
    #                latest_probation_revoked_date = probation_revoked_date
    #    return acc, latest_probation_revoked_date

    @staticmethod
    def __build_hashed_dispo_data(soup):
        disposition_events, other_events = CaseParser.__parse_events(soup)
        acc: Dict[int, Dict[str, str]] = {}
        for event in disposition_events:
            if CaseParser.__valid_event_table(event):
                disposition_data = CaseParser.__parse_event_table(event)

    # TODO: change DATE retrieved to CLOSED DATE
    # ------------------- UPDATED THIS FAR, WORKING ON ABOVE LINE ------------------- #

    @staticmethod
    def __parse_events(soup):
        events_title = soup.find("div", class_=SECTION_TITLE_CLASS, string="Events & Orders of the Court")
        events = list(events_title.parent.next_siblings)
        split_events = list(split_at(events, CaseParser.__is_other_events_and_hearings))
        assert len(split_events) == 2
        return split_events

    @staticmethod
    def __is_other_events_and_hearings(event):
        return CaseParser.__normalize_text(event.text) == "other events and hearings".replace(" ", "")

    # MOVED TO STRETCH GOAL:
    # @staticmethod
    # def __build_balance_due(soup) -> str:
    #     financial_information = soup.find("div", class_=SECTION_TITLE_CLASS, string="Financial Information")
    #     if financial_information:
    #         return financial_information.parent.parent.find("b").text
    #     else:
    #         return "0"

    @staticmethod
    def __normalize_text(text):
        return text.replace("\xa0", "").replace(" ", "").lower()

    @staticmethod
    def __valid_event_table(event):
        # return true if event.text is not a disposition or empty string
        return not CaseParser.__normalize_text(event.text) in EVENTS_TO_EXCLUDE

    @staticmethod
    def __parse_event_table(event) -> Optional[Dict[int, Dict[str, str]]]:
        event_parts = event.contents
        assert len(event_parts) == 4
        date, empty_one, empty_two, event_table_wrapper = event_parts
        event_table = event_table_wrapper.contents
        if len(event_table) == 1:
            event_table_contents = event_table[0].contents
            if len(event_table_contents) >= 5 and len(event_table_contents) % 2 == 1:
                event_type, officer, _, event_inner_table_div, created, *rest = event_table_contents
                event_inner_table_parse = CaseParser.__parse_string_list(event_inner_table_div)
            elif len(event_table_contents) >= 4 and len(event_table_contents) % 2 == 0:
                event_type, _, event_inner_table_div, created, *rest = event_table_contents
                event_inner_table_parse = CaseParser.__parse_string_list(event_inner_table_div)
            else:
                raise ValueError("len(event_table_contents) should always be greater than 3.")

            if CaseParser.__normalize_text(event_type.text) in ["disposition", "amendeddisposition"]:
                disposition_data = {}
                for row, next_row in zip(event_inner_table_parse, event_inner_table_parse[1:]):
                    if CaseParser._valid_data(row.split(".\xa0")):
                        charge_id_string, charge = row.split(".\xa0")
                        charge_id = int(charge_id_string)
                        disposition_data[charge_id] = {
                            "date": str(date.text),
                            "charge": str(charge),
                            "ruling": str(next_row),
                            "event": str(event_type.text),
                        }
                return disposition_data
            else:
                return None
        else:
            raise ValueError("event_table should never be empty.")

    @staticmethod
    def __parse_string_list(content) -> List[str]:
        if content:
            if isinstance(content, str):
                return [content]
            else:
                string_list = []
                for e in content.contents:
                    string_list.extend(CaseParser.__parse_string_list(e))
                return string_list
        else:
            return []

    @staticmethod
    def _valid_data(disposition):
        return len(disposition) == 2
