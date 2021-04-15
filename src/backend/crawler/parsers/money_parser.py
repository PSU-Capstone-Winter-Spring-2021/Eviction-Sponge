import re
import datetime
from bs4 import BeautifulSoup


class MoneyParser:

    @staticmethod
    def parse_money(data):
        TOTAL = "Total:"
        DOLLAR_SIGN = "$"
        INTEREST = "%"
        SATISFIED = "Satisfied"
        UNSATISFIED = "Unsatisfied"

        only_first_date = False
        interest_date = 0
        interest_rate = 0
        money_list = []
        final_total = 0
        soup = BeautifulSoup(data, "html.parser")
        labels = soup.find_all("td", class_="ssMenuText ssSmallText")
        for tag in labels:
            for stuff in tag:
                print(tag.text)
                if not only_first_date:
                    interest_date = MoneyParser.beginning_interest_date(stuff)
                    only_first_date = True
                if SATISFIED in stuff:
                    # Change this to return string
                    print("Costs appear to be satisfied.")
                    # return "Costs appear to be satisfied."
                # Not checking for unsatisfied, because the string is not a given
                if TOTAL in stuff:
                    the_total = MoneyParser.extract_money(stuff, money_list)
                    print("The amount owed is " + the_total)
                    # return "The amount owed is " + the_total
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
                    money_list.append(amount_with_interest)
                    continue
                else:
                    MoneyParser.extract_money(stuff, money_list)
                    
        for stuff in money_list:
            final_total += float(stuff)
            print(stuff)
            return "The amount owed appears to be $" + str(final_total)

    @staticmethod
    def extract_money(string, money_list):
        for stuff in string.split():
            money = re.findall("^[+-]?[0-9]{1,3}(?:,?[0-9]{3})*(?:.[0-9]{2})?$", stuff)
            for cash in money:
                cash.replace("$", "")
                money_list.append(cash)
        return money_list

    @staticmethod
    def extract_one_money(string):
        money = re.match("^[+-]?[0-9]{1,3}(?:,?[0-9]{3})*(?:.[0-9]{2})?$", string)
        money.replace("$", "")
        return float(money[0])

    @staticmethod
    def extract_interest(string):
        for stuff in string.split():
            interest = re.match("^[0-9]+(.[0-9]{1,2})?%", stuff)
            return interest.replace("%", "")

    @staticmethod
    def beginning_interest_date(string):
        for stuff in string.split():
            # hoping the courts are consistant with date format...
            return re.match("d{2}/d{2}/d{4}", stuff)

with open(r"C:\Users\danfo\Desktop\PSU\Capstone\Eviction-Sponge\src\backend\files\BOrtiz.html", "r") as file:
    MoneyParser.parse_money(file)

