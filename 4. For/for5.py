a = int(input("bir sayı giriniz: "))
b = int(input("bir sayı daha giriniz: "))

toplam=0

for i in range(a,b+1):
    toplam+=i

print("sayıların toplamı:",toplam)