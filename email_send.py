import smtplib
import ssl
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(password, email, name_of_file):
    sender_address = email[0]
    receiver_address = email[1]
    message = MIMEMultipart("alternative")
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Martian rover.'
    
    mail_content = '''Hello,
    the email contains the results of the experiment as an attachment.
    Thank You'''
    
    message.attach(MIMEText(mail_content, 'plain'))
    
    try:
        with open(name_of_file, "rb") as attachment:
            p = MIMEApplication(attachment.read(), _subtype="txt")
            p.add_header('Content-Disposition', "attachment; filename= %s" % name_of_file)
            message.attach(p)
    except Exception as e:
        print(str(e))

    make_context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=make_context) as server:
        server.login(sender_address, password)
        server.sendmail(sender_address, receiver_address, message.as_string())
