baslangic = int(input("Bir Sayı Giriniz: "))
bitis = int(input("Bir Sayı Giriniz: "))

toplam = 0

while baslangic <= bitis:
    toplam += baslangic
    baslangic += 1

print("sayıların toplamı :", toplam)

