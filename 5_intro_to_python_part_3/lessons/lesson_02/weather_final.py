# TO DO:
# 1. Have display_weather print the weather report.
# 2. Handle network errors by printing a friendly message.
#
# To test your code, open a terminal below and run:
#   python3 weather.py


import requests

API_ROOT = 'https://www.metaweather.com'
API_LOCATION = '/api/location/search/?query='
API_WEATHER = '/api/location/'  # + woeid


def fetch_location(query):
    try:
        r = requests.get(API_ROOT + API_LOCATION + query).json()
    except requests.exceptions.ConnectionError:
        print("Connection error.")

    return r


def fetch_weather(woeid):
    return requests.get(API_ROOT + API_WEATHER + str(woeid)).json()


def display_weather(weather):
    print(f"Weather for {weather['title']}:")
    for day in weather['consolidated_weather']:
        applicable_date = day['applicable_date']
        humidity = day['humidity']
        print(f"The humidity for {applicable_date} is {humidity}")


def disambiguate_locations(locations):
    print("Ambiguous location! Did you mean:")
    for loc in locations:
        print(f"\t* {loc['title']}")


def weather_dialog():
    where = ''
    while not where:
        where = input("Where in the world are you?\n ")
    locations = fetch_location(where)
    if len(locations) == 0:
        print("I don't know where that is.")
    elif len(locations) > 1:
        disambiguate_locations(locations)
    else:
        woeid = locations[0]['woeid']
        display_weather(fetch_weather(woeid))


if __name__ == '__main__':
    while True:
        weather_dialog()