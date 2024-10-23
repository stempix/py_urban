def validate_email(email):
    email_domain = email[email.rfind('.'):len(email)]
    if not '@' in email or not email_domain.casefold() in [s.casefold() for s in [".com", ".net", ".ru"]]:
        return False
    return True

def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    if not validate_email(recipient) or not validate_email(sender):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    else:
        text = f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}"
        # Захотелось использовать тернарный оператор
        print(text if sender == "university.help@gmail.com" else "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! " + text)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Please correct the task', 'urban.student@mail.uk', sender='urban.teacher@mail.ru')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')