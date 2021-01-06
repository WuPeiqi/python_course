import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from config import settings


def send_email(subject, content, *email):
    """ 发送邮件
    :param subject: 邮件主题
    :param content: 邮件内容
    :param email: 收件人，可以是一个也可以是多个。
    :return: None
    """
    msg = MIMEText(content, 'html', 'utf-8')
    msg['From'] = formataddr([settings.EMAIL_FROM_NAME, settings.EMAIL])
    msg['Subject'] = subject
    server = smtplib.SMTP_SSL(settings.EMIAL_SMTP)
    server.login(settings.EMAIL, settings.EMAIL_PWD)
    server.sendmail(settings.EMAIL, email, msg.as_string())
    server.quit()
