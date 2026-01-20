# # TASK 1 

# list_1=[]
# list_2=[]

# a1=0
# b=0
# c=0

# a=int(input("1 dan 100 gacha son kiriting: "))

# for n in range(1, a+1):
#     if n%10==0:
#         list_1.append(n)
#         a1=a1+1
#     elif n%5==0:
#         list_2.append(n)
#         b=b+1
#     elif n%3==0:
#         list_2.append(n)
#         c=c+1
        
# print("10 ga bulinadiganlari: ", list_1, f"{a1} ta")
# print("5 va 3 ga bulinadiganli: ", list_2, f"{b+c} ta")

# # TASK 2 

# musbat_list=[]
# for n in range(10):
#     son=int(input(f"{n+1}-sonni kiriting. >>>"))
#     if son>=0:
#         musbat_list.append(son)
# print(f"Musbat sonlar ro'yxati: {musbat_list}")


# #  TASK 3

# natijalar = []

# n=int(input("n="))
# for x in range(1, n+1):
#     a=float(input(f"{x}-sonni kiriting: "))
#     natijalar.append(a*2)
# print("Natija:", natijalar)
# for y in natijalar:
#     print(y)


#  TASK 4
list_1=[]

for x in range(1, 8):
    a=float(input(f"{x}-bahoni kiriting: "))
    list_1.append(a)

    yigindi=sum(list_1)
    ortacha_qiymat=yigindi/7
    # print(list_1)
    # print(yigindi)
print(ortacha_qiymat)
if ortacha_qiymat<=60:
    print("fail")
elif ortacha_qiymat>=86:
    print("A'lo")
elif 71<ortacha_qiymat<86:
    print("yaxshi")
elif 65<ortacha_qiymat<71:
    print("o'rtacha")