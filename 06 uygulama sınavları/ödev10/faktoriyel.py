book = []

print("Kitaphane uygulamasına hoş geldiniz")

def ekleme():
    kitap = input("eklemek istediğiniz kitap ismi yzınız: ")
    yayın_evi = input("yayın evini ekleyiniz: ")
    yazar = input("kitabın yazarını ekleyiniz: ")
    return kitap,yayın_evi,yazar

def liste():
    book1 = ("kitabın ismi :",kitap,"kitabın yayın evi:",yayın_evi,"kitabın yazarın:",yazar )