import poplib
import string, random
import StringIO, rfc822
SERVER = "pop.spam.egg"
USER  = "mulder"
PASSWORD = "trustno1"
# connect to server
server = poplib.POP3(SERVER)
# login
server.user(USER)
server.pass_(PASSWORD)
# list items on server
resp, items, octets = server.list()
# download a random message
id, size = string.split(random.choice(items))
resp, text, octets = server.retr(id)
text = string.join(text, "\n")
file = StringIO.StringIO(text)
message = rfc822.Message(file)
for k, v in message.items():
    print k, "=", v
print message.fp.read()