from send import sendMail
from createmail import creaMail, sortmail
from email.mime.multipart import MIMEMultipart


def iterate(config):
    mails = recieve(config)

    mailInfo = sortmail(config, mails)
    mail = creaMail(mailInfo)
    #printMail(mail)
    sendMail(config, mail)
    
    
def printMail(mail: MIMEMultipart):
     print(mail)