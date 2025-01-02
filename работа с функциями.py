# data = {'a': 4, 'b': 5}
# for key, value in data.items():
#     print(len(key))  # Выводим ключ
#     print(value)  # Выводим значение

# def summa(a,b):
#     return a+b
# print (summa(5,6))

# def privet(name = 'Гость'):
#     if name == "":
#         return f'Привет, Гость'
#     return f'Привет, {name}'
# print(privet())

# def chetnoe(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
# print(chetnoe(5))

# def razvorot (str):
#     return str[::-1]
#
# print(razvorot('Вася'))

# def kvadrat_elementov_spiska(spisok):
#     resultat = []
#     for i in spisok:
#         resultat.append(i ** 2)
#     return resultat
# print(kvadrat_elementov_spiska([1, 2, 3, 4]))

# def ymnozhenie_na_dva(spisok_vxod):
#     spisok_isxod = []
#     for i in spisok_vxod:
#         spisok_isxod.append(i * 2)
#     return spisok_isxod
# print(ymnozhenie_na_dva([1, 2, 3, 4]))

# def tolko_chetnie(spisok):
#     chetnie = []
#     for i in spisok:
#         if i % 2 == 0:
#             chetnie.append(i)
#     return chetnie
# print(tolko_chetnie([1, 2, 3, 4, 5, 6]))

# def tolko_chetnie(spisok):
#     return [i for i in spisok if i % 2 == 0]
# print(tolko_chetnie([1, 2, 3, 4, 5, 6]))

# def ybrat_otric(spisok):
#     polozhitelnie = []
#     for i in spisok:
#         if i >= 0:
#             polozhitelnie.append(i)
#     return polozhitelnie
# print(ybrat_otric([-1, 3, -5, 8, 0]))

# def summa_spiska(spisok):
#     summa = 0
#     for i in spisok:
#         summa += i
#     return summa
# print(summa_spiska([1, 2, 3, 4]))

# def proizvedenie_spiska(spisok):
#     summa = 1
#     for i in spisok:
#         summa *= i
#     return summa
# print(proizvedenie_spiska([1, 2, 3, 4]))

# def max_chislo(a,b):
#     if a > b:
#         return a
#     elif b>a:
#         return b
#     else:
#         return f'они равны'
#
# print(max_chislo(10,10))

# def srednee_chislo(spisok):
#     return int((spisok[0] + spisok [-1]) / 2)
# print(srednee_chislo([1, 2, 3, 4, 5]))

