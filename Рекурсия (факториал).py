def factorial(n):
    if n == 0:
        return 1
    if not isinstance(n, int) or n<0:
        return 'Введите положительное целое число'
    if n == 1:  # Базовый случай
        return 1
    return n * factorial(n - 1)  # Рекурсивный случай

for i in range(6):
    print(f"{i}! = {factorial(i)}")