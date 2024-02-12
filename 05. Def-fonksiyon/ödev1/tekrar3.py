def file():
    number_one = int(input("birinci sayıyı giriniz: "))
    number_two = int(input("ikinci sayıyı giriniz: "))
    number_tree = int(input("üçüncü sayıyı giriniz: "))

    if (number_one + number_two + number_tree)/3 >= 50:
        print("afferin ")
    else:
        print("bi dahaki sefere")

file()