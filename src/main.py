from bs4 import BeautifulSoup
import requests

locale_cookie = {"STYXKEY_region": "WORLD.en.Europe/Amsterdam"}
source = requests.get("https://www.ufc.com/events", cookies=locale_cookie).text

soup = BeautifulSoup(source, 'lxml')

upcoming = soup.find("details", {"id": "events-list-upcoming"})

# print(upcoming.prettify())

for upcoming_item in upcoming.find_all("li", {"class": "l-listing__item"}):
    upcoming_item_title = upcoming_item.h3.text
    upcoming_item_date = upcoming_item.find("div", {"class":"c-card-event--result__date"})["data-main-card"]

    print(upcoming_item_title)
    print(upcoming_item_date)
