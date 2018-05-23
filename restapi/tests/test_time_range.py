
from restapi.time_range import TimeRange
from datetime import datetime

SIX_AM = datetime(2010, 1, 1, 6)
NOON = datetime(2010, 1, 1, 12)
SIX_PM = datetime(2010, 1, 1, 18)
ELEVEN_PM = datetime(2010, 1, 1, 23)


def test_contains_range():
    r1 = TimeRange(SIX_AM, ELEVEN_PM)
    r2 = TimeRange(NOON, SIX_PM)
    assert r1.contains_range(r2)


def test_not_contains_range():
    r1 = TimeRange(SIX_AM, ELEVEN_PM)
    r2 = TimeRange(NOON, SIX_PM)
    assert not r2.contains_range(r1)


def test_start_time_on_boundaries_still_contained():
    r1 = TimeRange(SIX_AM, ELEVEN_PM)
    r2 = TimeRange(SIX_AM, SIX_PM)
    assert r1.contains_range(r2)


def test_end_time_on_boundaries_still_contained():
    r1 = TimeRange(SIX_AM, ELEVEN_PM)
    r2 = TimeRange(NOON, ELEVEN_PM)
    assert r1.contains_range(r2)
