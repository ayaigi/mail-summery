import email
from imapclient import IMAPClient
from datetime import date, datetime, timedelta
from createmail import stnTime


def withhin(dt, time):
    now = datetime.now().astimezone()
    dif = now - stnTime(dt)   #datetime.strptime(dt, "%a, %d %b %Y %H:%M:%S %z").astimezone()
    return (dif<timedelta(hours=time))
 
        
def recieve(config):
    recentEmail = []
    with IMAPClient(config['host']['imap_host']) as server:
        server.login(config['host']['username'], config['host']['password'])
        foldList = []
        list = server.list_folders()
        for x in list:
            if x[2] == "Spam": break
            foldList.append(x[2])
        foldList.remove('Sent')
        foldList.remove('Drafts')
        for folder in foldList:
            folderMail = []
            server.select_folder(folder)
            miDays = round(config['sys']['time'] / 24) + 1
            messages = server.search(['SINCE', (date.today() - timedelta(days=miDays))])
            for uid, message_data in server.fetch(messages, "RFC822").items():
                email_message = email.message_from_bytes(message_data[b"RFC822"])
                #print(email_message)
                mailDate = email_message.get('Date') 
                if withhin(mailDate, config['margin_time']):
                    folderMail.append({
                        'From': email_message.get('From'),
                        'To': email_message.get('To'),
                        'Subject': email_message.get('Subject'),
                        'Date': email_message.get('Date')
                    })
                    
            recentEmail.append({
                'Name' : folder,
                'Emails' : folderMail
                })
                            
            server.unselect_folder()
        
        server.logout()
    print("Mails recieved!")
    return recentEmail


    
