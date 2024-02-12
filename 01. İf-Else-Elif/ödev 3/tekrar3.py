kilo = float(input("Bir Ağırlık Giriniz:"))

ücret = (kilo - 20)*10

if kilo > 20 :
    print(ücret,"tl ek ücret vermen lazım")
else :
    print("ek ücret vermene gerek yok")