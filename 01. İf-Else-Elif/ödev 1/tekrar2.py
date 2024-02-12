def pro():
    n1 = int(input("birincİ notu giriniz: "))
    n2 = int(input("ikinci notu giriniz: "))
    performans = int(input("performans notunu giriniz: "))

    if (n1 + n2 + performans)/3 >= 50:
        print("Afferin")
    else:
        print("Başarısız")

pro()
    
