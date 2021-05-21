from datetime import datetime
import bs4
from src.backend.crawler.parsers.case_parser import CaseParser
from tests.unitTests.class_mocks import MockSoup, MockTag

''' MOCKS '''


def mock_BeautifulSoup(data, format):
    return None


def mock_parse_money(soup):
    return '$0.00'


def mock_parse_closed_date(soup):
    return datetime(1000, 10, 10)


def mock_parse_judgements_success(soup):
    return ['judgement0', 'judgement1']


def mock_parse_judgements_failure(soup):
    return []


def mock_parse_secondary_judgements(soup):
    return ['secondary_judgement0', 'secondary_judgement1']


'''
 All mock_soup_... and mock_tag_... functions are used to adjust the return values of MockSoup and MockTag classes
 (see class_mocks.py), which are mocks of BeautifulSoup and BeautifulSoup.tag, respectively.  This allows tailoring
 each mock for a specific purpose
'''


def mock_soup_find_all(arg1, arg2, headers):
    return [MockTag(), MockTag()]


def mock_soup_find_all_returns_empty_list(arg1, arg2, headers):
    return []


# Used for parse_closed_date happy path, return a MockTag that has actual contents for .renderContents()
def mock_soup_find_all_with_contents(arg1, arg2, headers):
    return [MockTag(data=str.encode('10/10/1010'))]


# Used for parse_judgements happy path
def mock_soup_find_judgement(arg1, arg2, headers):
    return MockTag(data=str.encode('<b>judgement</b>'))


def mock_tag_find(arg1, headers):
    return MockTag()


def mock_tag_find_happy_path(arg1, headers):
    return MockTag(data=str.encode('Closed Date:'))


def mock_tag_render_contents_not_useful(arg1):
    return str.encode('not useful string')  # return bytes


''' ---------- FEED() TESTS ---------- '''


def test_feed_success(monkeypatch):
    monkeypatch.setattr(bs4, 'BeautifulSoup', mock_BeautifulSoup)
    monkeypatch.setattr(CaseParser.MoneyParser, 'parse_money', mock_parse_money)
    monkeypatch.setattr(CaseParser, '_parse_closed_date', mock_parse_closed_date)
    monkeypatch.setattr(CaseParser, '_parse_judgements', mock_parse_judgements_success)

    data = CaseParser().feed('data')
    assert data.closed_date == datetime(1000, 10, 10)
    assert data.judgements[0] == 'judgement0'
    assert data.judgements[1] == 'judgement1'
    assert data.money == '$0.00'


def test_feed_success_with_parse_judgements_fail(monkeypatch):
    monkeypatch.setattr(bs4, 'BeautifulSoup', mock_BeautifulSoup)
    monkeypatch.setattr(CaseParser.MoneyParser, 'parse_money', mock_parse_money)
    monkeypatch.setattr(CaseParser, '_parse_closed_date', mock_parse_closed_date)
    monkeypatch.setattr(CaseParser, '_parse_judgements', mock_parse_judgements_failure)
    monkeypatch.setattr(CaseParser, '_parse_secondary_judgements', mock_parse_secondary_judgements)

    data = CaseParser().feed('data')
    assert data.closed_date == datetime(1000, 10, 10)
    assert data.judgements[0] == 'secondary_judgement0'
    assert data.judgements[1] == 'secondary_judgement1'
    assert data.money == '$0.00'


''' ---------- _PARSE_CLOSED_DATE() TESTS ---------- '''


# Testing the outer loop getting no match (for tag in labels:)
def test_parse_closed_date_no_match(monkeypatch):
    monkeypatch.setattr(MockSoup, 'find_all', mock_soup_find_all_returns_empty_list)

    data = CaseParser()._parse_closed_date(MockSoup())
    assert data == datetime(9999, 9, 9)


# Testing the inner loop getting no match (if inner_string is None:)
def test_parse_closed_date_tag_parent_find_no_match(monkeypatch):
    monkeypatch.setattr(MockSoup, 'find_all', mock_soup_find_all)
    # MockTag.find() defaults to return None, so no need to patch

    data = CaseParser()._parse_closed_date(MockSoup())
    assert data == datetime(9999, 9, 9)


# Testing for when there is no 'Closed' string in the tags
def test_parse_closed_date_no_closed_date(monkeypatch):
    monkeypatch.setattr(MockSoup, 'find_all', mock_soup_find_all)
    monkeypatch.setattr(MockTag, 'find', mock_tag_find)
    monkeypatch.setattr(MockTag, 'renderContents', mock_tag_render_contents_not_useful)

    data = CaseParser()._parse_closed_date(MockSoup())
    assert data == datetime(9999, 9, 9)


# Testing for when there is a 'Closed' string in the tags
def test_parse_closed_date_happy_path(monkeypatch):
    # The happy path requires renderContents to return different values based on what's calling it, so
    # we have to build a 'complex' MockTag object for it to play with
    monkeypatch.setattr(MockSoup, 'find_all', mock_soup_find_all_with_contents)
    monkeypatch.setattr(MockTag, 'find', mock_tag_find_happy_path)

    data = CaseParser()._parse_closed_date(MockSoup())
    assert data == datetime(1010, 10, 10).date()


''' ---------- _PARSE_JUDGEMENTS() TESTS ---------- '''


# Testing no judgements found
def test_parse_judgements_no_match(monkeypatch):
    # MockSoup.find() default return is None, so no need to patch anything
    data = CaseParser()._parse_judgements(MockSoup())
    assert data == []


# Test judgements found
def test_parse_judgements_matches(monkeypatch):
    # We could give MockSoup an actual list of tags with actual judgement values, but this will suffice for testing
    # logic
    monkeypatch.setattr(MockSoup, "find", mock_soup_find_judgement)

    data = CaseParser()._parse_judgements(MockSoup())
    assert len(data) == 20
