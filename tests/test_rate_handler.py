
from datetime import datetime
from restapi.rate_handler import RateHandler
from django.test import TestCase

SIX_AM = datetime(2000, 1, 1, hour=6)
NOON = datetime(2000, 1, 1, hour=12)
NOON_TMRW = datetime(2000, 1, 2, hour=12)
handler = RateHandler()

class TimeRangeTest(TestCase):

    def test_validate_time(self):
        is_valid = handler.validate_time(start_time = SIX_AM, end_time =  NOON)
        self.assertTrue(is_valid)

    def test_validate_same_start_end_time(self):
        is_valid = handler.validate_time(start_time = SIX_AM, end_time =  SIX_AM)
        self.assertTrue(is_valid)

    def test_validate_time_invalid(self):
        is_valid = handler.validate_time(start_time = NOON, end_time = SIX_AM)
        self.assertFalse(is_valid)

    def test_validate_time_wrong_day(self):
        is_valid = handler.validate_time(start_time = SIX_AM, end_time = NOON_TMRW)
        self.assertFalse(is_valid)

    def test_invalid_time_returns_400(self):
        response = handler.handle_request(start_time = NOON, end_time = SIX_AM)
        self.assertEqual(response.status_code, 400)
