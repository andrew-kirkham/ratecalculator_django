
from datetime import datetime
from restapi.rate_handler import RateHandler
from django.test import TestCase
from restapi.exceptions.http_exceptions import NoRateFoundException, InvalidRangeException

SIX_AM = datetime(2000, 1, 1, hour=6)
NOON = datetime(2000, 1, 1, hour=12)
ELEVEN_PM = datetime(2000, 1, 1, hour=23)
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
        with self.assertRaises(InvalidRangeException) as ex:
            handler.handle_request(start_time = NOON, end_time = SIX_AM)

        self.assertEqual(400, ex.exception.status_code)

    def test_invalid_time_returns_404(self):
        with self.assertRaises(NoRateFoundException) as ex:
            handler.handle_request(start_time = SIX_AM, end_time = ELEVEN_PM)

        self.assertEqual(404, ex.exception.status_code)

