x = 'vasyok1337@gmail.com'
#t = x.find('@') != -1 and (x[-4:].find('.ru') != -1 or x[-4:].find('.com') != -1 or x[-4:].find('.net') != -1)
#print(t,x)
if '@' or '.ru' not in x:
    print('есть @')