# son_1=int(input("son 1 ni kiriting: "))
# son_2=float(input("son 2 ni kiriting: "))

# if son_1==son_2:
#     print("sonlar teng")
# else:
#     print("Sonlar teng emas")


# students=["Ali", "Vali", "Oysha", "Sharif", "Bolta", "Tesha"]
# for student in students:
#     ism_uznligi=0
#     for letter in student:
#         ism_uznligi+=1
#     if ism_uznligi>4:
#         print(student)


# a=int(input("a ni kirit: "))
# b=int(input("b ni kirit: "))
# c=int(input("c ni kirit: "))
# if a>b:
#     print(a)
# elif a<b:
#     print(b)
# else:
#     ("teng")
# else:
## ikkita else yozib bulmaydi 


#######  while  loopi: _________

# son=0
# while True:
#     son+=1
#     if son==5:
#         print(f"{son} 5 ga teng boldi shu sababdan breaking")
#         break


# son=0
# while son<5:
#     son+=1
#     print(son)



###  o'yin yaratamiz   o'yla izla top

# import random
# komp_number=random.randint(1, 10)
# print(komp_number)
# imkon_kodi=5
# while imkon_kodi>0:
#     user_num=int(input("raqam kirit: "))
#     if user_num==komp_number:
#         print("Siz yutdingiz")
#         break
#     else:
#         print("keyingi raqam kirit:, hozircha topolmadingiz :)")
#     imkon_kodi-=1


# birdan 10 gacha toq sonlar yig'indisini topish
son=1
yigindi=0
while son<10:
    yigindi=yigindi+son
    son=son+2
print("1 dan 10 gacha toq sonlar yig'indisi: ", yigindi)
