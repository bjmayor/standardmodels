import smtplib
import string, sys
HOST = "localhost"
FROM = "effbot@spam.egg"
TO = "fredrik@spam.egg"
SUBJECT = "for your information!"
BODY = "next week: how to fling an otter"
body = string.join((
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT,
    "",
    BODY), "\r\n")

print body
server = smtplib.SMTP(HOST)
server.sendmail(FROM, [TO], body)
server.quit()
