import random

def zar():
    return random.randint(1,1500)

operation = int(input("kaç defa zar atılsın: "))

for i in range(operation):
    result = zar()
    print(f"atılan zar: {result}")