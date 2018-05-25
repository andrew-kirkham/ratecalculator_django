# /usr/bin/python
"""config

Read the .json config files and map them to a dict for use
"""

import json
import calendar
from datetime import datetime
import pytz
from restapi.models.time_range import TimeRange

rates = {}
config = {}

def read_file():
    """
    Read the json config file for parsing
    """

    global config
    with open('./restapi/rates.json') as f:
        config = json.load(f)
    parse_config(config['rates'])


def parse_config(config):
    for rate in config:
        parse_rate(rate)


def parse_rate(rate):
    """parse an individual rate from the config

    Arguments:
        rate {dict} -- a dictionary containing days, times, and price
    """

    days_for_rate = rate['days'].split(',')
    times = rate['times'].split('-')
    #conver the HHMM timestamp to a UTC timestamp
    start_time = datetime.strptime(times[0], '%H%M').replace(tzinfo=pytz.UTC)
    end_time = datetime.strptime(times[1], '%H%M').replace(tzinfo=pytz.UTC)
    #convert timestamp to a time range
    time_range = TimeRange(start_time, end_time)
    for day in days_for_rate:
        #apply the price to each time range
        day_of_week = list(calendar.day_abbr).index(day[:3].capitalize())
        rates[day_of_week][time_range] = rate['price']


for day in range(7):
    rates[day] = {}

read_file()
