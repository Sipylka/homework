def summator (txt, *values, type = 'sum'):
    s = 0
    for i in values:
        s += i
    return f'{txt}{s} {type}'


print(summator('Сумма чисел: ', 2, 3, 4, type = 'summator'))