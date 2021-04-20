from dataclasses import dataclass
from datetime import datetime, date
from typing import List
from crawler.parsers.money_parser import MoneyParser
from bs4 import BeautifulSoup
from typing import List
import re
import datetime


@dataclass
class CaseParserData:
    closed_date: date
    judgements: []
    money: str


# CaseParser parses detailed case info, whose links were gathered by RecordParser
class CaseParser:
    @staticmethod
    def feed(data) -> CaseParserData:
        soup = BeautifulSoup(data, "html.parser")
        money = CaseParser.MoneyParser.parse_money(soup)
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

    class MoneyParser:

        @staticmethod
        def parse_money(soup):
            TOTAL = "Total:"
            DOLLAR_SIGN = "$"
            INTEREST = "%"
            SATISFIED = "Satisfied"
            UNSATISFIED = "Unsatisfied"
            DISMISSED = "Dismissed"
            DISMISSAL = "Dismissal"

            only_first_date = False
            interest_date = 0
            money_list = []
            total_money_list = []
            final_total = 0
            labels = soup.find_all("td", class_="ssMenuText ssSmallText")
            for tag in labels:
                for stuff in tag:
                    index = labels.index(tag)
                    # print(tag.text)
                    if not only_first_date:
                        interest_date = MoneyParser.beginning_interest_date(stuff)
                        only_first_date = True
                    if INTEREST in stuff:
                        amount = MoneyParser.extract_one_money(stuff)
                        interest_rate = MoneyParser.extract_interest(stuff)
                        from_date = datetime.datetime.strptime(interest_date, '%m/%d/%Y')
                        today = datetime.datetime.today()
                        time_difference = today - from_date
                        time_in_seconds = time_difference.total_seconds()
                        # 3153600 is total seconds in a year
                        interest_time = time_in_seconds/31536000
                        total_interest = float(amount) * float(interest_rate) * float(interest_time)
                        amount_with_interest = float(amount) + total_interest
                        if TOTAL in stuff:
                            if labels[index - 1].text.find(SATISFIED) != -1 and labels[index - 1].text.find(UNSATISFIED) == -1:
                                continue
                            total_money_list.append(amount_with_interest)
                        else:
                            if labels[index - 1].text.find(SATISFIED) != -1 and labels[index - 1].text.find(UNSATISFIED) == -1:
                                continue
                            money_list.append(amount_with_interest)
                        continue
                    if TOTAL in stuff:
                        if labels[index - 1].text.find(SATISFIED) != -1 and labels[index - 1].text.find(UNSATISFIED) == -1:
                            continue
                        the_total = MoneyParser.extract_one_money(stuff)
                        total_money_list.append(the_total)
                    else:
                        if not type(stuff) == str:
                            continue
                        if labels[index - 1].text.find(SATISFIED) != -1 and labels[index - 1].text.find(UNSATISFIED) == -1:
                            continue
                        MoneyParser.extract_money(stuff, money_list)
            if not total_money_list and not money_list:
                print("There appears to be no remaining amount owed.")
                return "There appears to be no remaining amount owed."
            if total_money_list:
                for stuff in total_money_list:
                    if DOLLAR_SIGN in stuff:
                        stuff = stuff[1:]
                    final_total += float(stuff)
                final_total = "{:.2f}".format(final_total)
                print("The amount owed appears to be $" + str(final_total))
                return "The amount owed appears to be $" + str(final_total)
            else:
                for stuff in money_list:
                    final_total += float(stuff)
                final_total = "{:.2f}".format(final_total)
                print("The amount owed appears to be $" + str(final_total))
                return "The amount owed appears to be $" + str(final_total)

        # The following function attempts to extract all occurrences of what could be money from a string
        @staticmethod
        def extract_money(string, money_list):
            for stuff in string.split():
                money = re.findall("^\$?\d{1,3}(\d+(?!,))?(,\d{3})*(\.\d{2})?$", stuff)
                for cash in money:
                    if "$" in cash:
                        cash.replace("$", "")
                    if cash in money_list:
                        continue
                    money_list.append(cash)
            return money_list

        # The following function extracts only the first item that could be money from a string
        @staticmethod
        def extract_one_money(string):
            for stuff in string.split():
                money = re.match("^\$?\d{1,3}(\d+(?!,))?(,\d{3})*(\.\d{2})?$", stuff)
                if money:
                    if '$' in money[0]:
                        money[0].replace("$", "")
            return money[0]

        # The following function extracts what could be interest from a string
        @staticmethod
        def extract_interest(string):
            for stuff in string.split():
                interest = re.match("^[0-9]+(.[0-9]{1,2})?%", stuff)
                return interest.replace("%", "")

        # The following function extracts a date
        @staticmethod
        def beginning_interest_date(string):
            if string:
                for stuff in str(string).split():
                    # hoping the courts are consistent with date format...
                    return re.match("d{2}/d{2}/d{4}", stuff)
