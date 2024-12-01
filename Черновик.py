x = 'shataev.artur@mail.com'
i = x.find('@')
print(len(x), i, x[0:i])
if x[-4:].find('.ru') != -1 or x[-4:].find('.com') != -1 or x[-4:].find('.net') != -1:
    print('есть')
else:
    print('нет')
print(x[-4:])