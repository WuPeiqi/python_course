import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import config


def send_email(subject, content, *email):
    """ 发送邮件
    :param subject: 邮件主题
    :param content: 邮件内容
    :param email: 收件人，可以是一个也可以是多个。
    :return: None
    """
    msg = MIMEText(content, 'html', 'utf-8')
    msg['From'] = formataddr([config.EMAIL_FROM_NAME, config.EMAIL])
    msg['Subject'] = subject
    server = smtplib.SMTP_SSL(config.EMIAL_SMTP)
    server.login(config.EMAIL, config.EMAIL_PWD)
    server.sendmail(config.EMAIL, email, msg.as_string())
    server.quit()
