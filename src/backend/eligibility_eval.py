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

    # Edge case: if the parser wasn't able to determine a closed date, the date "9/9/9999" would be used
    if closed_date == datetime(9999, 9, 9):
        return False, "Unable to Determine Eligibility - Needs manual analysis"

    if current_status == "Open":
        return False, "Case Still Open"

    years_since = ((datetime.date(datetime.now()) - closed_date).total_seconds()) / SECONDS_IN_YEAR
    if years_since >= 5:
        return True, "Older than five years"
    else:
        # edge case: no judgements
        if not judgements:
            return False, "Unable to Determine Eligibility - Needs manual analysis"
        for judgement in judgements:
            # Acceptable judgements must start with "Judgement" (amended judgements & notes won't) and be followed by
            # "Dismissal", with any characters in between
            if re.match(r"^[jJ]udgment.*[dD]ismissal", judgement) and not re.match(r".*[sS]tipulated", judgement):
                return True, "Case Dismissed"
            continue

    eligibleDate = (closed_date + relativedelta(years=5)).strftime("%m/%d/%Y")
    return False, ("Case not dismissed and less than five years old. Will be eligible on " + eligibleDate + ".")
