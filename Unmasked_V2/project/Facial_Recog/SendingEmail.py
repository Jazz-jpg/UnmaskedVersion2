#Imports for using email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

##Title: How to Send Emails Using Python - Plain Text, Adding Attachments, HTML Emails, and More
#Author: Corey Schafer
#Date:  2019
#Code Version: Python3
#Abailability: https://www.youtube.com/watch?v=JRCJ6RtE3xU, https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Emails

#gets email from db and sends automated email
def sendEmail(Useremail):
    #Email and password to be sent from
    email = 'rcyang@oakland.edu'
    password = 'windDragon9'
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