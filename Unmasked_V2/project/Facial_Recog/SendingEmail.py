#Imports for using email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


#gets email from db and sends automated email
def sendEmail(Useremail):
    #Email and password to be sent from
    email = ''
    password = ''
    #Email to be sent to
    #Currently static,get email from DB in future

    #send_to_email = 'lunarflaring@gmail.com'
    send_to_email = Useremail
    #Email subject and body
    subject = 'WARNING: Mask Mandate Violation' # The subject line
    message = 'This is my message'

    #Code from library to create email 
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject

    # Attach the message to the MIMEMultipart object
    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string() # You now need to convert the MIMEMultipart object to a string to send
    server.sendmail(email, send_to_email, text)
    server.quit()
    return
