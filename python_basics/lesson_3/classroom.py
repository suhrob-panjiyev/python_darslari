# # tuples
# my_tuple=(1,2,3,4,5)
# my_list=list(my_tuple)
# print(type(my_list))
# my_list.append(10)
# my_tuple=tuple(my_list)
# print(my_tuple)

# # for
# my_student=['Ali', 'Vali', 'Oysha']
# for std in my_student:
#     print(std)
#     print(f"Welcome to {std}")

# # range
# my_nums=[1,2,3,4,5,6,7,8,9]
# my_nums=range(10)
# for num in range(10):
#     print(f"{num} ning kvadrati: {num**2}")

# for num in range(9, 0, -1):
#     print(num)


# ism=input("5a ism kiriting: ")
# my_list=[]
# my_list.append(ism.upper())
# print(my_list)

# 5 ta sonning o'rta qiymati

yigindi=[]   # list 
for n in range(5):
    user_input=float(input(f"{n+1}-raqamni kiriting: "))
    yigindi.append(user_input)
    print(f"hozzirgi yig'indi {yigindi}")
print(f"o'rtacha qiymat: {sum(yigindi)//5}")

yigindi=0    # oddiyl
for n in range(5):
    user_input=float(input(f"{n+1}-raqamni kiriting: "))
    yigindi=yigindi+user_input
    print(f"hozzirgi yig'indi {yigindi}")
print(f"o'rtacha qiymat: {yigindi//5}")

















# kupaytma=1
# for n in range(5):
#     user_input=float(input(f"{n+1}-sonni kiriting: "))
#     kupaytma=kupaytma*user_input
#     natija=kupaytma//5
# print(f"orta qiymat: {natija}")

# """ if mavzusi"""

# n=int(input("n="))
# if n>0:
#     print("n 0 dan katta.")
# elif n<0:
#     print("n 0 dan kichik.")
# else:
#     print("n 0 ga teng.")


# a=int(input("Yoshingizni kiriting: "))
# if 0<a<=7:
#     print("Kirishga ruxsat yuq, Siz hali yoshsiz")
# elif 7<a<=18:
#     print("Kirishingzi mumkin, Bilet narxi 10 ming:")
# elif 18<a<=65:
#     print("Kirishingiz mumkin, Bilet narxi 20 ming:")
# elif a>65:
#     print("Kirishga mumkin sizga bepul")
# elif a<0:
#     print("siz hali tug'ulmagansiz😁")
# else:
#     print("Nimadir xato: Qayta urinib kuring:")

# my_list=[]
# for n in range(1, 11):
#     if n%3==0:
#         my_list.append(n)
# print(my_list)

# fizz=[]
# bazz=[]
# fizzbazz=[]
# a1=0
# b=0
# c=0

# a=int(input("1 dan 100 gacha son kiriting: "))
# for n in range(1, a+1):
#     if n%15==0:
#         fizzbazz.append(n)
#         a1=a1+1
#     elif n%5==0:
#         bazz.append(n)
#         b=b+1
#     elif n%3==0:
#         fizz.append(n)
#         c=c+1
        
# print("FizzBazz", fizzbazz, f"{a1} ta")
# print("Bazz", bazz, f"{b} ta")
# print("Fizz", fizz, f"{c} ta")