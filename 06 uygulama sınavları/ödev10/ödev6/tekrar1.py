def info():
    return input("metin giriniz: ")
metin = info()

def kelime_sayaç(metin):
    kelimeler = metin.split()
    return len(kelimeler)
sayaç = kelime_sayaç(metin)

print(sayaç)