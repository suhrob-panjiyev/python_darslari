###############        FUNKSIYA        ##################

# def tugilgan_yil_hisobla():
#     ism=input("Ismingizni kiriting: ")
#     yosh=int(input("Yoshingizni kiriting: "))
#     joriy_yil=2025
#     hisoblash=joriy_yil-yosh
#     return hisoblash
# print(tugilgan_yil_hisobla())

# def tugilgan_yil_hisola(ism, yosh):
#     joriy_yil=2025
#     tugilgan_yil=joriy_yil-yosh
#     return f"{ism.title()}, siz {tugilgan_yil}-yilda tug'ilgansiz."
# ism=input("Ismingizni kiriting: ")
# yosh=int(input("Yoshingizni kiriting: "))
# print(tugilgan_yil_hisola(ism, yosh))



# def kvadrat_kub(son):
#     kvadrat=son**2
#     kub=son**3
#     return f"{son} ning kvadrati {kvadrat} ga, kubi {kub} ga teng."
# son=int(input("Sonni kiriting: "))
# print(kvadrat_kub(son))



# def juft_toq(son):
#     if son % 2 == 0:
#         return f"{son} Juft son."
#     else:
#         return f"{son} Toq son."
# son=int(input("Son kiriting: "))
# print(juft_toq(son))



# def katta_kichik(a, b):
#     if a>b:
#         return f"a katta."
#     elif a<b:
#         return f"b katta."
#     else:
#         return f"a teng b ga."
# a=int(input("a ni kiriting: "))
# b=int(input("b ni kiriting: "))
# print(katta_kichik(a, b))


# def x_ning_n_drajasi(x, n=2):
#     natija=pow(x,n)
#     return f"{x} ning {n}-darajasi {natija} ga teng."
# x=int(input("x ni kiriting: "))
# # n=int(input("n ni kiriting: "))
# print(x_ning_n_drajasi(x))



# def qoldiqsiz_bulinishini_aniqla(son):
#     qoldiqsiz_bulinuvchilar=[]
#     qoldiqli_bulinuvchilar=[]
#     for i in range(2, 11):
#         if son % i == 0:
#             qoldiqsiz_bulinuvchilar.append(i)
#         elif son % i != 0:
#             qoldiqli_bulinuvchilar.append(i)
#     return f"Qoldiqsiz bulinuvchilar: {qoldiqsiz_bulinuvchilar}.\nQoldiqli bulinuvchilar {qoldiqli_bulinuvchilar}"

# son=int(input("Sonni kiriting: "))
# print(qoldiqsiz_bulinishini_aniqla(son))




def avto_info(make, model, rangi, karobka, yili, narxi=None):
    avto={
        "kompaniya":make ,
        "model":model,
        "rangi":rangi,
        "karobka":karobka,
        "yili":yili, 
        "narxi":narxi
    }
    return avto

print("Saytimizdagi avtolar ro'yxatini shakillantiramiz.")
avtolar=[]

while True:
    print("\nQuyidagi malumotlarni kiriting", end='')
    kompaniya=input(" Ishlab chiqaruvchi: ")
    model=input("Model: ")
    rangi=input("Rangi: ")
    karobka=input("Karobka: ")
    yili=input("Ishlab chiqarilgan yili: ")
    narxi=input("Narxi: ")
    avtolar.append(avto_info(kompaniya, model, rangi, karobka, yili, narxi))

    javob=input("Yana avto qushasizmi? (yes/no): ")
    if javob=="no":
        break