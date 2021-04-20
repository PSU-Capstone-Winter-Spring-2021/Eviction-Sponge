import re
import datetime
from bs4 import BeautifulSoup

# MoneyParser.parse_money scans OECI case files in HTML format in an attempt to find any remaining money owed. It grabs the first date than checks
# for, in order, if there is interest, if there is a "Total" section, if there is anything else that appears
# to be money. Total and the rest are separate lists, if there is anything in the 'total' list then it has
# precedence.


class MoneyParser:

    @staticmethod
    def parse_money(data):
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
        soup = BeautifulSoup(data, "html.parser")
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
