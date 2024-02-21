# email_sender.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import re


class EmailSender:
    def __init__(self, sender_email, sender_password, smtp_server, smtp_port):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, receiver_email, subject, body, attachments=None):
        # Set up the MIME
        message = MIMEMultipart()
        message["From"] = self.sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        # Attach body to the email
        message.attach(MIMEText(body, "plain"))

        # Attach files to the email
        if attachments:
            for attachment in attachments:
                with open(attachment, "rb") as file:
                    part = MIMEApplication(file.read(), Name=attachment)
                    part["Content-Disposition"] = f"attachment; filename={attachment}"
                    message.attach(part)

        # Connect to SMTP server and send email
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, receiver_email, message.as_string())
        # Başarı mesajını yazdır
        print("Email sent successfully!")

async def mail_sender(sender_email, sender_password, smtp_server, smtp_port):
    while True:
        # Kullanıcıdan alıcı e-posta adresini al
        receiver_email = input("Enter the recipient's email address: ")

        # Alıcı e-posta adresinin geçerli bir Gmail adresi olup olmadığını kontrol et
        if re.match(r'^[a-zA-Z0-9._%+-]+@gmail\.com$', receiver_email):
            break
        else:
            print("Invalid email address. Please enter a valid Gmail address.")

    # Diğer işlemleri gerçekleştir
    subject = "Web Crawler Results"
    body = "Please find attached the results of the web crawler."
    attachments = ["output.csv", "output.json", "output.xlsx"]

    email_sender = EmailSender(sender_email, sender_password, smtp_server, smtp_port)
    email_sender.send_email(receiver_email, subject, body, attachments)

# Kullanım örneği:
# await mail_sender("dfehmitahsin@gmail.com", "flko lpqg kzdn tioq", "smtp.gmail.com", 587)
