import smtplib


def sendemail(fromaddr,fromname,subject,msg):
    toaddr = ''
    message = """From: {} <{}>
    To: {} Jesse
    Subject: {}
    {}
    """

    messagetosend = message.format(
                                 fromaddr,
                                 fromname,
                                 toaddr,
                                 subject,
                                 msg)

    # Credentials (if needed)
    username = ''
    password = ''

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddr, messagetosend)
    server.quit()
