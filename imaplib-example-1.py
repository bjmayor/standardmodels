import imaplib
import string, random
import StringIO, rfc822
SERVER = "imap.spam.egg"
USER  = "mulder"
PASSWORD = "trustno1"
# connect to server
server = imaplib.IMAP4(SERVER)
# login
server.login(USER, PASSWORD)
server.select()
# list items on server
resp, items = server.search(None, "ALL")
items = string.split(items[0])
# fetch a random item
id = random.choice(items)
resp, data = server.fetch(id, "(RFC822)")
text = data[0][1]
file = StringIO.StringIO(text)
message = rfc822.Message(file)
for k, v in message.items():
    print k, "=", v
print message.fp.read()
server.logout()