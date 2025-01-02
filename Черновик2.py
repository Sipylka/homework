def recursive_sum(data):
    total = 0  # Счетчик суммы
    if isinstance(data, (list, tuple, set)):  # Если это список, кортеж или множество
        for item in data:
            total += recursive_sum(item)
    elif isinstance(data, dict):  # Если это словарь
        for key, value in data.items():
            total += recursive_sum(key)  # Считаем ключ (если применимо)
            total += recursive_sum(value)  # Считаем значение
    elif isinstance(data, str):  # Если это строка
        total += len(data)  # Добавляем длину строки
    elif isinstance(data, (int, float)):  # Если это число
        total += data  # Добавляем число
    return total

def recursive_print(data):
    if isinstance(data, (list, tuple, set)):  # Если это список, кортеж или множество
        for item in data:
            recursive_print(item)
    elif isinstance(data, dict):  # Если это словарь
        for key, value in data.items():
            recursive_print(key)  # Выводим ключ
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

print("Сумма элементов:", recursive_sum(data_structure))
recursive_print(data_structure)
