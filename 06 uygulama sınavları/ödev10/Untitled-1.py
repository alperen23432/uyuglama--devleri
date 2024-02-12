toplam=0

for i in range (1 ,10000000000000):
    if i % 3 == 0 or i % 5 == 0:
        toplam += i

print(toplam)