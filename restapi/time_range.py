
class TimeRange(object):
    def __init__(self, start_time, end_time):
        """Create a new TimeRange

        Arguments:
            start_time {datetime} -- start time for this time range
            end_time {datetime} -- end time for this time range
        """

        #start and end time are datetimes but we convert them to times
        self.start_time = start_time.time()
        self.end_time = end_time.time()

    def contains_range(self, range_to_compare):
        """Check if the given range is fully contained by this range

        Arguments:
            range_to_compare {TimeRange} -- the range to check

        Returns:
            boolean -- true if the range is fully contained
        """

        if range_to_compare.start_time < self.start_time:
            # start time before this start time
            return False
        if range_to_compare.end_time > self.end_time:
            # end time after this end time
            return False
        return True

    def __str__(self):
        return "start_time={0}, end_time={1}".format(self.start_time, self.end_time)
