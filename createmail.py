import re
import datetime
from table_html import table_html
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
            

def creaMail(info: list) -> MIMEMultipart:
    msg = MIMEMultipart('alternative')
    subj = mailSubj(info)
    text = mailText(info)
    html = mailHtlm(info)
    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg['Subject'] = subj
    
    msg.attach(part1)
    msg.attach(part2)
    print('Mail created')
    
    return msg
    
def mailHtlm(info: list):
    tb = table_html(3)
    bone = """\
    <html>
    <head></head>
    <body>
        <p>
            {}
        </p>
    </body>
    </html>
    """
    for fol in info[1]:
        if type(fol) is str:
            tb.add_header_row(fol)
        else:        
            tb.add_row(fol)
    html = bone.format(tb.print())
    return html


def mailText(info: list):
    str = []
    for spl in info[1]:
        if type(spl) is list:
            str.append(' '.join(spl))
        else:
            str.append(spl)
    return '\n'.join(str)
    

def mailSubj(info: list):
    return ' '.join(info[0])


def sortmail(config, mails):
    subject = [config['email']['subject']]
    content = []
    for fold in mails:
        name = fold['Name']
        emails = fold['Emails']
        str = "{0}:{1}".format(short(config, name), len(emails))
        subject.append(str)
        content.append(name)
        for mail in emails:
            su = mail['Subject']
            fr = shoFrm(mail['From'])
            #to = mail['To']
            dt = reformDate(mail['Date'])
            content.append([su, fr, dt])
    return [subject, content]


def short(config, name):
    try:
        key = config['folders'][name]
    except:
        key = name
    return key

def shoFrm(name = ""):
    na = re.split('<|>', name)
    return na[0] if na[0] != '' else na[1]

def reformDate(date):
    do = stnTime(date).strftime("%H:%M")
    return do

def stnTime(date):
    dtfs = [
        "%a, %d %b %Y %H:%M:%S %z",
        "%a, %d %b %Y %H:%M:%S %Z",
        "%a, %d %b %y %H:%M:%S %z",
        "%a, %d %b %y %H:%M:%S %Z",
        "%d %b %Y %H:%M:%S %Z",
        "%d %b %y %H:%M:%S %Z",
        "%d %b %Y %H:%M:%S %z",
        "%d %b %y %H:%M:%S %z",
    ]
    for dtf in dtfs:   
        try:
            dt = datetime.datetime.strptime(date, dtf)
            break
        except:
            dt = False
    if dt == False:
        print("ErrorNoParsing: " + date)
        dt = datetime.datetime.strptime("01.01.1970:12:00:00", "%d.%m.%Y:%H:%M:%S")
    return dt