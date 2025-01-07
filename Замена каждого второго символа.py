# Для строки текст = "Мир в деревне" замени каждый второй символ на "*".
# Ожидаемый результат:
# М*р * д*р*в*е

# stroka = 'Мир в деревне'
# stroka2 = ''
# for i in range(len(stroka)):
#         # if stroka[i] == " ": continue
#         if i % 2 != 0:
#             stroka2 += '*'
#         else:
#             stroka2 += stroka[i]
# print(stroka2)

stroka = 'Мир в деревне'
stroka2 = ''
for i in range(len(stroka)):
    if stroka[i] != " " and i % 2 != 0:
        stroka2 += '*'
    else:
        stroka2 += stroka[i]
print(stroka2)