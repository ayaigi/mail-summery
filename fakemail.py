def testMails():
    return [
    {'Name': 'Ayaigi', 'Emails': 
        [{
        'From': 'Test <test@gmail.com>', 
        'To': 'test@runbox.eu', 
        'Subject': 'Test Thunder', 
        'Date': 'Wed, 2 Nov 2022 21:29:14 +0100'
        }, {
        'From': '<test@test.de>', 
        'To': 'test@runbox.eu', 
        'Subject': 'Test Thunder', 
        'Date': 'Wed, 2 Nov 2022 21:28:24 UTC'
        }]
    }, 
    {'Name': 'Business', 'Emails': 
        [{
        'From': 'Test <test@gmail.com>', 
        'To': 'test@runbox.eu', 
        'Subject': 'Test Thunder', 
        'Date': 'Wed, 2 Nov 2022 21:29:14 +0100'
        }, {
        'From': '<test@test.de>', 
        'To': 'test@runbox.eu', 
        'Subject': 'Test Thunder', 
        'Date': 'Wed, 2 Nov 2022 21:28:24 GMT'
        }]
    }, 
    {'Name': 'Info', 'Emails': 
        [{
        'From': '<test@test.de>', 
        'To': 'test@runbox.eu', 
        'Subject': 'Test Thunder', 
        'Date': 'Wed, 2 Nov 2022 21:28:24 GMT'
        }, {
        'From': '<test@test.de>', 
        'To': 'test@runbox.eu', 
        'Subject': 'Test Thunder', 
        'Date': 'Wed, 2 Nov 2022 21:28:24 GMT'
        }]
    }
]