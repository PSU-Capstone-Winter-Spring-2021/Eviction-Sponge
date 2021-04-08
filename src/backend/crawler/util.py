# Misc service classes used by the crawler, to avoid cluttering the crawler.py file
import collections


class URL:
    @staticmethod
    def login_url():
        return "https://publicaccess.courts.oregon.gov/PublicAccessLogin/login.aspx"

    @staticmethod
    def search_url():
        return "https://publicaccess.courts.oregon.gov/PublicAccessLogin/Search.aspx?ID=100"


class Payload:
    @staticmethod
    def payload(param_parser, last_name, first_name, middle_name):
        return {
            "__EVENTTARGET": "",
            "__EVENTARGUMENT": "",
            "__VIEWSTATE": param_parser.view_state,
            "__VIEWSTATEGENERATOR": param_parser.view_state_generator,
            "__EVENTVALIDATION": param_parser.event_validation,
            "NodeID": param_parser.node_id,
            "NodeDesc": "All+Locations",
            "SearchBy": "1",
            "ExactName": "on",
            "CaseSearchMode": "CaseNumber",
            "CaseSearchValue": "",
            "CitationSearchValue": "",
            "CourtCaseSearchValue": "",
            "PartySearchMode": "Name",
            "AttorneySearchMode": "Name",
            "LastName": last_name,
            "FirstName": first_name,
            "cboState": "AA",
            "MiddleName": middle_name,
            "DriverLicNum": "",
            "CaseStatusType": "0",
            "DateFiledOnAfter": "",
            "DateFiledOnBefore": "",
            "chkCriminal": "on",
            "chkFamily": "on",
            "chkCivil": "on",
            "chkProbate": "on",
            "chkDtRangeCriminal": "on",
            "chkDtRangeFamily": "on",
            "chkDtRangeCivil": "on",
            "chkDtRangeProbate": "on",
            "chkCriminalMagist": "on",
            "chkFamilyMagist": "on",
            "chkCivilMagist": "on",
            "chkProbateMagist": "on",
            "DateSettingOnAfter": "",
            "DateSettingOnBefore": "",
            "SortBy": "fileddate",
            "SearchSubmit": "Search",
            "SearchType": "PARTY",
            "SearchMode": "NAME",
            "NameTypeKy": "ALIAS",
            "BaseConnKy": "DF",
            "StatusType": "true",
            "ShowInactive": "",
            "AllStatusTypes": "true",
            "CaseCategories": "",
            "RequireFirstName": "True",
            "CaseTypeIDs": "",
            "HearingTypeIDs": "",
            "SearchParams": "SearchBy~~Search+By:~~Defendant~~Defendant||chkExactName~~Exact+Name:~~on~~on||PartyNameOption~~Party+Search+Mode:~~Name~~Name||LastName~~Last+Name:~~"
                            + last_name
                            + "~~"
                            + last_name
                            + "||FirstName~~First+Name:~~"
                            + first_name
                            + "~~"
                            + first_name
                            + "||MiddleName~~Middle+Name:~~"
                            + middle_name
                            + "~~"
                            + middle_name
                            + "||AllOption~~All~~0~~All||selectSortBy~~Sort+By:~~Filed+Date~~Filed+Date",
        }


# Least-Recently-Used cache
class LRUCache:
    def __init__(self, size):
        self.size = size
        # using ordered dictionary (a hash table) for efficiency
        self.myDict: collections.OrderedDict = collections.OrderedDict()

    def __getitem__(self, key):
        # want to remove an item, then add it again at the top since it was recently used
        value = self.myDict.pop(key, None)  # if not found, return None
        if value:  # ~ if not None
            self.myDict[key] = value
        return value

    def __setitem__(self, key, value):
        # if full remove bottom item
        if len(self.myDict) >= self.size:
            self.myDict.popitem(last=False)  # last means last inserted, or the top. We want bottom, so last=False
        # now add item
        self.myDict[key] = value
