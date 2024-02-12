books = []
#------------------------------------------------------------------------------------------------------------------
while True:
    
    choice = input("1.= kitap listesini gör: \n2.=kitap ekle \n3.= kitap silme \n4.= çıkış \n")

    if choice == "1":

        for book_key in books:

            print(book_key)
#---------------------------------------------------------------------------------------------------------------------
    elif choice == "2":

        id = len(books) + 1
        
        isim = input("kitap ismini giriniz: ")
        
        yazar = input("yazarını giriniz: ")
        
        yayın_evi = input("yayın evini giriniz: ")
        
        books.append({"id":id,"isimi":isim,"yönetmeni":yazar,"yayın evi":yayın_evi})
#---------------------------------------------------------------------------------------------------------------------
    elif choice == "3":

        for book_key in books :

            print(book_key)

        book_remove = int(input("hangi kitabı silmek istediğinizi seçiniz: "))

        books.pop(book_remove - 1)

        for books_key in books:

            print(books_key)
#---------------------------------------------------------------------------------------------------------------------------
    elif choice == "4":

        print("çıkış yapılıyor ")

        break
