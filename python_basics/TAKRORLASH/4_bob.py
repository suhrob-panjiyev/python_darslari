#######       4-BOB   #########

# menyu=["osh","qazonkabob","shashlik","norin","lag'mon"]
# ovqat=input("Nima ovqat yeysiz?: ")
# if ovqat.lower() not in menyu:
#     print("Afsuski bizdan bunday ovqat yuq.")
# else:
#     print("Buyurtma qabul qilindi, tez orada yetkazib beramiz.")


########        AMALIYOT            ########

# user=int(input("Juft son kiriting: "))
# if user % 2 == 0:
#     print("Rahmat!")
# else:
#     print("Bu son juft emas!")




# yosh=int(input("Yoshingiz nechida?: "))

# if yosh<4 or yosh>60:
#     print("Sizga kirish bepul!")
# elif yosh<18:
#     print("Kirish narxi 10000 so'm")
# else:
#     print("Kirish narxi 20000 so'm")



# 10 ta mahsulot
# mahsulotlar=["un","yog'","shakar","tuxum","sovun","kartoshka","piyoz","sabzi","guruch","makaron"]
# savat=[]
# bor_mahsulotlar=[]
# mavjud_emas=[]
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni kiriting: "))
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# if len(mavjud_emas)==0:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
# else:
#     print("Quyidagi mahsulotlar do'konimizda yo'q:")
#     for i in mavjud_emas:
#         print(i)




# foydalanuvchilar=["admin","ali","vali","hasan","husan"]
# login=input("Yangi login tanlang: ")
# if login.lower().strip() in foydalanuvchilar:
#     print("Login band, yangi login tanlang!")
# else:
#     print(f"Xush kelibsiz, {login}!")


user=int(input("Son kiriting: "))
bulinadigan_sonlar=[]
bulinmaydigan_sonar=[]
for i in range(2, 11):
    if user % i == 0:
        bulinadigan_sonlar.append(i)
    else:
        bulinmaydigan_sonar.append(i)
print(f"Bulinadiganlari: {bulinadigan_sonlar}")
print(f"Bulinmaydiganlari esa: {bulinmaydigan_sonar}")