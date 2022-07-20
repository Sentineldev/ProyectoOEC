
from email.message import EmailMessage
import ssl
import smtplib




email_receptor = "jesusfiguera20@gmail.com"

asunto = "Probando envio"
cuerpo = "Hola te he enviado un mensaje!"

em = EmailMessage()

em['From'] = email_emisor
em['To'] = email_receptor

em['Subject'] = asunto
em.set_content(cuerpo)



context  = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
    smtp.login(email_emisor, email_password)
    smtp.sendmail(email_emisor, email_receptor, em.as_string())