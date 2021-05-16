from dataclasses import dataclass
from datetime import datetime, date
import re
from typing import List


@dataclass(frozen=True)
class CaseSummary:
    name: str
    case_number: str
    style: str
    location: str
    complaint_date: str
    closed_date: date  # this is a date since we do date arithmetic w/ it
    violation_type: str
    current_status: str
    judgements: List[str]
    case_detail_link: str
    balance_due_in_cents: int

    def get_balance_due(self):
        return self.balance_due_in_cents / 100


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
                complaint_date="",
                closed_date=date.today(),
                violation_type="",
                current_status="",
                judgements=[],
                case_detail_link="",
                balance_due_in_cents=0,
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
        closed_date, location = date_location
        closed_date = datetime.date(datetime.strptime(closed_date, "%m/%d/%Y"))
        violation_type, current_status = type_status
        balance_due_in_cents = CaseCreator.compute_balance_due_in_cents(balance)
        return CaseSummary(
            "",  # name
            case_number,
            style,
            location,
            "",  # complaint_date
            closed_date,
            violation_type,
            current_status,
            judgements,
            case_detail_link,
            balance_due_in_cents,
        )

    @staticmethod
    def compute_balance_due_in_cents(balance_due_dollar_amount: str):
        return int(CaseCreator._balance_to_float(balance_due_dollar_amount) * 100)

    @staticmethod
    def _balance_to_float(balance: str) -> float:
        commas_removed = balance.replace(",", "")
        normalized_negative = re.sub("\((?P<balance>.*)\)", "-\g<balance>", commas_removed)
        return float(normalized_negative)