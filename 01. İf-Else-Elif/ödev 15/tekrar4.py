a = input("tiyatro yada sinema  iksinden birini seçıiz: ")
b = input("Öğrenci veya sivil olduğunuzu seçiniz: ")

if a == "tiyatro":
    if b == "öğrenci":
        print("5tl")
    elif b == "sivil":
        print("10tl")
elif a == "sinema":
    if b == "öğrenci":
        print("7,5tl")
    elif b == "sivil":
        print("15tl")