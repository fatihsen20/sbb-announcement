import sys
sys.path.append("..")

import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


load_dotenv()


def send_email(
    body: str
) -> None:
    """
    Send email using the provided subject and body.

    Args
    ----
    body (str): The body of the email.
    """
    subject = "Yeni İş İlanı Var!"
    try:
        from_email = os.getenv("FROM_MAIL")
        password = os.getenv("FROM_MAIL_PASSWORD")
        to_email = os.getenv("TO_MAIL")
    except Exception as e:
        raise Exception("Environment variables are not set properly.")

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'html'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully.")
