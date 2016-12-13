import rfc822
file = open("samples/sample.eml")
message = rfc822.Message(file)
for k, v in message.items():
    print k, "=", v
print len(file.read()), "bytes in body"