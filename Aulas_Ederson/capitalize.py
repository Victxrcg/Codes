a="victor"
print(a.capitalize())
b="CARRO"
print(b.lower())
c="viajem"
print(c.upper())
d="PAISAGEM"
print(d.casefold())

print("LOCAL".lower())


print("local".upper())


print("local".capitalize())

print(a.isupper())

ab="193819203"
print(ab.isdigit())

ab="aaaaaa"
print(ab.isdigit())

ma="Victor galvao"
print(ma.replace("galvao","Antunes"))

ia="victor-galvao-queiroz-antunes"
print(ia.split("."))

m="nhdfahjfahjfajfnadkçfha"
print(m.find("a"))

ba="victor-galvao-queiroz-antunes"
print("victor"in ba)

print(ba.count("a"))
print(ba.count("v"))
print(ba.count("galvao"))
print(ba.count("u"))
print(ba.count("z"))

print(ba[0:6])

print(ba[0:10])

print(ba[0:])