from datetime import datetime, date

SECONDS_IN_YEAR = 31536000

# Good:
#   "Judgement - Dismissal"
#   5 Years or older


# Bad:
#   Anything else
#   Open case -> failed

def isEligible(style, location, violation_type, current_status, closed_date, judgements) -> (bool, str):
    # if status = open, not eligible
    # if >=5 years old, eligible
    # else if <5 years old, check judgement:
    #       if judgement dismissed, eligible
    #       else not eligible
    if current_status == "Open":
        return False, "Not Eligible - Case Still Open"

    years_since = ((datetime.date(datetime.now()) - closed_date).total_seconds()) / SECONDS_IN_YEAR
    if years_since >= 5:
        return True, "Eligible"
    else:
        # edge case: no judgements
        if not judgements:
            return False, "Unable to Determine Eligibility - Needs Review"
        for judgement in judgements:
            if "Judgement - Dismissal" in judgement or "Judgement - General Dismissal":
                return True, "Eligible"
                # TODO: find a amended disposition/judgement case for another if/else
