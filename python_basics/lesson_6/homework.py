# # 1.  ##### tub va murakkab sonlarning ro'yxatini chiqarish

# print("Tub yoki murakkab sonlarni aniqlovchi dastur:")
# tub_sonlar=[]
# murakkab_sonlar=[]
# a=0
# b=0
# while True:
#     if ((a != 5) and (b != 5)):
#         user = input("Sonni kiriting: (chiqish uchun 'exit' ni yozing.): ")
#         if user == 'exit':
#             print("Dastur to'xtadi.")
#             break
#         user = int(user)
#         if user == 1:
#             print("1 — na tub, na murakkab.")
#             continue

#         tub = True   # ishora usuli

#         for i in range(2, user):
#             if user % i == 0:   # user murakkab son bulsa if ning ichiga kiradi va ishora false bulgani uchun else operatori orqali murakkab songa qushiladi.

#                 tub = False
#                 break

#         if tub:
#             tub_sonlar.append(user)
#             a+=1
#             print(f"{user} — tub son.")
            
#         else:
#             murakkab_sonlar.append(user)
#             b+=1
#             print(f"{user} — murakkab son.")
            
#     else:
#         print(f"🔢 Tub sonlar ro'yxati: {tub_sonlar}.")
#         print(f"🔢 Murakkab sonlar ro'yxati: {murakkab_sonlar}.")
#         print(f"✅ 5 ta tub yoki murakkab son topildi. Dastur yakunlandi.")
#         break






#### 2 2.uyga vazifa user kritigan son necha xonali ekanligini topish
#####  masalan: 12: 2 xonali, 5634: 4 xonali

# user=int(input("Son kiriting: "))
# t=0
# while user !=0 :
#     user = user // 10
#     t=t+1
# print(f"Siz kiritgan son {t} xonali")




######   3   kiritilgan sonni oxirgi raqamini topish

# print("Oxirgi raqamni topuvchi dastur: ")

# while True:
#     user=(input("Son kiriting: "))
#     if user=="stop":
#         print("Dastur to'xtadi.")
#         break

#     user=int(user)
#     a=user % 10
#     print(f"{user} ning oxirgi raqami {a} ga teng.")



##### 4.  kiritlgan sonni ketma ket 5 marta 2 ga bo'lganda chiqadigan sonnit opish (integreda)

# user=int(input("Sonni kiriting: >>> "))
# t=0
# while t!=5:
#     user=user//2
#     t=t+1
#     print(user, end=" ")