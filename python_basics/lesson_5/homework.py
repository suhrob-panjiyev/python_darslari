1.  ####  tub sonlarni aniqlash
2.  #### 1 dan 100gacha bulgan sonni topish uchun algoritm >?

3.  ###  92betgacha va 117 dan 127 gacha
4.  ### mukammal kalkulyator while dan foydalanamiz



##### KITOBDAN 117-BET    6-BOB  WHILE SIKLI


# print("Kiritilgan soinning kvadratini qaytaruvchi dastur: ")
# savol= "Istalgan son kiriting: To'xtatish uchun 'exit' deb yozing: "
# qiymat=" "
# while qiymat!= "exit" :
#     qiymat =input(savol)
#     if qiymat !="exit":
#         print(float(qiymat)**2)
#     else:
#         print("Dastur tuxtadi.")


# print("kiritilgan sonning kvadratini qaytaruvchi dastur:")
# savol="Istalgan sonnni kirting"
# savol+=" To'xtataish uchun 'exit' deb yozing."

# while True:
#     qiymat=input(savol)
#     if qiymat=='exit':
#         print("dastur tuxtadi.")
#         break
#     else:
#         print(float(qiymat)**2user

# user="Istalgan sonnni kirting, To'xtataish uchun 'exit' deb yozing."
# while True:
#     son=input(user)
#     if son =='exit':
#         print("Dastur tuxtadi.")
#         break
#     elif son !='exit':
#         print(float(son)**3)



# son=0
# while son<10:
#     son+=1
#     if son%2==0:
#         continue
#     else:
#         print(son, end=" ")



# son = 0
# while son <10:
#     son+=1
#     if son%2!=0:
#         continue
#     else:
#         print(son)


####  AMALIYOT TASK 1

# print("Yaxshi kurgan kitoblaringizni yozing: ")
# user="Istalgan kitobingzini kiriting, To'xtatish uchun 'stop' ni yozing. "
# while True:
#     a=input(user)
#     if a=='stop':
#         print("Dastur tuxtadi.")
#         break
#     else:
#         print(a)

# ###  TASK 2 

# yosh="yoshingizni kiriting: "
# while True:
#     user=input(yosh)
#     if user=='quit' or user == 'exit':
#         print("Dastur tuxtadi: ")
#         break
#     user=int(user)
#     if user <= 7:
#         print("Kirishingiz mumkin: Chipta narxi 2 ming som.")
#     elif 7 < user <= 18:
#         print("Kirishingiz mumkin: Chipta narxi 3 ming som.")
#     elif 18 < user < 65:
#         print("Kirishingiz mumkin: Chipta narxi 10 ming som.")
#     elif user >= 65:
#         print("Kirishingiz mumkin: Sizga bepul.")


##### TASK 3 

# savol="Kiritilgan sonning ildizini qaytaruvchi dastur. \n"
# savol+= "Musbat son kiriting. "
# savol+= "dasturni to'xtatish uchun 'exit' deb yozing. "

# while True:
#     qiymat=input(savol)
#     if qiymat=='exit':
#         print("Dastur to'xtadi.")
#         break
#     qiymat=int(qiymat)
#     if qiymat<0:
#         continue
#     else:
#         ildiz=float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng.")



# ismlar=[]
# print("Yaqin do'stlaringizni ro'yxatini qo'shamiz. ")
# n=1
# while True:
#     savol=f"{n}-do'stingiz ismini kiriting. "
#     ism=input(savol)
#     ismlar.append(ism)
#     javob=input("Yana ism qo'shasizmi? (ha/yo'q) ")
#     if javob=="ha":
#         n+=1
#         continue
#     else:
#         break
# print("Ro'yxat tuzildi.")


# print("Do'stlaringiz ro'yxati: ")
# for ism in ismlar:
#     print(ism.title())



# print("Yoqtirgan mevalaringiz ro'yxati: ")
# fruits=[]
# n=1
# while True:
#     question=input(f"{n}-mevangizni kiriting: ")
#     fruits.append(question)
#     answer=input("Yana meva qushasizmi? (ha/yo'q)")
#     if answer=="ha":
#         n+=1
#         continue
#     else:
#         break
# print("Ro'yxat tuzildi.")

# print("Mevalar ro'yxati:")
# for fruit in fruits:
#     print(fruit.title())




# cars=["malibu", "nexia", "damas", "gentra", "nexia", "cobolt", "traktor", "nexia", "velik"]
# while "nexia" in cars:
#     cars.remove("nexia")
# print(cars)  



########   AMALIYOT  127-BET      TASK 1


# print("Buyurmalaringizni kiriting: ")
# buyurtmalar=[]
# n=1
# while True:
#     a=input(f"{n}-buyutmangizni kiriting: ")
#     buyurtmalar.append(a)
#     b=input("Yana buyurtma qilasizmi? (ha/yo'q). ")
#     if b=="ha":
#         n+=1
#         continue
#     elif b=="yo'q":
#         break
# print("Buyurtmalar qabul qilindi :) Sizning buyurtmalaringiz: ")

# for buyurtma in buyurtmalar:
#     print(buyurtma.title())


######     TASK 2  va  task  3

#   (lug'at hali utilmagan)






1.  ####  tub sonlarni aniqlash
2.  #### 1 dan 100gacha bulgan sonni topish uchun algoritm >?

3.  ###  92betgacha va 117 dan 127 gacha
4.  ### mukammal kalkulyator while dan foydalanamiz




print("Tub yoki murakkab sonlarni aniqlovchi dastur:")

while True:
    user = input("Sonni kiriting: (chiqish uchun 'exit' ni yozing.): ")
    if user == 'exit':
        print("Dastur to'xtadi.")
        break
    user = int(user)
    if user == 1:
        print("1 — na tub, na murakkab.")
        continue

    tub = True   # ishora usuli

    for i in range(2, user):
        if user % i == 0:   # user murakkab son bulsa if ning ichiga kiradi va ishora false bulgani uchun else operatori orqali murakkab songa qushiladi.
            tub = False
            break

    if tub:
        print(f"{user} — tub son.")
    else:
        print(f"{user} — murakkab son.")
