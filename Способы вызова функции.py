def send_email(message, recipient, sender="university.help@gmail.com"):
    str_1 = "@"
    str_2 = ".com", ".ru", ".net"
    if not any(i in sender for i in str_1):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    elif not any(j in sender for j in str_2):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    elif not any(k in recipient for k in str_1):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    elif not any(l in recipient for l in str_2):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
        return
    if sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с {sender} на адрес {recipient}")
        return


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')











