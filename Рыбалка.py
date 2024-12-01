xodki = int(input('Сколько раз ходили? '))
i = 1
summa = 0
while i <= xodki:
    summa += int(input(f'Вес {i} мешка? '))
    i += 1
print(summa)