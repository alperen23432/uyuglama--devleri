import defkitap

while True:
    defkitap.seçenek()
    seçim = input("birini seçin:")
    if seçim == "1":
        defkitap.kitap_ekleme()

    elif seçim == "2":
        defkitap.kitap_silme()

    elif seçim == "3":
        defkitap.kitap_listesi()

    elif seçim == "4":
        defkitap.çıkış()
        break
    else:
        print("seçtiğiniz işlem geçersiz")