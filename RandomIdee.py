import random

a = ["app","platform","regeling","dienst","game","stuk software"]
b =	["je","vrouwen","mannen","meisjes","jongens","CEOs","armen","immigranten","rijke lui"]
c = ["voelen","horen","zien", "vinden","ruiken","proeven", "leren", "opzoeken"]
d = ["een interactie tussen bedrijven en studenten","een nuttig project","een passende studie","een willekeurig idee", "een nieuwe vaardigheid", "een nieuwe vriendschap", "programmeerkennis"]
e = ["Machine Learning", "Nanotechnology", "Augmented Reality", "Virtual Reality", "Bluetooth"]

for i in range (0,10):
	straa = "Een " + a[random.randint(0,len(a) - 1)] + " die " + b[random.randint(0,len(b) - 1)] + " " + d[random.randint(0, len(d) - 1)] + " laat " + c[random.randint(0,len(c) - 1)] + " door middel van " + e[random.randint(0,len(e) - 1)]
	print(straa)
input()