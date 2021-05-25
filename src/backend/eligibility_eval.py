from datetime import datetime
from dateutil.relativedelta import relativedelta
import re

SECONDS_IN_YEAR = 31536000


# Good:
#   "Judgement - Dismissal"
#   "Judgement - Small Claims Dismissal"
#   "Judgement - General Dismissal"
#   probably others as well
#   5 Years or older

# Bad:
#   Anything else
#   "Stipulated" appearing somewhere in the judgement
#   Open case -> failed

def is_eligible(current_status, closed_date, judgements) -> (bool, str):
    # if status = open, not eligible
    # if >=5 years old, eligible
    # else if <5 years old, check judgement:
    #       if judgement dismissed, eligible
    #       else not eligible

    # Use flags to mark possible conditions
    five_years = False
    case_dismissed = False
    no_date = False
    no_judgements = False

    # Edge Case: Case is still going on, can't be expunged until it's closed
    if current_status == "Open":
        return False, "Case Still Open"

    # Edge Case: Parser couldn't find the closed date (may be physically missing, may be parser error)
    if closed_date == datetime(9999, 9, 9):
        no_date = True

    # Edge Case: Parser couldn't find any judgements (may be physically missing, may be parser error)
    if not judgements:
        no_judgements = True

    # Regular Cases:
    if not no_date:
        years_since = ((datetime.date(datetime.now()) - closed_date).total_seconds()) / SECONDS_IN_YEAR
        if years_since >= 5:
            five_years = True
    for judgement in judgements:
        # Acceptable judgements must start with "Judgement" (amended judgements & notes won't) and be followed by
        # "Dismissal", with any characters in between.  "Stipulated" disqualifies this
        if re.match(r"^[jJ]udgment.*[dD]ismissal", judgement) and not re.match(r".*[sS]tipulated", judgement):
            case_dismissed = True
        continue

    # First address edge cases where we cannot determine the eligibility:
    # Situations:
    if ((not five_years and not no_date and no_judgements)  # less than 5 years, but we can't read judgements
        or (not case_dismissed and no_date and not no_judgements)  # not dismissed, but we can't read date
        or (no_date and no_judgements)):  # we can't read date or judgements, so we have no idea
        return False, "Unable to Determine Eligibility - Needs manual analysis"

    # Regular Cases:
    eligibleDate = (closed_date + relativedelta(years=5)).strftime("%m/%d/%Y")
    if not five_years and not case_dismissed:
        return False, ("FUTURE: Not Dismissed & Not Older than 5 Years. Eligible on: " + eligibleDate)
    if not five_years and case_dismissed:
        return True, "ELIGIBLE NOW: Not Older than 5 Years, but Case Dismissed"
    if five_years and not case_dismissed:
        return True, "ELIGIBLE NOW: Not Dismissed, but Older than 5 Years"
    if five_years and case_dismissed:
        return True, "ELIGIBLE NOW: Case Dismissed & Older than 5 Years"
