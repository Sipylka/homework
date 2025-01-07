# Реализуй простое шифрование: сдвиг каждого символа строки текст = "Привет"
# на 2 позиции вперёд в алфавите (например, "а" станет "в", "я" — "б").
# Ожидаемый результат:
# Трукжх

stroka = "Привет"
smeshenie = 3
shifr = ""

for char in stroka:
    if "а" <= char <= "я":  # Для строчных букв
        new_char = chr((ord(char) - ord("а") + smeshenie) % 32 + ord("а"))
    elif "А" <= char <= "Я":  # Для заглавных букв
        new_char = chr((ord(char) - ord("А") + smeshenie) % 32 + ord("А"))
    else:
        new_char = char  # Не буквы не меняем
    shifr += new_char

print(shifr)