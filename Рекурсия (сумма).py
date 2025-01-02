def summa(n):
    if not isinstance(n, int) or n<0:
        return 'Введите положительное целое число'
    if n == 1:  # Базовый случай
        return 1
    return n + summa(n - 1)  # Рекурсивный случай

print(summa(5))