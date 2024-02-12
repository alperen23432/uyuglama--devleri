def apple():
    number_one = int(input("birinci notu giriniz: "))
    number_two = int(input("ikinci notu giriniz: "))
    performance = int(input("performans notunu giriniz: "))

    if (number_one + number_two + performance)/3 >= 50 :
        print("afferin arkadaşım")

    else :
        print("bi dahaki sefere")
apple()