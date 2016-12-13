import multifile
import cgi, rfc822
infile = open("samples/sample.msg")
message = rfc822.Message(infile)
# print parsed header
for k, v in message.items():
    print k, "=", v
# use cgi support function to parse content-type header
type, params = cgi.parse_header(message["content-type"])
if type[:10] == "multipart/":
    # multipart message
    boundary = params["boundary"]
    file = multifile.MultiFile(infile)
    file.push(boundary)
    while file.next():
        submessage = rfc822.Message(file)
        # print submessage
        print "-" * 68
        for k, v in submessage.items():
            print k, "=", v
        print
        print file.read()
    file.pop()
else:
    # plain message
    print infile.read()