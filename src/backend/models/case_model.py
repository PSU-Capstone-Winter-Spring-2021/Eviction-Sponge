from dataclasses import dataclass
from datetime import datetime, date

import re
from enum import Enum

from typing import List


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
    style: str
    location: str
    date: date
    violation_type: str
    current_status: str
    judgements: List[str]
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
                style="",
                location="",
                date=date.today(),
                violation_type="",
                current_status="",
                judgements=[],
                case_detail_link="",
                balance_due_in_cents=0,
                edit_status=EditStatus.UNCHANGED,
            ),
            (),
        )


class CaseCreator:
    @staticmethod
    def create(
        case_number,
        style,
        date_location,
        type_status,
        case_detail_link,
        balance="0",
        judgements=[],
    ) -> CaseSummary:
        myDate, location = date_location
        myDate = datetime.date(datetime.strptime(myDate, "%m/%d/%Y"))
        violation_type, current_status = type_status
        balance_due_in_cents = CaseCreator.compute_balance_due_in_cents(balance)
        return CaseSummary(
            "",
            case_number,
            style,
            location,
            myDate,
            violation_type,
            current_status,
            judgements,
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