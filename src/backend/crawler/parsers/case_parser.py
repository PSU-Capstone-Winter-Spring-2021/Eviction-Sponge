from dataclasses import dataclass
from datetime import datetime, date
import re

from bs4 import BeautifulSoup
from typing import List


@dataclass
class CaseParserData:
    closed_date: date
    complaint_date: str
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
        complaint_date = CaseParser.__parse_complaint_date(soup)
        # If there were no judgements in the disposition section, check if they got put in the other events
        if not judgements:
            judgements = CaseParser.__parse_secondary_judgements(soup)

        # return CaseParserData(closed_date, complaint_date, judgements, money)
        return CaseParserData(closed_date, complaint_date, judgements, money)

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
        return datetime(9999, 9, 9)

    @staticmethod
    def __parse_complaint_date(soup) -> str:
        # The complaint is always the first entry in OTHER EVENTS AND HEARINGS, so the header is always
        # "COtherEventsAndHearings RCDER#".  Just grab that block and parse the date (string) out of it
        # Update: For some reason, RCDER# doesn't always count from 1 (or 0), sometimes starts at higher number
        date_string = ''
        for i in range(0, 10):
            header = "COtherEventsAndHearings RCDER" + str(i)
            tag = soup.find("td", headers=header)
            if tag is None:
                continue

            as_string = tag.renderContents().decode("utf-8")
            if "Complaint" not in as_string:
                continue
            try:
                date_string = re.search(r'[0-9]{2}\/[0-9]{2}\/[0-9]{4}', as_string).group(0)
            except AttributeError:
                date_string = "09/09/9999"
        return date_string

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

    class MoneyParser:

        @staticmethod
        def parse_money(soup):
            return "$0.00"
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
            interest_rate = 0
            amount_before_interest = 0
            labels = soup.find_all("td", class_="ssMenuText ssSmallText")
            for tag in labels:
                for stuff in tag:
                    index = labels.index(tag)
                    # print(tag.text)
                    if not only_first_date:
                        interest_date = CaseParser.MoneyParser.beginning_interest_date(stuff)
                        only_first_date = True
                    if INTEREST in stuff:

                        amount_before_interest = MoneyParser.extract_one_money(stuff)
                        interest_rate = MoneyParser.extract_interest(stuff)
                        from_date = datetime.datetime.strptime(interest_date, '%m/%d/%Y')
                        today = datetime.datetime.today()
                        time_difference = today - from_date
                        time_in_seconds = time_difference.total_seconds()
                        # 3153600 is total seconds in a year
                        interest_time = time_in_seconds / 31536000
                        total_interest = float(amount_before_interest) * float(interest_rate) * float(interest_time)
                        amount_with_interest = float(amount_before_interest) + total_interest

                        if TOTAL in stuff:
                            if labels[index - 1].text.find(SATISFIED) != -1 and labels[index - 1].text.find(
                                    UNSATISFIED) == -1:
                                continue
                            total_money_list.append(amount_with_interest)
                        else:
                            if labels[index - 1].text.find(SATISFIED) != -1 and labels[index - 1].text.find(
                                    UNSATISFIED) == -1:
                                continue
                            money_list.append(amount_with_interest)
                        continue
                    if TOTAL in stuff:
                        if labels[index - 1].text.find(SATISFIED) != -1 and labels[index - 1].text.find(
                                UNSATISFIED) == -1:
                            continue
                        the_total = CaseParser.MoneyParser.extract_one_money(stuff)
                        total_money_list.append(the_total)
                    else:
                        if not type(stuff) == str:
                            continue
                        if labels[index - 1].text.find(SATISFIED) != -1 and labels[index - 1].text.find(
                                UNSATISFIED) == -1:
                            continue
                        CaseParser.MoneyParser.extract_money(stuff, money_list)
            if not total_money_list and not money_list:
                print("There appears to be no remaining amount owed.")
                return "There appears to be no remaining amount owed."
            if total_money_list:
                for stuff in total_money_list:
                    if DOLLAR_SIGN in stuff:
                        stuff = stuff[1:]
                    final_total += float(stuff)
                final_total = "{:.2f}".format(final_total)
                if interest_rate is not None:
                    extra_string = "The interest rate on " + str(amount_before_interest) + " is " + str(
                        interest_rate) + "% for a total of " + str(final_total) + "."
                    return extra_string + " The total amount owed appears to be $" + str(final_total)
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
                money = re.findall(r"^\$?\d{1,3}(\d+(?!,))?(,\d{3})*(\.\d{2})?$", stuff)
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
                money = re.match(r"^\$?\d{1,3}(\d+(?!,))?(,\d{3})*(\.\d{2})?$", stuff)
                if money:
                    if '$' in money[0]:
                        money[0].replace("$", "")
            return money[0]

        # The following function extracts what could be interest from a string
        @staticmethod
        def extract_interest(string):
            for stuff in string.split():
                interest = re.match(r"^[0-9]+(.[0-9]{1,2})?%", stuff)
                return interest.replace("%", "")

        # The following function extracts a date
        @staticmethod
        def beginning_interest_date(string):
            if string:
                for stuff in str(string).split():
                    # hoping the courts are consistent with date format...
                    return re.match(r"d{2}/d{2}/d{4}", stuff)
