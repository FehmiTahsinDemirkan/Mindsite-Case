import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import pandas as pd
from tabulate import tabulate


class EmailSender:
    def __init__(self, sender_email, sender_password, smtp_server, smtp_port):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def _is_valid_gmail_address(self, email):
        # Gmail adresi kontrolü için basit bir regex
        pattern = re.compile(r"[a-zA-Z0-9_.+-]+@gmail\.com$")
        return bool(pattern.match(email))

    async def send_email(self, receiver_email, subject, body, attachments=None):
        while not self._is_valid_gmail_address(receiver_email):
            print("Error: Please enter a valid Gmail address.")
            receiver_email = input("Enter the recipient's Gmail address: ")

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

    async def send_crawl_success_email(self, receiver_email):
        while not self._is_valid_gmail_address(receiver_email):
            print("Error: Please enter a valid Gmail address.")
            receiver_email = input("Enter your Gmail address: ")

        subject = "Crawl Process Successful"
        body = "The crawl process has been completed successfully."
        await self.send_email(receiver_email, subject, body)
        print("Crawl Process Mail Sent")

    async def send_exported_data_email(self, receiver_email, product_data, attachments=None):
        subject = "Exported Data"
        body = self._create_html_table(product_data)

        await self.send_email(receiver_email, subject, body, attachments)
        print("Exported Data Mail Sent")

    def _create_html_table(self, product_data):
        # Veriyi bir Pandas DataFrame'e dönüştür
        df = pd.DataFrame(product_data)

        # HTML tablosu oluşturmak için tabulate kullan
        html_table = tabulate(df, headers='keys', tablefmt='html', showindex=False)

        # HTML etiketlerini temizle
        html_table_cleaned = re.sub(r'<.*?>', '', html_table)

        # E-posta gövdesine eklemek üzere biçimlendirilmiş HTML tablosunu döndür
        return f"<html><body><p>Below is the exported data in a table format:</p>{html_table_cleaned}</body></html>"
