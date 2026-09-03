# Import os
# os allows Python to read environment variables
import os

# Import smtplib
# smtplib is Python's built-in library for sending emails
import smtplib

# Import EmailMessage
# EmailMessage helps us create the email
from email.message import EmailMessage

# Import load_dotenv
# load_dotenv() reads values from our .env file
from dotenv import load_dotenv

# Load the variables from the .env file
load_dotenv()

# Read the sender email from the .env file
EMAIL_USER = os.getenv("EMAIL_USER")

# Read the email password/app password from the .env file
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Read the receiver email from the .env file
EMAIL_TO = os.getenv("EMAIL_TO")

# Create a function to send an email
# The function receives the ERROR/WARNING messages
def send_email(alerts):

    if not alerts:
        print("No alerts to send.")
        return False

    if not EMAIL_USER or not EMAIL_PASSWORD or not EMAIL_TO:
        print("Email configuration is missing. Please set EMAIL_USER, EMAIL_PASSWORD, and EMAIL_TO in .env")
        return False

    # Create an email message object
    message = EmailMessage()

    # Set the sender email
    message["From"] = EMAIL_USER

    # Set the receiver email
    message["To"] = EMAIL_TO

    # Set the email subject
    message["Subject"] = "Log Analyzer Alert"

    # Convert the list of alerts into one text message
    email_body = "\n".join(alerts)

    # Set the email body
    message.set_content(email_body)

    try:
        # Connect to Gmail's SMTP server
        # smtp.gmail.com is Gmail's mail server
        # 587 is the port used for secure email submission
        with smtplib.SMTP("smtp.gmail.com", 587) as server:

            # Start TLS encryption
            server.starttls()

            # Login using the email credentials
            server.login(EMAIL_USER, EMAIL_PASSWORD)

            # Send the email
            server.send_message(message)
    except Exception as exc:
        print(f"Failed to send email: {exc}")
        return False

    # Print a confirmation message
    print("Email sent successfully.")
    return True
