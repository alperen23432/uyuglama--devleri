kilogram = float(input("Bir ağırlık giriniz: "))

ek_ücret = (kilogram - 20)*10

if kilogram > 20 :
    print("ücret vermen lazım",ek_ücret)
else :
    print("ücret vermen lazım değil")

