def fibonacci(n):
    if not isinstance(n, int) or n<0:
        return 'Введите положительное целое число'
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)  # Рекурсивный случай

# def fibonacci(n):
#     if not isinstance(n, int) or n < 0:
#         return "Введите неотрицательное целое число"
#     if n == 0:  # Базовый случай
#         return 0
#     if n == 1:  # Базовый случай
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)  # Рекурсивный случай


print(fibonacci(8))
# # for i in range(6):
# #     print(f"{i}! = {factorial(i)}")