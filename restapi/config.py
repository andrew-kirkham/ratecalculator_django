import json
from datetime import datetime
from restapi.time_range import TimeRange

rates = {}

def read_json():
    config = {}
    with open("./restapi/rates.json") as f:
        config = json.load(f)
    parse_config(config['rates'])


def parse_config(config):
    for rate in config:
        parse_rate(rate)


def parse_rate(rate):
    days_for_rate = rate['days'].split(',')
    times = rate['times'].split('-')
    start_time = datetime.strptime(times[0], '%H%M')
    end_time = datetime.strptime(times[1], '%H%M')
    time_range = TimeRange(start_time, end_time)
    for day in days_for_rate:
        rates[datetime.strptime(day[:3], '%a').day][time_range] = rate['price']

for day_num in range(7):
    rates[day_num] = {}
read_json()
