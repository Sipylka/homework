# Напиши код, который подсчитает количество гласных и согласных в строке текст = "Деревенский уют".
# Ожидаемый результат:
# Гласных: 6
# Согласных: 9

glasnie = ['а','у','о','и','э','ы','я','ю','е','ё',]
count_glasnie = 0
soglasnie = ['б','в','г','д','ж','з','й','к','л','м','н','п','р','с','т','ф','х','ц','ч','ш','щ','Д']
count_soglasnie = 0
ost_simvol = 0
stroka = 'Деревенский уют'
for i in range(len(stroka)):
    if stroka[i] in glasnie:
        count_glasnie += 1
    elif stroka[i] in soglasnie:
        count_soglasnie += 1
    else:
        ost_simvol += 1

print(f'Длина строки {len(stroka)}')
print(f'Гласных: {count_glasnie}')
print(f'Согласных: {count_soglasnie}')
print(f'Остаьных символов {ost_simvol}')