#          A' L   i     
# shuni sening isming Ali deb chiqarish kk.

# turlarga 5 tadan misol qilib turini aniqlash 5 tadan

#har bir metodga 5 tadan misol yozish

# 5 ta listni bulaklarga(slaysing) bulish

# kitobdan 61-betgacha 

# # ---->  TASK 1 

# ism=" . -=a4L$   I 899()"
# jarayon=filter(str.isalpha, ism) # bundan tashqari .isdigit-> faqat raqamlar oladi, .isalnum -> raqam va harflarni oladi.
# natija="".join(jarayon)
# print("Ismingni juda ham notug'ri yozgan ekansan, sening isming: ", natija.capitalize(), "\nTo'g'ri yozishni o'rgan😁")

# # ----> TASK 2

# a=45
# b="55"
# c=-4.5
# d=-4,5
# f=(1, 56, 'salom', True)
# j=True
# ab=[1, 'salom', True, -4.5, [1,2,3,4,5]]
# ac={1,2,2,2,3,3,5,7,9,8,8,10}
# bb={"name": "Ali"}
# bc={"age": 20}
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(f))
# print(type(j))
# print(type(ab))
# print(type(ac))
# print(type(bb))
# print(type(bc))

# ----> TASK 3

a1=['salom', True, 45, -6.4, 4,5, 1, 2, 3, 4, 5, 6]
oxiri=a1[-3:]
boshi=a1[:4]
yangi=oxiri+boshi
print(yangi)
print(a1[0:4])
print(a1[0:-1])
print(a1[::5])
print(a1[-3:5])