from dataclasses import dataclass
from datetime import datetime, date
from typing import List
from src.backend.crawler.parsers.money_parser import MoneyParser
from bs4 import BeautifulSoup
from typing import List


@dataclass
class CaseParserData:
    closed_date: date
    judgements: []


# CaseParser parses detailed case info, whose links were gathered by RecordParser
class CaseParser:
    @staticmethod
    def feed(data) -> CaseParserData:
        soup = BeautifulSoup(data, "html.parser")
        money = MoneyParser.parse_money(data)
        closed_date = CaseParser.__parse_closed_date(soup)
        judgements = CaseParser.__parse_judgements(soup)
        # If there were no judgements in the disposition section, check if they got put in the other events
        if not judgements:
            judgements = CaseParser.__parse_secondary_judgements(soup)
        return CaseParserData(closed_date, judgements)

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
    def __parse_judgements(soup) -> List[str]:
        # Explanation:  Look for tags with the header CDisp RDISPDATE#, as these contain the judgement information
        # Start from judgement #1 and work up, note that judgement #1 always occurs earliest so the list will be
        # chronological
        # If we run out of judgements, return what we have.  Note that having no judgements is acceptable.
        judgements = []
        for i in range(1, 20):
            disposition_header = "CDisp RDISPDATE" + str(i)
            disposition_tag = soup.find(header=disposition_header)
            if disposition_tag == None:
                return judgements
            judgements.append(disposition_tag.string)

    @staticmethod
    def __parse_secondary_judgements(soup) -> List[str]:
        JUDGEMENT_KEY = "Judgement"
        judgements = []
        labels = soup.find_all("td", "COtherEventsAndHearings")
        for tag in labels:
            inner_string = tag.string
            if JUDGEMENT_KEY in inner_string:
                judgements.append(inner_string)
        return judgements
