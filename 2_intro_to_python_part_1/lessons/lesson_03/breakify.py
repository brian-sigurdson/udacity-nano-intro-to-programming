lines = ["Haiku frogs in snow",
         "A limerick came from Nantucket",
         "Tetrametric drum-beats thrumming, Hiawathianic rhythm."]


def breakify(lines):
    return "<br>".join(lines)


print(breakify(lines))