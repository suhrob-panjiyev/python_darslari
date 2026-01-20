##  o'yin yaratamiz   "o'yla izla top"

import random
komp_number=random.randint(1, 10)
print(komp_number)  #  bu yer g'irommlik qilish uchun  :)
imkon_kodi=5
while imkon_kodi>0:
    user_num=int(input("raqam kirit: "))
    if user_num==komp_number:
        print("Siz yutdingiz")
        break
    else:
        print("keyingi raqam kirit:, hozircha topolmadingiz :)")
    imkon_kodi-=1