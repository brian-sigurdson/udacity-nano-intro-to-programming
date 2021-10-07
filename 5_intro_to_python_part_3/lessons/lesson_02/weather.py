weather = [
    {
        'date': 'today',
        'state': 'cloudy',
        'temp': 68.5
    },
    {
        'date': 'tomorrow',
        'state': 'sunny',
        'temp': 74.8
    }
]

# for e in weather:
#     print(e)
# print()
#
# for e in weather[0]:
#     print(e)
# print()
#
# for e in weather[0].values():
#     print(e)
# print()
#
for forecast in weather:
    print(f"The weather for {forecast['date']} will be {forecast['state']} with a temperature of {forecast['temp']}"
          f" degrees.")

