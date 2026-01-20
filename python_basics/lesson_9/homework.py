################            DEF -- FUNKSIYA               #################

# def salom_ber(ism):
#     """Salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")
# salom_ber(ism="Suhrob")


# def salom_ber(ism):
#     """Foydalanuuvchi ismini qabul qilib,
#     unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")
# print(salom_ber.__doc__)
# print(salom_ber(ism='suhrob'))


# def ism_familiya(ism, familiya):
#     """Ism familiyani jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchini familiyasi: {familiya.title()}")
# ism_familiya(ism="suhrob", familiya="panjiye")



# def tugilga_yil(ism, tugilgan_yili):
#     """Tug"ilgan yilni hisoblash funksiyasi"""
#     print(f"{ism.title()} {2025-tugilgan_yili} yoshda")
# tugilga_yil(ism="Suhrob", tugilgan_yili=2005)



###########          155-bet       1-misol                      ##########################

# def yosh_hisobla(tugilgan_yil, joriy_yil):
#     """Tug'ilgan yildan yoshini hisoblaymiz"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
#     tugilgan_yil=input("Tug'ilgan yilingizni kiriting: ")   # 1-xato   tyil emas tugilgan_yil
# yosh_hisobla(tugilgan_yil=2005, joriy_yil=2025)             # 2-xato   tyil emas tugilgan_yil va joriy_yil ga atribut berish va def dan tashqarida yozish


###########          155-bet       2-misol                      ##########################

# def yosh_hisobla(tugilgan_yil, joriy_yil):
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
# yosh_hisobla(1993, 2025)                                      # xato joriy_yil parametiriga atribut yozilmagan


###########          155-bet       3-misol                      ##########################

# def salom_ber(ism):
#     """Salom beruvchi funksiya"""
#     print(f"Assalomu alaykum!, {ism}")                          # print ni ichiga {ism} ni kirgizib ketishimiz kk edi
# salom_ber("hasan")



###########          155-bet       4-misol                      ##########################

# def toliq_ism(ism, familiya):
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
# toliq_ism(ism="olim", familiya="hakimov")                        # xatolik shuyerda





###########    __________>>>>>>   AMALIYOT  1  <<<<<____________   ##########################

###   1-misol


# def tugilgan_yilni_aniqla(ism, yosh):
#     """Tug'ilgan yilingizni aniqlab beruvchi funksiya."""

#     joriy_yil = 2025
#     natija = joriy_yil - yosh
#     print(f"Salom {ism.title()}, siz {natija}-yilda tugilgansiz.")

# tugilgan_yilni_aniqla(ism="Suhrob", yosh=20)


###   2-misol

# def kvadrat_kub_aniqla(son):
#     """Sonning kvadrati va kubini aniqlovch dastur"""

#     kvadrat=pow(son, 2)
#     kub=pow(son, 3)
#     print(f"Sonning kvadrati: {kvadrat} \nSonning kubi: {kub}")

# kvadrat_kub_aniqla(son=3)


###   3-misol

# def juft_toq_aniqla(son):
#     """Sonning juft yoki toq ligini aniqlovchi funksiya"""
#     if son % 2 == 0:
#         return f"{son}-Juft son"
#     else:
#         return f"{son}-Toq son"
# natija=juft_toq_aniqla(son=25)
# print(natija)

###   4-misol

# def katta_kichiklikni_aniqla(son1, son2):
#     """Sonning katta kichikligini aniqlovchi funkksiya"""
#     if son1 > son2:
#         return f"{son1} katta"
#     elif son1 < son2:
#         return f"{son2} katta"
#     elif son1==son2:
#         return f"Sonlar teng"
# natija=katta_kichiklikni_aniqla(son1=5, son2=7)
# print(natija)



###  5-misol

# def daraja_chiqar(x, n):
#     """x ning n-darajasini aniqlovchi funksiya"""
#     hisobla=pow(x, n)
#     return f"{x} ning {n}-darajasi: {hisobla} ga teng."
# print(daraja_chiqar(x=2, n=5))


###   6-misol

# def qoldiqsiz_bolishni_aniqla(son):
#     """sonni 2 dan 10 gacha bo'lgan sonlarga bolib qoldiqsizini aniqlash funksiyasi"""
#     natija=" "
#     for i in range(2, 10+1):
#         if son % i == 0:
#             natija+=f"{son} {i} ga qoldiqsiz bo'linadi.\n"
#         elif son % i != 0:
#             natija+=f"{son} {i} ga bo'linmaydi.\n"
#     return natija
# print(qoldiqsiz_bolishni_aniqla(son=64))


#####  ro'yxatlar bilan kodlanganda      |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# def qoldiqsiz_bolishni_aniqla(son):
#     """Sonni 2 dan 10 gacha bo'lgan sonlarga bo'lib qoldiqsizligini aniqlash funksiyasi"""
#     natijalar = []
#     for i in range(2, 11):
#         if son % i == 0:
#             natijalar.append(f"{son} {i} ga qoldiqsiz bo'linadi.")
#         else:
#             natijalar.append(f"{son} {i} ga bo'linmaydi.")
#     return natijalar

# natija = qoldiqsiz_bolishni_aniqla(64)
# print(natija)

# for x in natija:
#     print(x)




########################## _____________ 8.3 QIYMAT QAYTARUVCHI FUNKSIYA  157-bet _____________

# def toliq_ism_yasa(ism, familiya):
#     """To'lliq ism qaytaruvchi funksiya"""
#     toliq_ism=f"{ism.title()} {familiya.title()}"
#     return toliq_ism

# talaba1=toliq_ism_yasa(ism="olim", familiya="hakimov")
# talaba2=toliq_ism_yasa(familiya="valiyev", ism="ali")
# print(talaba1)
# print(talaba2)

####################  ___________ IXTIYOROY ARGUMENT _______________

# def toliq_ism_yasa(ism, familiya, otasining_ismi=" "):
#     """To'lliq ism qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism=f"{ism} {familiya} {otasining_ismi}"
#     else:
#         toliq_ism=f"{ism} {familiya}"
#     return toliq_ism.title()

# talaba1=toliq_ism_yasa(ism="olim", familiya="hakimov", otasining_ismi="karimovich")
# talaba2=toliq_ism_yasa(familiya="valiyev", ism="ali")
# print(talaba1)
# print(talaba2)


################### ______________  FUNKSIYADAN LUG'AT QAYTARAMIZ  159-BET __________

###########____________________159-betdan   165-betgacha  qilinishi kk________________________####################################