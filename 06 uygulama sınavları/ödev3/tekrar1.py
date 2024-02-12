import random

def pro():

    print("taş kağıt mağısa hoş geldiniz")

    while True:
        oyun = ["taş","makas","kağıt","kertenkele","spock"]
        bilgisayar= oyun[random.randint(0,2)] 

        sen = str(input("taş kağıt makas spock kertenkele veya (q) ile çıkış: "))

        if sen == "Q" or sen == "q":
            break
        if bilgisayar == sen :
                print("berabere")

        elif bilgisayar == "taş" and sen == "makas":
            print("bilgisayar kazandı")

        elif bilgisayar == "taş" and sen == "kağıt":
            print("sen kazandın")

        elif bilgisayar == "taş" and sen == "spock":
            print("sen kazandın")
 
        elif bilgisayar == "taş" and sen == "kertenkele":
            print("bilgisayar kazandı")  

        elif bilgisayar == "makas" and sen == "taş":
            print("sen kazandın")

        elif bilgisayar == "makas" and sen == "kağıt":
            print("bilgisayar kazan")

        elif bilgisayar == "makas" and sen == "spock":
            print("sen kazandın")

        elif bilgisayar == "makas" and sen == "kertenkele":
            print("bilgisayar kazandı")


        elif bilgisayar == "kağıt" and sen == "makas":
            print("sen kazandın")

        elif bilgisayar == "kağıt" and sen == "taş":
            print("bilgisayar kazandı.")


        elif bilgisayar == "kağıt" and sen == "spock":
            print("sen kazandın")

        elif bilgisayar == "kağıt" and sen == "kertenkele":
            print("sen kazandın")
        
pro()