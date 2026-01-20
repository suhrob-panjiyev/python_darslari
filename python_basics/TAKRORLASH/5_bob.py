###########   5-BOB    ###########


# car={
#     "model":"BMW",
#     "rang":"oq",
#     "yil":2020,
#     "narh":50000,
#     "km":20000,
#     "karobka":"avtomat"
# }
# narx=car.get("narx")
# print(narx)



# talaba={
#     "ism":"Ali",
#     "familiya":"Valiyev",
#     "yosh":20,
#     "fakultet":"Informatika"
# }
# talaba["yosh"]=21
# talaba["jinsi"]="erkak"
# print(talaba)


# car={}
# car["model"]="Lacetita 3"
# car["narxi"]=40000
# car["color"]="dark black"
# car["yili"]=2025
# print(f"Modeli: {car['model']}, Narxi: {car['narxi']}, Rangi: {car['color']},  Yili: {car['yili']}")




# ________________________________________________________________________________________________________________________________
# ________________________________________________________________________________________________________________________________
# ________________________________________________________________________________________________________________________________




# ###########       AMALIYOT         ###########

# otam={
#     "ism":"Abdulla",
#     "t_yil":1965,
#     "t_joy":"Toshkent",
#     "kasb":"muhandis"
# }
# onam={
#     "ism":"Gulnora",
#     "t_yil":1970,
#     "t_joy":"Samarqand",
#     "kasb":"o'qituvchi"
# }
# akam={
#     "ism":"Jasur",
#     "t_yil":1995,
#     "t_joy":"Toshkent",
#     "kasb":"dasturchi"
# }
# print(f"Otamning ismi {otam['ism']}, u {otam['t_joy']}-da tug'ilgan, {otam['t_yil']}-yilda. Kasbi: {otam['kasb']}.")
# print(f"Onamning ismi {onam['ism']}, u {onam['t_joy']}-da tug'ilgan, {onam['t_yil']}-yilda. Kasbi: {onam['kasb']}.")
# print(f"Akamning ismi {akam['ism']}, u {akam['t_joy']}-da tug'ilgan, {akam['t_yil']}-yilda. Kasbi: {akam['kasb']}.")



# sevimli_ovqat={
#     "ali":"osh",
#     "vali":"shashlik",
#     "hasan":"lag'mon",
#     "husan":"manti",
#     "maryam":"somsa"
# }
# print(f"{sevimli_ovqat['ali']}, {sevimli_ovqat['husan']}, {sevimli_ovqat['maryam']}")


# python={
#     "integer":"butun son",
#     "float":"o'nlik son",
#     "string":"matn",
#     "if":"agar",
#     "else":"aks holda",
#     "for":"uchun",
#     "while":"qachonki",
#     "list":"ro'yxat",
#     "tuple":"o'zgarmas ro'yxat",
#     "dictionary":"lug'at"
# }
# for key, value in python.items():
#     print(f"{key} - {value}")



# vocabularys={
#     "apple":"olma",
#     "banana":"banan",
#     "grape":"uzum",
#     "orange":"apelsin",
#     "peach":"shaftoli",
#     "pear":"nok",
#     "plum":"o'rik",
#     "cherry":"gilos",
#     "watermelon":"tarvuz",
#     "melon":"qovun"
# }
# user=input("Biror meva kiriting (ingliz tilida): ").lower()
# if user in vocabularys:
#     print(f"{user.title()} so'zning o'bek tilidagi tarjimasi: {vocabularys[user]}.")
# else:
#     print("Kechirasiz, bizda bunday meva yo'q.")



# ___________________________________  END  ___________________________________
# _____________________________________________________________________________


# talaba={
#     "ism":"Ali",
#     "familiya":"Valiyev",
#     "yosh":20,
#     "fakultet":"Informatika",
#     "kurs":3
# }
# for key, value in talaba.items():
#     print(f"{key}: {value}")


# telifonlar={
#     "suhrob": "Samsung Gallaxy S25 Ultra",
#     "ali":"iphone 13",
#     "vali":"samsung galaxy s22",
#     "hasan":"xiaomi redmi note 11",
#     "husan":"google pixel 6",
#     "maryam":"oneplus 10 pro"
# }
# for i, q in telifonlar.items():
#     print(f"{i.title()}ning telifoni {q}.")


# mahsulotlar={
#     "olma":10000,
#     "banan":15000,
#     "anor":20000,
#     "shaftoli":25000,
#     "gilos":30000
# }
# for keys in mahsulotlar.keys():
#     print(keys)
# print(mahsulotlar.keys())



# mahsulotlar={
#     "olma":10000,
#     "banan":15000,
#     "anor":20000,
#     "shaftoli":25000,
#     "go'sht":30000,
#     "uzum":35000,
#     "sabzi":40000,
#     "tarvuz":45000
# }
# bozorlik=["olma","non","go'sht","sabzi","piyoz"]
# for m in mahsulotlar:
#     if m in bozorlik:
#         print(f"{m.title()} {mahsulotlar[m]} so'm")


# mahsulotlar={
#     "olma":10000,
#     "banan":15000,
#     "anor":20000,
#     "shaftoli":25000,
#     "go'sht":30000,
#     "uzum":35000,
#     "sabzi":40000,
#     "tarvuz":45000
# }
# for m  in sorted(mahsulotlar):
#     print(f"{m.title()} {mahsulotlar[m]} so'm")




##########     AMALIYOT         ###########
######  104-bet    ######


# python={
#     "integer":"butun son",
#     "float":"o'nlik son",
#     "string":"matn",
#     "if":"agar",
#     "else":"aks holda",
#     "for":"uchun",
#     "while":"qachonki",
#     "list":"ro'yxat",
#     "tuple":"o'zgarmas ro'yxat",
#     "dictionary":"lug'at"
# }
# for key, value in sorted(python.items()):
#     print(f"{key.title()} - {value.title()}")



# davlatlar={
#     "o'zbekiston":"toshkent",
#     "aqsh":"washington d.c.",
#     "rossiya":"moskva",
#     "xitoy":"pekin",
#     "yaponiya":"tokio"
# }
# for davlat, poytaxt in sorted(davlatlar.items()):
#     print(davlat.title())
#     print(poytaxt.title())


# davlatlar={
#     "o'zbekiston":"toshkent",
#     "aqsh":"washington d.c.",
#     "rossiya":"moskva",
#     "xitoy":"pekin",
#     "yaponiya":"tokio"
# }
# user=input("Davlat nomini kiriting (o'zbek tilida): ").lower()
# if user in davlatlar:
#     print(f"{user}ning poytaxti {davlatlar[user]}")
# else:
#     print("Kechirasiz, bizda bunday davlat yo'q.")



# menyu={
#     "osh":20000,
#     "shashlik":25000,
#     "lag'mon":18000,
#     "manti":22000,
#     "somsa":15000,
#     "shovurma":30000,
#     "norin":28000, 
#     "qazonkabob":35000,
#     "chuchvara":16000,
#     "mastava":14000
# }
# buyurtmalar=[]
# print("3 ta taom buyurtma qiling.")
# for i in range(3):
#     n=i+1
#     buyurtma=input(f"{n}-taom: ").lower()
#     buyurtmalar.append(buyurtma)
# for taom in buyurtmalar:
#     if taom in menyu:
#         print(f"{taom.title()} {menyu[taom]} so'm")
#     else:
#         print(f"Kechirasiz, bizda {taom} yo'q.")





#############      105-betga keldik      #############


# mevalar={"anjir","olma","banan","shaftoli","gilos"}
# mevalar.add("tarvuz")
# print(mevalar)


# mevalar={"anjir","olma","banan","shaftoli","gilos"}
# mevalar.update(["tarvuz", "kivi", "nok"])
# print(mevalar)


# uyinchoqlar={"samaliyot","mashina","robot","dinosaur","teddy bear"}
# uyinchoqlar.remove("robot")
# print(uyinchoqlar)


# bozorlik={"non","sabzi","piyoz","go'sht","guruch","yog'","tuz"}
# bozorlik.discard("yog'")
# print(bozorlik)


# gullar={"lola","atirgul","sunbul","binafsha","qizilg'ul"}
# a=gullar.pop()
# print(gullar)
# print(a)


# A={"olma","banan","shaftoli"}
# B={"banan","anor","uzum"}
# C=A|B
# D=A.union(B)
# print(C)
# print(D)


# A={1,2,3,4,5}
# B={4,5,6,7,8}
# C=A&B
# D=A.intersection(B)
# print(C)
# print(D)


# A={1,2,3,4,5}
# B={4,5,6,7,8}
# C=A-B
# D=A.difference(B)
# E=B-A
# print(C)
# print(D)
# print(E)



# A={1,2,3,4,5}
# B={4,5,6,7,8}
# C=A^B
# D=A.symmetric_difference(B)
# print(C)
# print(D)



# _____________  END  _______________
# ___________________________________

#########   AMALIYOT      ##########



# colors={"red","green","blue"}
# colors2={"yellow","green","black"}
# colors.add("orange")
# colors.update(colors2)
# print(colors)


# set1={10,20,30,40,50}
# set2={30,40,50,60,70}
# a=set1 & set2
# print(a)


# set1={10,20,30,40,50}
# set2={30,40,50,60,70}
# a=set1 - set2
# b=set2 - set1
# print(a)
# print(b)



# set1={10,20,30,40,50}
# set2={30,40,50,60,70}
# a=set1 ^ set2
# print(a)


# car0={
#     "model":"lacetti",
#     "rang":"qora",
#     "yil":2018,
#     "narh":13000,
#     "km":50000,
#     "karobka":"mexanika"
# }
# car1={
#     "model":"nexia 3",
#     "rang":"oq",
#     "yil":2019,
#     "narh":12000,
#     "km":40000,
#     "karobka":"avtomat"
# }
# car2={
#     "model":"gentra",
#     "rang":"qizil",
#     "yil":2020,
#     "narh":15000,
#     "km":30000,
#     "karobka":"mexanika"
# }

# cars=[car0, car1, car2]
# for car in cars:
#     print(f"{car["model"].title()} - {car["rang"]} rang, {car["yil"]} yil, {car["narh"]}$, {car["km"]}km, {car["karobka"]}") 



# dasturchilar={
#     "ali": ["python","c++"],
#     "vali": ["java","c#","html"],
#     "hasan": ["javascript","php"],
#     "husan" : ["python","java","c++"],
#     "maryam": ["c","c++","java"]
# }

# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(til.upper())


# hamkasblar={
#     "ali":{"familiyasi":"valiyev",
#            "yoshi":25,
#            "kasbi":"dasturchi"},
#     "vali":{"familiyasi":"karimov",
#            "yoshi":30,
#            "kasbi":"muhandis"},
#     "hasan":{"familiyasi":"husanov",
#            "yoshi":28,
#            "kasbi":"dasturchi"}
# }

# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()}ning ma'lumotlari:")
#     for key, value in info.items():
#         print(f"{key.title()}: {value}")



# mashxur_shaxslar={
#     "alisher navoiy": {
#         "tyil":1441,
#         "tjoy":"xirot",
#         "kasb":"shoir",
#         "asari":"kitob asari"
#     },
#     "amir temur": {
#         "tyil":1336,
#         "tjoy":"shahrisabz",
#         "kasb":"sarkarda",
#         "asari":"temuriylar asari"
#     },
#     "stiv jobs": {
#         "tyil":1955,
#         "tjoy":"san-fransisko",
#         "kasb":"dasturchi va tadbirkor",
#         "asari":"mantiq asari"
#     },
#     "shekispir": {
#         "tyil":1564,
#         "tjoy":"angliya",
#         "kasb":"shoir va dramaturg",
#         "asari":"qushiq asari"
#     }

# }

# mashxurlar=["alisher navoiy", "amir temur", "stiv jobs", "shekispir"]
# for ism in mashxurlar:
#     info=mashxur_shaxslar[ism]
#     print(f"\n{ism.title()} haqida ma'lumot:")
#     print(f"Tug'ilgan yili: {info['tyil']}")
#     print(f"Tug'ilgan joyi: {info['tjoy'].title()}")
#     print(f"Kasbi: {info['kasb'].title()}")
#     print(f"Mashxur asari: {info["asari"].title()}")


###______________________________________________________________________________________________________________________-



# t = 0
# for i in range(3):
#     t+=1
#     print(f"{t}-sevimli kinoyingiz? >>> ")
#     sevimli_kino=input("Sevimli kinoyingizni kiriting: ")


# misol sharti
# do'stlaringiz yoki oila azolaringizdan .  3 ta sevimli kino-seriallarini haqida so'rang. Do'stingiz ismi kalit,
#  uning sevimli kinolari esa ro'yxat ko'rinishida lug'atga saqlang. Natijani konsolga chiqaring. 

# kinolar = {}

# ism = input("Do'stingiz ismini kiriting: ")
# kinolar[ism] = []

# for i in range(3):
#     kino = input(f"{i+1}-sevimli kino/serialni kiriting: ")
#     kinolar[ism].append(kino)

# print("\nNatija:")
# print(f"{ism.title()}ning sevimli kinolari:")
# for kino in kinolar[ism]:
#     print(f"- {kino}")




# davlatlar={
#     "o'zbekiston":{
#         "poytaxt":"toshkent",
#         "hudud":"448978 km2",
#         "aholi":36_000_000,
#         "pul birligi":"so'm"
#     },
#     "aqsh":{
#         "poytaxt":"washington d.c.",
#         "hudud":"9_833_520 km2",
#         "aholi":331_000_000,
#         "pul birligi":"dollar"
#     },
#     "rossiya":{
#         "poytaxt":"moskva",
#         "hudud":"17_098_242 km2",
#         "aholi":146_000_000,
#         "pul birligi":"rubl"
#     },
# }

# for key, value in davlatlar.items():
#     print(f"{key.title()}ning poytaxti {value['poytaxt'].title()}.")
#     print(f"{key.title()}ning hududi {value['hudud']}.")
#     print(f"{key.title()}ning aholisi {value['aholi']} kishi.")
#     print(f"{key.title()}ning pul birligi {value['pul birligi']}.\n")