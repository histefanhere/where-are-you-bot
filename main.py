# from ics import Calendar
import datetime
import icalendar
import recurring_ical_events
import requests

url = 'https://uoacal.auckland.ac.nz/calendar/1c43b64b63a6ed6761594ba513a9a55ff7a9fbd50da28ed417ab0b78eaa768485e34275a4ca52274f19f4b1619d59d44c5959131b2f84ac1cbeb265f32cbc0c6'

cal = icalendar.Calendar.from_ical(requests.get(url).text)
rcal = recurring_ical_events.of(cal)

# a_date = (2022, 7, 26)

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)

class MyEvent:
    def __init__(self, event):
        self.summary = event.get('SUMMARY')
        self.description = event.get('DESCRIPTION')
        self.location = event.get('LOCATION')
        self.start = event.get('DTSTART').dt
        self.end = event.get('DTEND').dt
        self.dtstamp = event.get('DTSTAMP')
    
    def __str__(self):
        return f"Name: {self.summary} - {self.description}\n\tstart: {self.start.strftime('%Y-%m-%d %H:%M')}\n\tend: {self.end.strftime('%Y-%m-%d %H:%M')}\n\tlocation: {self.location}"

events = []
for event in rcal.at(tomorrow):
    events.append(MyEvent(event))

events.sort(key=lambda x: x.start)

for event in events:
    print(str(event))
