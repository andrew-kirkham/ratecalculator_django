from datetime import datetime


class TimeRange():
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def is_time_in_range(self, time_to_compare):
        return time_to_compare >= self.start_time \
            and time_to_compare <= self.end_time
