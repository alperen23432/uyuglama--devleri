import os
 
print("Bilgisayarı yeniden başlatmak için saniye girin: ")
saniye = int(input())
 
kapatmaKodu = "shutdown /r /t " + str(saniye)
 
os.system(kapatmaKodu)
