from random import randint
from itertools import product
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

RANDOM_CODES = [int(''.join(i)) for i in product('1234567890', repeat=6)]
CODE = RANDOM_CODES[randint(0, len(RANDOM_CODES) - 1)]

def send_email(e, p):
	smtp_server = smtplib.SMTP("smtp.mail.ru", 587)
	smtp_server.starttls()
	smtp_server.login('skeatw@mail.ru', p)

	msg = MIMEMultipart()
	msg['From'] = 'skeatw@mail.ru'
	msg['To'] = e
	msg['Subject'] = 'Секретный код'
	text = f"Для того, чтобы иметь возможность управлять постами введите в адресной строке после имени всего имени этот код: {CODE} "
	msg.attach(MIMEText(text, 'plain'))

	smtp_server.sendmail('skeatw@mail.ru', e, msg.as_string())

