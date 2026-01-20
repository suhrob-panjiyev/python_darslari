print("Welcome to calculator programming. :) ")
print("Kalkulyatordan foydalanish uchun (a va b) sonlar va amallar(+, -, /, *) dan foydalaning. ")


while True:

    a=input("Birinchi sonni kiriting(To'xtatish uchun 'stop' ni yozing.) a= ")
    if a == "stop":
        print("Kalkulyator to'xtadi. ")
        break

    amal_belgisi=input("Amal belgisini kiriting(+, -, /, *)/(To'xtatish uchun 'stop' ni yozing.): >>> ")
    if amal_belgisi == "stop":
        print("Kalkulyator to'xtadi. ")
        break
    if (amal_belgisi != "+") and (amal_belgisi != "-") and (amal_belgisi != "*") and (amal_belgisi != "/") and (amal_belgisi != 'stop'):
        print("Amalni qayta kiriting(+, -, /, *, 'stop'): >>> ") 
        continue
        

    b=input("Ikkinchi sonni kiriting(To'xtatish uchun 'stop' ni yozing.) b= ")
    if b == "stop":
        print("Kalkulyator to'xtadi. ")
        break

    a=float(a)
    b=float(b)

    if amal_belgisi == "+":
        natija = a + b
        print(f"{a} + {b} = {natija} ga teng. ")

    elif amal_belgisi == "-":
        natija = a - b
        print(f"{a} - {b} = {natija} ga teng. ")

    elif amal_belgisi == "*":
        natija = a * b
        print(f"{a} * {b} = {natija} ga teng. ")

    elif amal_belgisi == "/":
        if b == 0:
            print("b noll ga teng bo'lmasligi kerak, qayta kiriting: ")
            continue
        else:
            natija = a / b
            print(f"{a} / {b} = {natija} ga teng. ")