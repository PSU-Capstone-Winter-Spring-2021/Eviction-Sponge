from dataclasses import dataclass
from datetime import datetime, date

import re
from enum import Enum


class ChargeEligibilityStatus(str, Enum):
    UNKNOWN = "Unknown"
    ELIGIBLE_NOW = "Eligible Now"
    POSSIBLY_ELIGIBILE = "Possibly Eligible"
    WILL_BE_ELIGIBLE = "Will Be Eligible"
    POSSIBLY_WILL_BE_ELIGIBLE = "Possibly Will Be Eligible"
    INELIGIBLE = "Ineligible"
    NEEDS_MORE_ANALYSIS = "Needs More Analysis"

    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"


class EditStatus(str, Enum):
    UNCHANGED = "UNCHANGED"
    UPDATE = "UPDATE"
    ADD = "ADD"
    DELETE = "DELETE"


@dataclass(frozen=True)
class CaseSummary:
    name: str
    case_number: str
    district_attorney_number: str
    citation_number: str
    location: str
    date: date
    violation_type: str
    current_status: str
    case_detail_link: str
    balance_due_in_cents: int
    edit_status: EditStatus

    def get_balance_due(self):
        return self.balance_due_in_cents / 100

    def closed(self):
        CLOSED_STATUS = ["Closed", "Inactive", "Purgable", "Bankruptcy Pending"]
        return self.current_status in CLOSED_STATUS


@dataclass(frozen=True)
class OeciCase:
    summary: CaseSummary

    @staticmethod
    def empty(case_number: str):
        return OeciCase(
            CaseSummary(
                name="",
                case_number=case_number,
                district_attorney_number="",
                citation_number="",
                location="",
                date=date.today(),
                violation_type="",
                current_status="",
                case_detail_link="",
                balance_due_in_cents=0,
                edit_status=EditStatus.UNCHANGED,
            ),
            (),
        )


class CaseCreator:
    @staticmethod
    def create(
        info,
        case_number,
        district_attorney_number,
        citation_number,
        date_location,
        type_status,
        case_detail_link,
        balance="0",
    ) -> CaseSummary:
        name = info[0]
        citation_number = citation_number[0] if citation_number else ""
        date, location = date_location
        date = date.fromdatetime(datetime.strptime(date, "%m/%d/%Y"))
        violation_type, current_status = type_status
        balance_due_in_cents = CaseCreator.compute_balance_due_in_cents(balance)
        return CaseSummary(
            name,
            case_number,
            district_attorney_number,
            citation_number,
            location,
            date,
            violation_type,
            current_status,
            case_detail_link,
            balance_due_in_cents,
            EditStatus.UNCHANGED,
        )

    @staticmethod
    def compute_balance_due_in_cents(balance_due_dollar_amount: str):
        return int(CaseCreator._balance_to_float(balance_due_dollar_amount) * 100)

    @staticmethod
    def _balance_to_float(balance: str) -> float:
        commas_removed = balance.replace(",", "")
        normalized_negative = re.sub("\((?P<balance>.*)\)", "-\g<balance>", commas_removed)
        return float(normalized_negative)