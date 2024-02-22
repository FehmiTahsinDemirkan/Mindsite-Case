# email_sender.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import re
import logging

class EmailSender:
    def __init__(self, sender_email, sender_password, smtp_server, smtp_port):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    async def send_email(self, receiver_email, subject, body, attachments=None):
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

    async def send_crawl_success_email(self, receiver_email):
        subject = "Crawl Process Successful"
        body = "The crawl process has been completed successfully."
        await self.send_email(receiver_email, subject, body)

    async def send_exported_data_email(self, receiver_email, attachments):
        subject = "Exported Data"
        body = "Please find attached the results of the web crawler."
        await self.send_email(receiver_email, subject, body, attachments)

    @classmethod
    def send_crawler_finished_email(cls, receiver_email):
        cls.send_email(receiver_email, "Crawler Finished", "The crawler has finished its job.")
