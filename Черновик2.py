def recursive_print(data):
    if isinstance(data, (list, tuple, set)):  # Если это список, кортеж или множество
        for item in data:
            recursive_print(item)
    elif isinstance(data, dict):  # Если это словарь
        for key, value in data.items():
            recursive_print(len(key))  # Выводим ключ
            recursive_print(value)  # Выводим значение
    else:  # Если это не коллекция, выводим элемент
        print(data)

# Тестируем на предоставленных данных
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

recursive_print(data_structure)
