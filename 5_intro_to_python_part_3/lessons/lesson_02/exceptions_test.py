import requests


try:
    r = requests.get('https://www.udacity.com')
    print(r.status_code)
except requests.exceptions.ConnectionError:
    print("There is a problem connecting to the server")



