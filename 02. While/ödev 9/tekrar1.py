toplam = 0
miktar = 0
devam_et = True

while devam_et:
    sayi = int(input("bir sayı giriniz(ortalamayı görmek için 1e basınız): "))

    if sayi == 1:
        print("çıkış yapılıyor.")
        devam_et = False
    else :
        toplam += sayi
        miktar += 1

if miktar > 0:
    ortalama = toplam / miktar
    print("girilen sayıların ortalaması: ", ortalama)
else:
    print("hiç sayı girilmedi")
