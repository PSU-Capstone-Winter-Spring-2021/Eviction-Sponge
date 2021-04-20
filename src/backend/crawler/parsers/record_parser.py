from html.parser import HTMLParser
import re

from models.case_model import CaseCreator


# Record Parser gathers information from the list of cases returned by OECI when a name is searched
class RecordParser(HTMLParser):
    BASE_URI = "https://publicaccess.courts.oregon.gov/PublicAccessLogin/"

    def __init__(self):
        HTMLParser.__init__(self)
        self.cases = []
        self.column = 0
        self.within_tr_tag = False
        self.within_nested_tr = False
        self.collect_data = False
        self.case_number = ""  # column 1
        self.style = ""  # column 2
        self.date_location = []  # column 3
        self.type_status = []  # column 4
        self.case_detail_link = ""

    def handle_starttag(self, tag, attrs):
        self.__increase_column_count(tag)
        if self.__case_column():
            self.__assign_case_link(tag, attrs)
        self.__set_flags(tag)

    def handle_endtag(self, tag):
        if self.__exiting_nested_table(tag):
            self.within_nested_tr = False
        elif self.__collect_tr_data(tag):
            if self.__valid_row():
                self.__record_case()
                self.__reset_case()
            self.__reset_flags()

    def handle_data(self, data):
        if self.__within_valid_table_row():
            switcher = {
                1: self.__set_case_number,
                2: self.__set_style,
                3: self.__set_date_location,
            }
            # ^ is equivalent to a c++ switch(argument) { case 1: return self.__set_case_number; ... }
            switcher.get(self.column, self.__set_type_status)(data)
            # switcher.get(case = self.column, default = self.__set_type_status), pass in argument (data)

        elif data == "Type":
            self.collect_data = True

    def error(self, message):
        pass

    def __set_case_number(self, data):
        self.case_number = data

    def __set_style(self, data):
        # For some reason, whitespaces in the style are encoded as new lines, so fix that:
        self.style = re.sub('\n', ' ', data)

    def __set_date_location(self, data):
        self.date_location.append(data)

    def __set_type_status(self, data):
        self.type_status.append(data)

    def __record_case(self):
        self.cases.append(
            CaseCreator.create(
                self.case_number,
                self.style,
                self.date_location,
                self.type_status,
                self.case_detail_link,
            )
        )

    def __reset_case(self):
        self.case_number = ""  # column 1
        self.style = ""  # column 2
        self.date_location = []  # column 3
        self.type_status = []  # column 4
        self.case_detail_link = ""

    def __valid_row(self):
        # verify all data entries were filled
        # edge case: style is empty.  I've found one such case that satisfies this
        return (len(self.case_number) > 0) and (len(self.style) >= 0) \
               and (len(self.date_location) > 0) and (len(self.type_status) > 0)

    def __reset_flags(self):
        self.column = 0
        self.within_tr_tag = False

    def __increase_column_count(self, tag):
        if tag == "td":
            self.column += 1

    def __case_column(self):
        return self.column == 1

    def __assign_case_link(self, tag, attrs):
        if tag == "a" and self.collect_data:
            self.case_detail_link = self.BASE_URI + dict(attrs)["href"]

    def __set_flags(self, tag):
        if self.__nested_table_row(tag):
            self.within_nested_tr = True
        elif self.__collect_tr_data(tag):
            self.within_tr_tag = True

    def __collect_tr_data(self, tag):
        return tag == "tr" and self.collect_data

    def __nested_table_row(self, tag):
        return tag == "tr" and self.within_tr_tag

    def __exiting_nested_table(self, tag):
        return tag == "tr" and self.within_nested_tr  # tr = table row

    def __within_valid_table_row(self):
        return self.within_tr_tag and self.collect_data
