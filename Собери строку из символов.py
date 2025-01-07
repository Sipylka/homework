# Напиши код, который создаёт строку из каждого третьего символа строки текст = "Здравствуй, деревня!".
# Ожидаемый результат:
# Зрсв ерн

# stroka = 'Здравствуй, деревня!'
# # for i in range(len(stroka)):
# #     if i % 3 == 0: print(stroka[i], end='')
# # print()
# # print(stroka[::2])
# print(stroka[::3])

stroka = 'Здравствуй, деревня!'
result = ''
for i in range(len(stroka)):
    if i % 3 == 0:
        result += stroka[i]
print(result)