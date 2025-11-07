from random import randint
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

RANDOM_CODE = randint(100000, 999999)
PASSWORD = os.getenv('PASSWORD')
EMAIL = os.getenv('EMAIL')


def send_email(e):
	smtp_server = smtplib.SMTP("smtp.mail.ru", 587)
	smtp_server.starttls()
	smtp_server.login(EMAIL, PASSWORD)

	msg = MIMEMultipart()
	msg['From'] = EMAIL
	msg['To'] = e
	msg['Subject'] = 'Секретный код'
	text = f"Для того, чтобы иметь возможность управлять постами введите в адресной строке после имени всего имени этот код: {RANDOM_CODE} "
	msg.attach(MIMEText(text, 'plain'))

	smtp_server.sendmail(EMAIL, e, msg.as_string())


def check_code(user_code: int) -> bool:
	if user_code == RANDOM_CODE:
		return True
	return False