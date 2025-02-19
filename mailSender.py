import smtplib
from email.mime.text import MIMEText
from config import GMAIL_PASSWORD
# ЗАПОЛНИТЬ (нужна именно gmail почта и еще включенная настройка) В настройках почты ->
# Ненадежные приложения, у которых есть доступ к аккаунту -> ON
# Почта с которой идет письмо
gmail_user = "bySeleznevaHeiG@gmail.com"
gmail_password = GMAIL_PASSWORD

# Почта ЦОКа
to = "ceq@spbstu.ru"  # ЗАПОЛНИТЬ


def send_mail(question, mail, fio):
    message = question + f"\n\nПожалуйста, пришлите ответ на почту: {mail}\n\n\nПисьмо сформировано при помощи " \
                         f"телеграм-бота для помощи студентам."
    subject = "Вопрос в ЦКО от " + fio

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(gmail_user, gmail_password)
        msg = MIMEText(message)
        msg["Subject"] = subject
        server.sendmail(gmail_user, to, f"{msg.as_string()}")

        return "The message was sent!"
    except Exception as _ex:
        return f"{_ex}\n Something went wrong!"
