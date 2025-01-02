def summ_of_number(n):
    if n == 0:
        return 1
    return n + summ_of_number(n - 1)

print(summ_of_number(5))