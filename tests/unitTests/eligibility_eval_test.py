from datetime import date, datetime, timedelta

from dateutil.relativedelta import relativedelta

from src.backend.eligibility_eval import is_eligible


def test_eligible__more_than_5_years():
    five_years_ago = date.today() - timedelta(days=5*365)
    ten_years_ago = date.today() - timedelta(days=10*365)

    assert is_eligible('Closed', five_years_ago, ['Judgment - Stipulated']) == (
        True, 'ELIGIBLE NOW: Not Dismissed, but Older than 5 Years')

    assert is_eligible('Closed', five_years_ago, ['']) == (
        True, 'ELIGIBLE NOW: Not Dismissed, but Older than 5 Years')

    assert is_eligible('Closed', ten_years_ago, ['Judgment - Default']) == (
        True, 'ELIGIBLE NOW: Not Dismissed, but Older than 5 Years')

    assert is_eligible('Closed', ten_years_ago, ['']) == (
        True, 'ELIGIBLE NOW: Not Dismissed, but Older than 5 Years')


def test_eligible__more_than_5_years_and_judgement_dismissal():
    ten_years_ago = date.today() - timedelta(days=10 * 365)

    assert is_eligible('Closed', ten_years_ago, ['Judgment - Dismissal']) == (
        True, 'ELIGIBLE NOW: Case Dismissed & Older than 5 Years')

    assert is_eligible('Closed', ten_years_ago, ['Judgment - Small Claims Dismissal']) == (
        True, 'ELIGIBLE NOW: Case Dismissed & Older than 5 Years')

    assert is_eligible('Closed', ten_years_ago, ['Judgment - General Dismissal']) == (
        True, 'ELIGIBLE NOW: Case Dismissed & Older than 5 Years')


def test_eligible__judgement_dismissal():
    three_years_ago = date.today() - timedelta(days=3*365)

    assert is_eligible('Closed', three_years_ago, ['Judgment - Dismissal']) == (
        True, 'ELIGIBLE NOW: Not Older than 5 Years, but Case Dismissed')

    assert is_eligible('Closed', three_years_ago, ['Judgment - Small Claims Dismissal']) == (
        True, 'ELIGIBLE NOW: Not Older than 5 Years, but Case Dismissed')

    assert is_eligible('Closed', three_years_ago, ['Judgment - General Dismissal']) == (
        True, 'ELIGIBLE NOW: Not Older than 5 Years, but Case Dismissed')


def test_not_eligible__case_still_open():
    three_years_ago = date.today() - timedelta(days=3*365)
    six_years_ago = date.today() - timedelta(days=6*365)

    assert is_eligible('Open', three_years_ago, ['Judgment - Dismissal']) == (
        False, "Case Still Open")

    assert is_eligible('Open', three_years_ago, ['Judgment - Stipulated']) == (
        False, "Case Still Open")

    assert is_eligible('Open', six_years_ago, ['Judgment - Dismissal']) == (
        False, "Case Still Open")

    assert is_eligible('Open', six_years_ago, ['Judgment - Stipulated']) == (
        False, "Case Still Open")


def test_not_eligible__no_judegement_dismissal():
    three_years_ago = date.today() - timedelta(days=3*365)
    eligibleDate = (three_years_ago + relativedelta(years=5)).strftime("%m/%d/%Y")

    assert is_eligible('Closed', three_years_ago, ['Judgment - Default']) == (
        False, ("FUTURE: Not Dismissed & Not Older than 5 Years. Eligible on: " + eligibleDate))

    assert is_eligible('Closed', three_years_ago, ['Judgment - Stipulated']) == (
        False, ("FUTURE: Not Dismissed & Not Older than 5 Years. Eligible on: " + eligibleDate))

    assert is_eligible('Closed', three_years_ago, ['Judgment - Dismissal Stipulated']) == (
        False, ("FUTURE: Not Dismissed & Not Older than 5 Years. Eligible on: " + eligibleDate))

    assert is_eligible('Closed', three_years_ago, ['Amended Judgment - General Creates Lien', 'Judgment - General Creates Lien']) == (
        False, ("FUTURE: Not Dismissed & Not Older than 5 Years. Eligible on: " + eligibleDate))


def test_not_eligible__one_day_less_than_5_years_with_no_judgement_dismissal():
    four_years_and_364_day_ago = date.today() - timedelta(days=4*365-1)
    eligibleDate = (four_years_and_364_day_ago + relativedelta(years=5)).strftime("%m/%d/%Y")

    assert is_eligible('Closed', four_years_and_364_day_ago, ['']) == (
        False, ("FUTURE: Not Dismissed & Not Older than 5 Years. Eligible on: " + eligibleDate))


def test_not_eligible__no_judgement():
    three_years_ago = date.today() - timedelta(days=3*365)

    assert is_eligible('Closed', three_years_ago, []) == (
        False, "Unable to Determine Eligibility - Needs manual analysis")


def test_unable_to_determine_eligibility():
    # no_date & no_judgements
    assert is_eligible('Closed', datetime(9999, 9, 9), '') == (
        False, "Unable to Determine Eligibility - Needs manual analysis")

    # no_date & judgement not dismissed
    assert is_eligible('Closed', datetime(9999, 9, 9), ['Judgment - Stipulated']) == (
        False, "Unable to Determine Eligibility - Needs manual analysis")

    # date <5 years & no_judgements
    assert is_eligible('Closed', date.today(), '') == (
        False, "Unable to Determine Eligibility - Needs manual analysis")