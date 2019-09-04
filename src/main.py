from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta
from ics import Calendar, Event

c = Calendar()
locale_cookie = {"STYXKEY_region": "WORLD.en.Europe/Amsterdam"}
source = requests.get("https://www.ufc.com/events", cookies=locale_cookie).text

soup = BeautifulSoup(source, 'lxml')

upcoming = soup.find("details", {"id": "events-list-upcoming"})

# print(upcoming.prettify())

for upcoming_item in upcoming.find_all("li", {"class": "l-listing__item"}):
    e = Event()

    event_number = upcoming_item.find("div", {"class": "c-card-event--result__logo"})
    event_number = event_number.a["href"]
    event_number = event_number.split("/")[2]
    event_number = event_number.split("-")
    
    if len(event_number) == 2:
        upcoming_item_title = f'UFC {event_number[1]}: {upcoming_item.h3.text}'
    elif len(event_number) > 2 and len(event_number) <= 6:
        upcoming_item_title = f'UFC {event_number[1]} {event_number[2]}: {upcoming_item.h3.text}'

    upcoming_item_date = upcoming_item.find("div", {"class":"c-card-event--result__date"})["data-main-card"]

    now = datetime.now()
    # Sat, Oct 26 / 2:00 PM CEST
    upcoming_item_date = datetime.strptime(now.strftime("%Y") + " " + upcoming_item_date, '%Y %a, %b %d / %I:%M %p CEST')
    
    print(upcoming_item_title)
    print(upcoming_item_date)
    e.name = upcoming_item_title
    e.begin = upcoming_item_date
    e.end = upcoming_item_date + timedelta(hours=3)
    c.events.add(e)

with open('ufc-events.ics', 'w') as ufc_events:
    ufc_events.writelines(c)