from datetime import date, datetime, timedelta

from src.backend.eligibility_eval import is_eligible


def test_eligible__more_than_5_years():
    five_years_ago = date.today() - timedelta(days=5*365)
    ten_years_ago = date.today() - timedelta(days=10*365)

    assert is_eligible('Closed', five_years_ago, [
                      'Judgement - Dismissal']) == (True, 'Eligible')

    assert is_eligible('Closed', five_years_ago, [
                      'Judgment - Stipulated']) == (True, 'Eligible')

    assert is_eligible('Closed', five_years_ago, [
                      '']) == (True, 'Eligible')

    assert is_eligible('Closed', ten_years_ago, [
                      'Judgment - Default']) == (True, 'Eligible')

    assert is_eligible('Closed', ten_years_ago, [
                      '']) == (True, 'Eligible')


def test_eligible__judgement_dismissal():
    three_years_ago = date.today() - timedelta(days=3*365)

    assert is_eligible('Closed', three_years_ago, [
                      'Judgment - Dismissal']) == (True, 'Eligible')

    assert is_eligible('Closed', three_years_ago, [
                      'Judgment - Small Claims Dismissal']) == (True, 'Eligible')

    assert is_eligible('Closed', three_years_ago, [
                      'Judgment - General Dismissal']) == (True, 'Eligible')


def test_not_eligible__case_still_open():
    three_years_ago = date.today() - timedelta(days=3*365)
    six_years_ago = date.today() - timedelta(days=6*365)

    assert is_eligible('Open', three_years_ago, ['Judgment - Dismissal']) == (
        False, "Not Eligible - Case Still Open")

    assert is_eligible('Open', three_years_ago, ['Judgment - Stipulated']) == (
        False, "Not Eligible - Case Still Open")

    assert is_eligible('Open', six_years_ago, ['Judgment - Dismissal']) == (
        False, "Not Eligible - Case Still Open")

    assert is_eligible('Open', six_years_ago, ['Judgment - Stipulated']) == (
        False, "Not Eligible - Case Still Open")


def test_not_eligible__no_judegement_dismissal():
    three_years_ago = date.today() - timedelta(days=3*365)

    assert is_eligible('Closed', three_years_ago, ['Judgment - Default']) == (
        False, "Not Eligible")

    assert is_eligible('Closed', three_years_ago, ['Judgment - Stipulated']) == (
        False, "Not Eligible")

    assert is_eligible('Closed', three_years_ago, ['Judgment - Dismissal Stipulated']) == (
        False, "Not Eligible")

    assert is_eligible('Closed', three_years_ago, ['Amended Judgment - General Creates Lien', 'Judgment - General Creates Lien']) == (
        False, "Not Eligible")


def test_not_eligible__one_day_less_than_5_years_with_no_judgement_dismissal():
    four_years_and_364_day_ago = date.today() - timedelta(days=4*365-1)

    assert is_eligible('Closed', four_years_and_364_day_ago, ['']) == (
        False, "Not Eligible")


def test_not_eligible__no_judegement():
    three_years_ago = date.today() - timedelta(days=3*365)

    assert is_eligible('Closed', three_years_ago, []) == (
        False, "Unable to Determine Eligibility - Needs Review")


def test_unable_to_determine_eligibility__cannot_determine_closed_date():

    assert is_eligible('Open', datetime(9999, 9, 9), '') == (
        False, "Unable to Determine Eligibility - Cannot determine Closed Date")

    assert is_eligible('Closed', datetime(9999, 9, 9), '') == (
        False, "Unable to Determine Eligibility - Cannot determine Closed Date")

    assert is_eligible('Closed', datetime(9999, 9, 9), ['Judgment - Dismissal']) == (
        False, "Unable to Determine Eligibility - Cannot determine Closed Date")

    assert is_eligible('Closed', datetime(9999, 9, 9), ['Judgment - Stipulated']) == (
        False, "Unable to Determine Eligibility - Cannot determine Closed Date")
