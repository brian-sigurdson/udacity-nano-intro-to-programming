import requests


r = requests.get('https://www.metaweather.com/api/location/search/?query=New%20Delhi')

if r.status_code == 200:
    print("successful request")
elif r.status_code == 400:
    print("page not found")
else:
    print("something else is wrong")

    
