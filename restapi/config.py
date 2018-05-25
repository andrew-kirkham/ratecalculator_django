# /usr/bin/python
import json
import calendar
import pytz
from datetime import datetime
from restapi.models.time_range import TimeRange

rates = {}
config = {}

def read_file():
    global config
    with open('./restapi/rates.json') as f:
        config = json.load(f)
    parse_config(config['rates'])


def parse_config(config):
    for rate in config:
        parse_rate(rate)


def parse_rate(rate):
    days_for_rate = rate['days'].split(',')
    times = rate['times'].split('-')
    start_time = datetime.strptime(times[0], '%H%M').replace(tzinfo=pytz.UTC)
    end_time = datetime.strptime(times[1], '%H%M').replace(tzinfo=pytz.UTC)
    time_range = TimeRange(start_time, end_time)
    for day in days_for_rate:
        day_of_week = list(calendar.day_abbr).index(day[:3].capitalize())
        rates[day_of_week][time_range] = rate['price']


for day in range(7):
    rates[day] = {}

read_file()
