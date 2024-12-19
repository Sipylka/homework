def get_multiplied_digits(number):
    str_number = str(number)
    if not str_number:
        return 1
    first = int(str_number[0])
    if first == 0:
        return get_multiplied_digits(str_number[1:])
    else:
        return first * get_multiplied_digits(str_number[1:])

result = get_multiplied_digits(40203)
print(result)

result2 = get_multiplied_digits(402030)
print(result2)
