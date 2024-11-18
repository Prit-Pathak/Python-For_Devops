import getpass
import smtplib

host = "smtp.gmail.com"
port = 587

from_user = "pritpathak63@gmail.com"
to_user = "pritpathak56@gmail.com"
password = getpass.getpass("enter password: ")

message = """ Subject: Mail sent using python
Hi Prit,

This mail has been sent using python automation script.

Thanks,
PPP
"""
smtp = smtplib.SMTP(host, port)  # create object of smtp

# check if smtp mail server is up and running
status_code, res = smtp.ehlo()
print(f"[*]echoing the server {status_code} {res}")

# start TLS connection for sending mail securely.
status_code, res = smtp.starttls()
print(f"[*] starting TLS connection {status_code} {res}")

# loging to your email
status_code, res = smtp.login(from_user, password)
print(f"[*] logging in {status_code} {res}")

smtp.sendmail(from_user, to_user, message)

smtp.quit()
