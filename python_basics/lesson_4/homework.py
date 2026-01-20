###  KITOBDAN TOPSHIRIQLAR::::   

# # 41-bet 
# kocha=str(input("Kochani kiriting: "))
# mahalla=str(input("Mahallani kiriting: "))
# tuman=str(input("Tumanni kiriting: "))
# viloyat=str(input("Viloyatni kiriting: "))
# print(f"{kocha} kochasi,\n{mahalla} mahallasi,\n{tuman} tumani,\n{viloyat} viloyati.")

###  44-bet
# x,y,z=10,-5,2.36
# print(f"qiymatlar: {x} {y} {z}")
# ism, yosh = "suhrob", 20
# print(f"{ism.title()} {yosh} yoshda")

# ism = "Jobir"
# yosh = 36
# xabar = ism + " " + str(yosh) + " yoshda"
# print(xabar)

## 46-bet

# ism='jobir'
# yosh=36
# print(type(ism), type(yosh))

### AMALIYOT 46-BET

### TASk 1
# user=int(input("Sonni kiriting: >>> "))
# kvadrati=user**2
# kubi=user**3
# print(f"{user} ning kvadrati {kvadrati} ga teng\n{user} ning kubi {kubi} ga teng")

####  TASK 2

# yoshingiz=int(input("Yoshingizni kiriting:>>> "))
# hozirgi_yil=2025
# tugilgan_yili=hozirgi_yil-yoshingiz
# print(f"Siz {tugilgan_yili} -yilda tug'ulgansiz.")


# ### TASK 3

# son_1=int(input("Birinchi sonni kiriting:>>> "))
# son_2=int(input("Ikkinchi sonni kiriting:>>> "))

# yigindi=son_1+son_2
# ayirma=son_1-son_2
# kopaytmasi=son_1*son_2
# bolinmasi=son_1/son_2

# print(f"Yig'indi { yigindi}\nAyirma {ayirma}\nKopaytma {kopaytmasi}\nBo'linma {bolinmasi}")

#####  RO'YXATLAR USTIDA AMALLAR
# cars=[]

# cars.append("Lasetti")
# cars.append("Damas")
# cars.append("Spark")
# cars.insert(2, "Malibu")
# cars.insert(0, "Cobalt")
# cars.append("Traktor")
# cars.insert(3, "Cobalt")
# del cars[2]
# cars.remove("Spark")
# cars.remove("Cobalt")
# print(cars)

# bozorlik=["yog", "un", "piyoz", "baban", "go'sht"]
# mahsulot=bozorlik.pop(3)
# print("Men " + mahsulot + " sotib oldim")
# print("OLinmagan mahsulotlar:", bozorlik)


###  AMALIYOT 54-BET  TASK 1 

# ismlar=["Elbek", "Javohir", "Nodir"]
# name_1=ismlar.pop(0)
# name_2=ismlar.pop(0)
# name_3=ismlar.pop(0)
# print(f"Salom {name_1} qandaysan ishlaring yaxshimi")
# print(f"{name_2} qalesan zormisan?")
# print(f"{name_3} nima gaplar ?")

## TASK 2

# sonlar=[45, -75, 25.14, 0.25]
# sonlar[2]=45.88
# sonlar[3]=sonlar[3]+100

# print(sonlar)

# narxlar=[12000, 22500, 23456, 9800, 5600, 9934, 32874]
# arzon=min(narxlar)
# qimmat=max(narxlar)
# jami=sum(narxlar)
# print("eng arzon narx", arzon, \
#       ". eng qimmati ", qimmat, \
#         ". jami ", jami)


# sonlar=[1, 2, 3, 4, 5]
# sonlar_1=sonlar[:]
# sonlar_1.append(6)
# sonlar_1.append(7)
# print("bu sonlar ro'yxati:", sonlar)
# print("Bu sonlar_1 ro'yxati: ", sonlar_1)


####  AMALIYOT 63-BET   TASK 1

# davlatlar=["O'zbekiston", "Bolgariya", "Germainya", "AQSH", "Rassiya"]
# uzunligi=len(davlatlar)

# # print(sorted(davlatlar, reverse=True))
# # print(uzunligi)
# # print("asl ro'yxat:", list(reversed(davlatlar)))
# davlatlar.sort(reverse=True)
# print(davlatlar)

###   TASK 2

# raqamlar=list(range(120, 1201, 2))
# yigindi=sum(raqamlar)
# katta=max(raqamlar)
# kichik=min(raqamlar)
# yigindi=katta-kichik
# uzunlik=len(raqamlar)
# royxat_boshidan=raqamlar[0:21]
# orta_index=uzunlik//2
# royxat_ortasidan=raqamlar[orta_index-10:orta_index+10]
# royxat_oxiridan=raqamlar[-20:]
# print("Boshidan: ", royxat_boshidan, "\nO'rtasidan: ", royxat_ortasidan, "\nOxiridan: ", royxat_oxiridan)



# ####  TASK 3


# taomlar=["osh", "manti", "somsa", "qazi", "shorva"]
# nonushta=taomlar[:]
# nonushta.remove("qazi")
# nonushta.append("sumalak")
# nonushta.append("tort")
# nonushta[0]="qaymoq va non"
# nonushta=tuple(nonushta)
# print(taomlar)
# print(nonushta)



######   FOR SIKLI

# mehmonlar=["ali", "vali", "alisher", "ravshan", "shirin"]
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, ")
#     print("Sizni 20-mart kuni nahorgi oshga taklif qilamiz. ")
#     print("Hurmat bilan, Panjiyevlar oilasi")


# cars=['nexia', 'tico', 'damas']
# for car in cars:
#     print(car.title())
# print("Ko'rganlar qilar havas")

# sonlar=list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")

# sonlar=list(range(11))
# sonlar_kvadrati=[]
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
# print(sonlar)
# print(sonlar_kvadrati)

# dostlar=[]
# print("Eng yaqin 5ta dosringiz kim?")
# for n in range(1, 6):
#     dostlar.append(input(f"{n}-ismini kiriting: "))
# print(dostlar)


##### AMALIYOT  TASK 1

# ismlar=["ali", "vali", "hasan", "husan", "olim"]
# a=0
# for ism in ismlar:
#     a=a+1
#     print(ism, "qalesan")
# print(f"Kod {a} martta takrorlandi")

### TASK 2

# for n in range(11, 100, 2):
#     a=n**3
#     print(f"{n} ning kubi {a}")

### TASK 3

# kinolar=[]
# print("Yoqtirgan kinolaringizni kiriting.")
# for n in range(1, 6):
#     kinolar.append(input(f"{n}-kinoyingiz? "))
# print(kinolar)


####   TASK 4

# royxat=[]
# a=int(input("Bugun nechta odam bilan suhbatlashdingiz? "))

# for n in range(a):
#     royxat.append(input(f"{n+1}-suhbatlashgan odamingiz? "))
# print(royxat)



#####  4 BOB (SHARTLAR VA TARMOQLANISH) 

# x=10
# print
# (x*x>=float(f"{x**2}"))


# avtolar=["audi", "bmw", "volvo", "kia", "hyundai"]
# for avto in avtolar:
#     if avto=="bmw":
#         print(avto.upper())
#     else:
#         print(avto.title())


##########    KITOB 90-BET  AMALIYOT 

# user=int(input("Juft son kiriting: "))
# if user % 2 ==0:
#     print("Rahmat")
# elif user % 2 !=0:
#     print("Bu son juft emas.")


# yosh=int(input("Yoshingizni kiriting: "))
# if yosh < 4 or yosh > 60:
#     print("Sizga kirish bepul.")
# elif yosh < 18:
#     print("Chipta puli 10 ming so'm. ")
# elif yosh > 18:
#     print("Chipta puli 20 ming so'm ")


son1=int(input("son1 ni kiriting: "))
son2=int(input("son2 ni kiriting: "))
if son1>son2:
    print("son 1 katta")
elif son1<son2:
    print("son 2 katta")
else:
    print("Ikkalasi ham teng")