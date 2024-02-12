a = ["35","26","81","64"]
a2 = a.copy()
a.sort()
print(a)

a.reverse()
print(a)

b = a.count("26")
print(b)

a.pop(2)
print(a)

print(a2.index("64"))

a.clear()
print(a)
