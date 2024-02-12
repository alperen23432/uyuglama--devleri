a = int(input("bir sayı girin: "))
b = int(input("bir sayı daha giriniz: "))

toplam = 0

for i in range (a,b+1):
    toplam+=i

ortalama = toplam / (a - b +1)
print("bu sayıların ortalaması:",toplam)