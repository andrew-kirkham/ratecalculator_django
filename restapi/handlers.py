from rest_framework.response import Response
from rest_framework import status
from restapi.config import rates
from restapi.time_range import TimeRange

class RateHandler():

    # dict[int_dow][] = price
    rate_dict = {}

    def handle_request(self, start_time, end_time):
        # validate that the query params are date time
        print start_time
        print end_time
        if not self.validate_time(start_time, end_time):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(self.get_rate_for_request(start_time, end_time))

    def validate_time(self,  start_time, end_time):
        if start_time > end_time:
            # return a 400
            return False
        if start_time.weekday() != end_time.weekday():
            return False
        return True

    def get_rate_for_request(self, start_time, end_time):
        rates_for_day = rates[start_time.weekday()]
        print start_time.weekday()
        print rates_for_day
        requested_range = TimeRange(start_time, end_time)
        for rate in rates_for_day.keys():
            if rate.contains_range(requested_range):
                return rates_for_day[rate]
        return 0
