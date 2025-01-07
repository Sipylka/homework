# Из строки текст = "Праздник на деревне" удали все символы, стоящие на чётных позициях.
# Ожидаемый результат:
# раник н дервн

# stroka = 'Праздник на деревне'
# stroka2 = ''
# for i in range(len(stroka)):
#     if (i + 1) % 2 != 0:  # Учитываем сдвиг позиций
#         stroka2 += stroka[i]
# print(stroka2)

# stroka = 'Праздник на деревне'
# stroka2 = ''
# for i in range(len(stroka)):
#     if i % 2 != 0:  # Удаляем чётные позиции (0, 2, 4, ...)
#         continue
#     stroka2 += stroka[i]
# print(stroka2)

stroka = 'Праздник на деревне'
result = ''.join([char for i, char in enumerate(stroka) if i % 2 != 0])
print(result)