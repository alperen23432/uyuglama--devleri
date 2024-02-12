saat = float(input("otoparkta kaç saat kaldınız: "))

if saat <= 1:
    print("ücret 5 tl")
elif saat <= 5:
    print("ücret:",5 + (hour - 1) * 4)
else :
    fiyat = 5 + 4 * 4  + (hour - 5) * 3:
    