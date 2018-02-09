import smtplib
import random
from email.mime.multipart import MIMEMultipart

server = 'smtp.gmail.com' # Mail server address
port = 587 # ports: 587, 465
from_user_name = '' # From address
from_user_password = '' # Password
from_user_nickname = 'From: AutoMail'# Mail nickname

words = ['IPA','Health Plan','ID','Claims Address','Group','Claim','Phone','Fax','Contact','AdjusterEmail','UtilReviewPhone',
        'UtilReviewFax','Doctor','NPI','DateofInjury','BodyParts','BodyPartide','Gender','Diagnosis','Diagnosis','Procedure']

domains = ["gmail.com", "ya.ru", "mail.ru", "yahoo.com", "openslave.com", "yandex.ru", "hotmail.com", "aol.com", "mail.com",
               "mail.kz"]

def subject_generator():
    random_word = words[random.randint(0, len(words) - 1)]
    random_domain = domains[random.randint(0, len(domains) - 1)]
    number = str(random.randint(0, 99999))
    subject = '{0}{1}{2}{3}'.format(random_word,number,'@',random_domain)
    return subject


def send_mails_to_address(to_address,count_of_mails):
    for i in range (0,count_of_mails):

        msg = MIMEMultipart('mixed')
        msg['Subject'] = from_user_name
        msg['From'] = from_user_nickname
        msg['To'] = to_address

        s = smtplib.SMTP(server, port)
        s.ehlo()
        s.starttls()
        s.ehlo()
        # Авторизация
        s.login(from_user_name, from_user_password)
        # Отправка пиьма
        s.sendmail(from_user_nickname, to_address, msg.as_string())
        s.quit()
        print(i)
