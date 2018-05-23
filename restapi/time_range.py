from datetime import datetime


class TimeRange():
    def __init__(self, start_time, end_time):
        #start and end time are datetimes but we convert them to times
        self.start_time = start_time.time()
        self.end_time = end_time.time()

    def is_time_in_range(self, time_to_compare):
        return time_to_compare >= self.start_time \
            and time_to_compare <= self.end_time

    def contains_range(self, range_to_compare):
        if range_to_compare.start_time < self.start_time:
            # start time before this start time
            return False
        if range_to_compare.end_time > self.end_time:
            # end time after this end time
            return False
        return True
