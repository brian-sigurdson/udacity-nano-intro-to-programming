import requests

r = requests.get('https://www.metaweather.com/api/location/2455920')
# print(r)
# print()
#
# print(r.text)
# print()
#
weather_dict = r.json()
# print(weather_dict)
# print()
#
# for key in weather_dict:
#     print(key)

print()

for day in weather_dict['consolidated_weather']:
    applicable_date = day['applicable_date']
    humidity = day['humidity']
    print(f"The humidity for {applicable_date} is {humidity}")


