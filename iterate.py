from send import sendMail
from recive import recieve
from fakemail import testMails
from createmail import creaMail, sortmail
from email.mime.multipart import MIMEMultipart


def iterate(config, fake):
    if fake:
        mails = testMails()
    else:
        mails = recieve(config)

    mailInfo = sortmail(config, mails)
    mail = creaMail(mailInfo)
    #printMail(mail)
    sendMail(config, mail)
    
    
def printMail(mail: MIMEMultipart):
     print(mail)