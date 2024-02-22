import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import pandas as pd
from tabulate import tabulate


class EmailSender:
    def __init__(self, sender_email, sender_password, smtp_server, smtp_port):
        # Constructor method for the EmailSender class. Initializes the sender's email, password, SMTP server, and port.
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def _is_valid_gmail_address(self, email):
        # Simple regex check to validate a Gmail address.
        pattern = re.compile(r"[a-zA-Z0-9_.+-]+@gmail\.com$")
        return bool(pattern.match(email))

    async def send_email(self, receiver_email, subject, body, attachments=None):
        # Validates the receiver's email address and sends an email with the provided subject, body, and attachments.

        # Ensure a valid Gmail address is entered.
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
        # Sends an email notifying the user that the crawl process has been completed successfully.

        # Ensure a valid Gmail address is entered.
        while not self._is_valid_gmail_address(receiver_email):
            print("Error: Please enter a valid Gmail address.")
            receiver_email = input("Enter your Gmail address: ")

        subject = "Crawl Process Successful"
        body = "The crawl process has been completed successfully."
        await self.send_email(receiver_email, subject, body)
        print("Crawling Process Alert E-mail Was Sent to Admin ! ")

    async def send_exported_data_email(self, receiver_email, product_data, attachments=None):
        # Sends an email with exported product data in table format as an HTML attachment.

        subject = "Exported Data"
        body = self._create_html_table(product_data)

        await self.send_email(receiver_email, subject, body, attachments)
        print(f"Exported Data Mail Sended to: {receiver_email}")

    def _create_html_table(self, product_data):
        # Converts the product data to a Pandas DataFrame, creates an HTML table using tabulate, and returns the formatted HTML table for the email body.

        # Convert data to a Pandas DataFrame
        df = pd.DataFrame(product_data)

        # Create an HTML table using tabulate
        html_table = tabulate(df, headers='keys', tablefmt='html', showindex=False)

        # Clean up HTML tags
        html_table_cleaned = re.sub(r'<.*?>', '', html_table)

        # Return the formatted HTML table for the email body
        return f"<html><body><p>Below is the exported data in a table format:</p>{html_table_cleaned}</body></html>"
