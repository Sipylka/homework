def send_email(message, recipient, sender = "university.help@gmail.com"):
    x = str(recipient)
    if x.find('@') != -1 and x[-4:].find('.ru') != -1 or x[-4:].find('.com') != -1 or x[-4:].find('.net') != -1:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

#send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')