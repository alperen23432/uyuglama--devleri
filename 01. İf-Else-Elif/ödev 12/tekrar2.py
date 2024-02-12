ağırlık = float(input("Ağırlığınızı kg cinsinden giriniz: "))
boy = float(input("boyunuzu metre cinsinden giriniz: "))

VKI = ağırlık / (boy * boy)

if 18 <= VKI < 25:
    print("normal bir kilonuz var")
elif 25 <= VKI < 30:
    print("kilolusunuz")
elif VKI >= 30:
    print("obez yaratık seni")
else:
    print("bulunamadı")
    