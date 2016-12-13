import quopri
import StringIO
# helpers (the quopri module only supports file-to-file conversion)
def encodestring(instring, tabs=0):
    outfile = StringIO.StringIO()
    quopri.encode(StringIO.StringIO(instring), outfile, tabs)
    return outfile.getvalue()
def decodestring(instring):
    outfile = StringIO.StringIO()
    quopri.decode(StringIO.StringIO(instring), outfile)

    return outfile.getvalue()
#
# try it out
MESSAGE = "? i ?a ? e ?!"
encoded_message = encodestring(MESSAGE)
decoded_message = decodestring(encoded_message)
print "original:", MESSAGE
print "encoded message:", repr(encoded_message)
print "decoded message:", decoded_message