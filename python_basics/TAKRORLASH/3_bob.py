######  49-bet ######


# num=int(input("son kiriting: "))
# print(f"{num} ning kvadrati {num**2} ga teng")
# print(f"{num} ning kubi {num**3} ga teng")


# yosh=int(input("yoshingiz nechida?: "))
# tyil=2025-yosh
# print(f"Siz {tyil} yilda tug'ilgansiz")


# num1=int(input("1-sonni kiriting: "))
# num2=int(input("2-sonni kiriting: "))
# amal=input("amalni kiriting (+,-,*,/): ")
# if amal=="+":
#     print(f"{num1}+{num2}={num1+num2}")
# elif amal=="-":
#     print(f"{num1}-{num2}={num1-num2}")
# elif amal=="*":
#     print(f"{num1}*{num2}={num1*num2}")
# elif amal=="/":
#     if num2==0:
#         print("0 ga bo'lib bo'lmaydi")
#     else:
#         print(f"{num1}/{num2}={num1/num2}")   
# else:
#     print("Noto'g'ri amal kiritildi")



#######  52-bet ######

# mevalar=["olma","anor","banan","shaftoli","gilos"]
# mevalar.append("tarvuz")
# mevalar.append("o'rik")
# print(mevalar)

# cars=[]
# cars.append("BMW")
# cars.append("Mercedes")
# cars.append("Toyota")
# print(cars)


# animals=[]
# animals.append("it")
# animals.append("mushuk")
# animals.append("quyon")
# print(animals)


# cars=["BMW","Mercedes","Toyota"]
# cars.insert(0, "Audi")
# cars.insert(2, "Kia")
# print(cars)


# fruits=["olma","anor","banan","shaftoli","gilos"]
# del fruits[0]
# print(fruits)

# mevalar=["olma","anor","banan","shaftoli","gilos"]
# mevalar.remove("banan")
# print(mevalar)

# oyinchoqlar=["mashina","samolyot","qayiqlar","robot"]
# oyinchoqlar.remove("qayiqlar")
# print(oyinchoqlar)

# compyuterlar=["HP","Dell","Asus","Acer"]
# compyuterlar.remove("Dell")
# print(compyuterlar)


# bozorlik=["yog'", "un", "non", "piyoz", "kartoshka"]
# a=bozorlik.pop(2)
# print("Olingan mahsulot:", a)
# print("Qolgan mahsulotlar:", bozorlik)


# ismlar=["Ali","Vali","Hasan"]
# name1=ismlar.pop(0)
# name2=ismlar.pop(0)
# name3=ismlar.pop(0)
# print("Salom", name1)
# print("Salom qalesan", name2)
# print("Salom nima qilyapsan ", name3)



# cars=["BMW","Mercedes","Toyota","Audi","Kia"]
# cars.sort()
# print(cars)

# nums=[5,3,8,1,4]
# nums.sorted()
# print(nums)  


# cars=["BMW","Mercedes","Toyota","Audi","Kia"]
# my_cars=cars[0:3]
# print(my_cars)


# ismlar=["Ali","Vali","Hasan","Husan","Olim"]
# t=0
# for ism in ismlar:
#     t+=1
#     print(f"Salom, {ism}! Qalesan?")
# print(f"Jami {t} ta ism bor")



# toq_sonlar_royxati=[]
# kubi=[]

# for n in range(10, 100, 2):
#     toq_sonlar_royxati.append(n)
#     kubi.append(n**3)
# print(toq_sonlar_royxati)
# print(kubi)



nechta_odam=int(input("Nechta odam bilan suhbatlashdingiz?: "))
odamlar=[]
for i in range(nechta_odam):
    odam=input(f"{i+1} - odam kim edi?: ")
    odamlar.append(odam)
print(f"Siz quyidagi odamlarlar bilan suhbatlashdingiz:")
for x in odamlar:
    print(x)