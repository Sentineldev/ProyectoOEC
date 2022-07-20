from email.message import EmailMessage
import ssl 
import smtplib
def SendEmail(subject,body):

    max_tries = 3
    current_tries = 0
    flag = False
    while current_tries != max_tries:
        try:
            email_emisor = "proyectooec12@gmail.com"
            email_password = "fmjonhvmftazelsy"
            email_receptor = "jesusfiguera20@gmail.com"

            mail = EmailMessage()
            mail["From"] = email_emisor
            mail["To"] = email_receptor
            mail["Subject"] = subject
            mail.set_content(body)
            context = ssl.create_default_context()

            with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
                smtp.login(email_emisor,email_password)
                smtp.sendmail(email_emisor,email_receptor,mail.as_string())
            current_tries = 3
            flag = True
        except Exception as e:
            current_tries+=1
    return flag
    

