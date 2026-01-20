# a={"ali":7}
# try:
#     a["Ali"]
# except Exception as e:
#     print(e)


# try:
#     print(7/0)
# except ZeroDivisionError:
#     print("nolga bo'lib bo'maydi")
# except ValueError:
#     print("Value error")
#     pass
# except Exception as e:
#     print(e)
# else:
#     print("men faqat try ishlasa ishlayman")
# finally:
#     print("men har doim ishlayman, try ga ham exeptga ham")







#######    FUNKSIYA 


# FUNKSIYA
# print()
# input()
# range()
# len()
# sum()

# def funksiya_nomi(ism="Ali"):
#     print(f"SAlom {ism}!")

# funksiya_nomi("Oysha")
# funksiya_nomi(ism="Vali")

# def toq_juft_funksiya(num):
#     if num % 2 == 0:
#         return 'Juft'
#     return 'Toq'

# print(toq_juft_funksiya(num=11))
# user2 = toq_juft_funksiya(num=17)
# user3 = toq_juft_funksiya(num=100)
# print(f"user2 ning natijasi: {user2} \n user3 niki: {user3}")

# def katta_kichik(num1, num2=None):
#     if not num2:
#         return "kamida 2 ta son kiriting:)"
#     if num1 > num2:
#         return num1
#     elif num1 == num2:
#         return "teng"
#     return num2

# print(katta_kichik(num1=10))
# print(katta_kichik(num1=4, num2=6))


def sonning_faktariali(num1, num2=None):
    t=1
    if num2:
        for i in range(num1, num2 + 1):
            t = t * i
        return t
    
    for i in range(1, num1):
        t = t * i
    return t

# print(sonning_faktariali(4))
# print(sonning_faktariali(2 , 5))




def baholar_dict():
    baholar = {}
    jami = 0

    for i in range(10):
        fan = input(f"{i+1}-fan nomini kiriting: ")
        baho = float(input(f"{fan} fanidan bahoni kiriting: "))
        baholar[fan] = baho
        jami += baho

    ortacha = jami / 10
    baholar["o'rtacha ball"] = ortacha

    return baholar

natija = baholar_dict()
print(natija)
