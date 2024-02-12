ürün1 = int(input("Birinci ürünün fiyatını Giriniz:"))
ürün2 = int(input("İkinci ürünün fiyatını Giriniz:")) 

toplam = ürün1 + ürün2
 
if(toplam<200):
    print("Ödenecek miktar:",toplam)
else:
    indirim = toplam - (toplam*0.25)
    
    toplam = toplam - indirim
   
    print("İndirim miktarı:",indirim)
    
    print("Ödenecek miktar:",toplam)