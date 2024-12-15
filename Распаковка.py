def print_params (a = 1, b = 'строка', c = True):
    return print(a, b, c)

values_list = [1, ('a', 'b'), True]
values_dict = {'a': 123, 'b': False, 'c': 'столбец'}
values_list_2 = ['abc', 333]
print('вывод списка')
print_params(*values_list)

print('вывод словаря')
print_params(**values_dict)
print('вывод подставок')
print_params(b=25)
print_params(c = [1,2,3])

print('вывод списка 2')
print_params(*values_list_2, 42)