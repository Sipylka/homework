sender = "university.help@gmail.com"
x = 'vasyok1337@gmail.com'
#if not ('.ru' or '.com' or '.net') in x:
if '@' in x :
    print(x)
    print(f'Невозможно отправить письмо с адреса {sender} на адрес {x}')
    print('нет')
else:
    print(x)
    print('есть')
    #print(sender.find('@'))

#send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')