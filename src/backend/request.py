

@staticmethod
def payload(param_parser, last_name, first_name, middle_name, birth_date):
    return {
        "__EVENTTARGET": "",
        "__EVENTARGUMENT": "",
        "__VIEWSTATE": param_parser.view_state,
        "__VIEWSTATEGENERATOR": param_parser.view_state_generator,
        "__EVENTVALIDATION": param_parser.event_validation,
        "NodeID": param_parser.node_id,
        "NodeDesc": "All+Locations",
        "SearchBy": "1",
        "ExactName": "on",            # Not sure where this even is
        "CaseSearchMode": "CaseNumber",
        "CaseSearchValue": "",
        "CourtCaseSearchValue": "",
        "PartySearchMode": "Name",
        "AttorneySearchMode": "Name",  # Not sure we are giving this option
        "LastName": last_name,
        "FirstName": first_name,
        "MiddleName": middle_name,
        "DateOfBirth": birth_date,
        "cboState": "AA",           # I am not sure what this is
        "DateFiledOnAfter": "",
        "DateFiledOnBefore": "",
        "chkCriminal": "off",       # This and the others that say off may be able to be excluded
        "chkFamily": "off",
        "chkCivil": "on",
        "chkProbate": "off",
        "chkDtRangeCivil": "on",
        "chkCivilMagist": "on",
        "DateSettingOnAfter": "",
        "DateSettingOnBefore": "",
        "SortBy": "fileddate",
        "SearchSubmit": "Search",
        "SearchType": "PARTY",
        "SearchMode": "NAME",
        "StatusType": "true",
        "ShowInactive": "",
        "AllStatusTypes": "true",
        "CaseCategories": "",       # another I am not sure about
        "RequireFirstName": "True",
        "CaseTypeIDs": "",          # and this one
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
                        + "||DateOfBirth~~Date+of+Birth:~~"
                        + birth_date
                        + "~~"
                        + birth_date
                        + "||AllOption~~All~~0~~All||selectSortBy~~Sort+By:~~Filed+Date~~Filed+Date",
    }