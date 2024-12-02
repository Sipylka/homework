x = 'vasyok1337@gmail.com'
i = x.find('@')
print(len(x), i, x[0:i])
if x.find('@') != -1 and x[-4:].find('.ru') != -1 or x[-4:].find('.com') != -1 or x[-4:].find('.net') != -1:
    print('есть')
else:
    print('нет')
print(x[-4:])

#send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')