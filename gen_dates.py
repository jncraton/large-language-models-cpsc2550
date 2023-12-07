from dateutil.rrule import rruleset, rrule, WEEKLY, MO, TU, WE, TH, FR
from datetime import datetime
import csv
import json
from itertools import zip_longest

config = json.load(open('config.json'))

day_map = {"M": MO, "T": TU, "W": WE, "R": TH, "F": FR}
day3_map = {"Mon": "M", "Tue": "T", "Wed": "W", "Thu": "R", "Fri": "F"}
lecture_days = [day_map[d] for d in config["lecture_days"] + config["lab_days"]]

rules = rruleset()
rules.rrule(
    rrule(
        WEEKLY,
        dtstart=datetime.fromisoformat(config["start_date"]),
        until=datetime.fromisoformat(config["end_date"]),
        byweekday=lecture_days,
    )
)
for b in config["breaks"]:
    rules.exdate(datetime.fromisoformat(b))

with open('topics.tsv') as f:
    lectures = csv.DictReader(f, dialect='excel-tab')

    start_week = None
    
    for i, day in enumerate(zip_longest(rules, lectures)):
        if not start_week:
            start_week = int(day[0].strftime("%V")) - 1

        dow = day3_map[day[0].strftime("%a")]
        week = int(day[0].strftime("%V")) - start_week

        if dow in config['lab_days']:
            assert day[1]['type'] == 'lab', f'Day should be lab {i+2}'

        print(f"Week {week} {day[1]['type'].title()}: {day[1]['name'] if day[1] != None else 'Out of topics'} ({day[0].strftime('%A, %B %d')})")
