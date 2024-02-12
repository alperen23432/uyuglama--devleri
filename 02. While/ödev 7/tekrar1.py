ilk = int(input("İlk sayıyı giriniz: "))
son = int(input("İkinci sayıyı giriniz: "))

toplam = 0
sayi_mik = 0

while ilk <= son:
    toplam += ilk
    sayi_mik += 1
    ilk += 1

ortalama = toplam / sayi_mik
print("Girilen sayıların ortalaması:", ortalama)