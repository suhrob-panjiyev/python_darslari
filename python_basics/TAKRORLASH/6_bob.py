#################        122-bet    ##############

#################       AMALIYOT    ##############


# while True:
#     user=input("Yaxshi kurgan kitobingizni kiriting(to'xtatish uchun stop ni yozing.): ")
#     if user == "stop":
#         print("Dastur tuxtadi.")
#         break
#     else:
#         print(f"Sizning yoqtirgan kitobingiz, {user} kitobi.")




# while True:
#     user_stop=input("Yoshingizni kiriting(to'xtatish uchun stop yoki quit ni yozing.): ")

#     if user_stop == "stop" or "quit":
#         print("Dastur tuxtadi :)")
#         break

#     user=int(user_stop)

#     if user < 7 :
#         print("Chipta narxi 2000 so'm")
#     elif 7 <= user < 18 :
#         print("Chipta narxi 3000 so'm")
#     elif 18 <= user < 65 :
#         print("Chipta narxi 10000 so'm")
#     elif user >= 65 :
#         print("Chipta bepul.")
 


# print("Do'staringizni yoshini saqlaymiz.")

# dostlar = {}
# ishora = True
# while ishora :
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh)

#     javob=input("Yana malumot qushasizmi(ha/yuq): ")
#     if javob == "yuq":
#         ishora=False
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")



# cars=["laceti", "nexia", "jshdvc", "wbi", "nexia", "iwvciw", "nexia"]
# while "nexia" in cars:
#     cars.remove("nexia")
# print(cars)



# talabalar=["hasan", "husan", "olim", "botir"]
# baholangan_talabalar={}
# while talabalar:
#     talaba=talabalar.pop()
#     baho=input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi.")
#     baholangan_talabalar[talaba]=baho
# print(f"Baholangan talabalar: {baholangan_talabalar}")



# mahsulotlar_ruyxati=[]
# ishora=True
# while ishora:
#     user=input("Buyurtmangizni yozing(tugaganda 'stop'): ")
#     mahsulotlar_ruyxati.append(user)
#     if user == "stop":
#         print("Buyurtmalaringiz qabul qilindi:")
#         ishora = False
# print("Maxsulotlar ruyxati:", mahsulotlar_ruyxati)



# e_bozor_mahsulotlar={}
# ishora=True
# while ishora:
#     mahsulot=input("Mahsulot kiriting: ")
#     mahsulot_narxi=int(input(f"{mahsulot.title()}ning narxini kiriting: "))
#     e_bozor_mahsulotlar[mahsulot]=mahsulot_narxi
#     a=input("Toxtatish uchun 'stop' aks holda 'goo' : ")
#     if a == "stop":
#         print("Buyurtmalar qabul qilindi. ")
#         ishora = False 
#     elif "goo":
#         ishora=True

# print(f"Mahsulotlar ruyxati: {e_bozor_mahsulotlar}")



