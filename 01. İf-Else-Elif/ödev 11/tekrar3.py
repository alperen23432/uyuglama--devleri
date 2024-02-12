a1 = int(input("birinci açıyı giriniz: "))
a2 = int(input("ikinci açıyı giriniz: "))
a3 = int(input("üçüncü açıyı giriniz: "))

if a1 == a2 == a3:
    print("Bu Bir Eş Kenar Üçgen")
elif a1 == a2 or a1 == a3 or a2 == a1 or a2 == a3 or a3 == a1 or a3 == a2:
    print("Bu Bir İkiz Kenar Üçgen")
else:
    print("Bu Bir Çeşit Kenar Üçgen")