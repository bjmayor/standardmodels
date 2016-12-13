import rfc822
file = open("samples/sample.eml")
message = rfc822.Message(file)
print message.getdate("date")
print message.getaddr("from")
print message.getaddrlist("to")