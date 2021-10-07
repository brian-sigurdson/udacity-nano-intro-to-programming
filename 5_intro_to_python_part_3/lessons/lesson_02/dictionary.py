pets = {
    'birds': {
        'parrot': 'Arthur',
        'canary': 'Ford'
    },
    'fish': {
        'goldfish': 'Zaphod',
        'koi': 'Trillium'
    }
}

for key in pets:
    print(key)

for value in pets.values():
    print(value)

for items in pets.items():
    print(items)

for e in pets['birds']:
    print(e)

for e in pets['birds'].values():
    print(e)

