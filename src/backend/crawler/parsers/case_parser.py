from dataclasses import dataclass
from datetime import datetime, date
import re

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
            inner_string = tag.parent.find("td", headers="COtherEventsAndHearings")
            if inner_string is None:
                continue

            # soup.find returns a bytes-like, so convert it to characters so we can check for substrings
            inner_string = inner_string.renderContents().decode("utf-8")
            if CLOSED_DATE_KEY in inner_string:
                # date format: 0-padded decimal month, 0-padded decimal day, 4-digit year
                # Specifically, decode soup's bytes-like into characters, then parse those characters into a date,
                # and finally remove the time from the date:
                return datetime.strptime(tag.renderContents().decode("utf-8"), "%m/%d/%Y").date()
        return datetime(9999, 10, 10)

    @staticmethod
    def __parse_judgements(soup) -> List[str]:
        # Explanation:  Look for tags with the header CDisp RDISPDATE#, as these contain the judgement information
        # Start from judgement #1 and work up, note that judgement #1 always occurs earliest so the list will be
        # chronological

        # If we run out of judgements, return what we have.  Note that having no judgements is acceptable.
        judgements = []
        for i in range(20, 0, -1):
            disposition_header = "CDisp RDISPDATE" + str(i)
            disposition_tag = soup.find("td", headers=disposition_header)
            if disposition_tag is None:
                continue

            # soup.find returns a bytes-like, so convert it to characters and then strip everything but the part in bold
            # (<b> this is bolded </b>), as the bold section contains the judgement
            as_string = disposition_tag.renderContents().decode("utf-8")
            judgement_string = (re.sub('^.*?<b>', '', as_string)).split("</b>")[0]
            judgements.append(judgement_string)

        return judgements

    @staticmethod
    def __parse_secondary_judgements(soup) -> List[str]:
        # Apparently, it's spelled Judgment in American English.  The OECI database uses "Judgment", so it's necessary
        # here, but I don't fancy replacing every other use of the word to match
        JUDGEMENT_KEY = "Judgment"
        judgements = []
        labels = soup.find_all("td", headers=re.compile(r"COtherEventsAndHearings RCDER[0-9]+"))
        for tag in labels:
            inner_string = tag.renderContents().decode("utf-8")
            if JUDGEMENT_KEY in inner_string:
                # Trim everything before and after the Judgement, which will be in bold (<b> this is bolded </b>)
                judgements.append((re.sub('^.*?<b>', '', inner_string)).split("</b>")[0])
        return judgements
