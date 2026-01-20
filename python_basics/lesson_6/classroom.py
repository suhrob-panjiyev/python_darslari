# # Raqamlar yig'indisini 
# user=int(input("Son kiriting: "))
# yigindi=0
# while True:
#     if user==0:
#         break
#     yigindi+=user%10
#     user=user//10
# print(yigindi)


user=int(input("Raqam kiriting: "))
a=0
for son in range(1, user+1):
    a=a*10+son
print(a)
