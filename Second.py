from email.message import EmailMessage
import ssl
import smtplib
from passw import password

sender_email = "bruwoski@gmail.com"
email_password = password

receiver_email = "sudarshan513@gmail.com"

subject = "Subscribe please"

body = """ 

This is my first phython project. I hope I learn python fast and able to chane my job.

"""

em = EmailMessage()
em['From'] = sender_email
em['To'] = receiver_email
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
      smtp.login(sender_email, email_password)
      smtp.sendmail(sender_email, receiver_email, em.as_string())

