import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail(config: list, mail: MIMEMultipart):
    mail["From"] = config['email']['from']
    mail["To"] = config['email']['to']
    
    with smtplib.SMTP("mail.runbox.com", 587) as sender:
        sender.ehlo()
        sender.starttls()
        sender.ehlo()

        sender.login(config['host']['username'], config['host']['password'])
        sender.send_message(mail)
        sender.quit()
    print('Mail send!')     
        

