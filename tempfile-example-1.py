import tempfile
import os
tempfile = tempfile.mktemp()
print "tempfile", "=>", tempfile
file = open(tempfile, "w+b")
file.write("*" * 1000)
file.seek(0)
print len(file.read()), "bytes"
file.close()
try:
    # must remove file when done
    os.remove(tempfile)
except OSError:
    pass