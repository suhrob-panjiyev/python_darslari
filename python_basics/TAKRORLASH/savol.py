# student = {
#     "name":"Suhrob",
#     "age":20,
#     "yunalishi":"IT",
#     "qiziqishi":"GYM"
# }
# print(student)
# print(student.get("name"))
# print(student.get("age"))
# print(student.keys())
# print(student.values())
# student.update({"age": 21, "city": "Qarshi"})
# student.update({"name": "Suha_AI", "sport": "Fudbol"})
# print(student)
# print(student.items())
# student.pop("city")
# print(student)
# student.popitem()
# print(student)









list_items=[1, 2, [4, 5, 7], [5, 8, -7, 8, [4, 5, -7, [7, -8, 9, 1]]]]
# list ichidagi raqamlari yig'indisini topish "sum"

def sum_list(list_):
    summa=0
    for i in list_:
        if type(i)==list:
            summa+=sum_list(i)
        else:
            summa+=i
    return summa
print(sum_list(list_items))


# faktarial, fibanache 


# palindroma="aziza"
# palindroma="non"
# palindroma="abba"
# palindroma="tut"
# palindroma="kiyik"
# palindroma[::-1]==palindroma

# def check_pldr(word)-> bool:
#     return 1

# def check(word):
#     n=len(word)

#     for i in range(n//2):
#         if word[i] !=word[n-i-1]:
#             return False
        
#     return True

# print(check("abbi"))
# print(check("tut"))
# print(check("aziza"))


