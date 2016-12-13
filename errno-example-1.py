import errno
try:
    fp = open("no.such.file")
except IOError, (error, message):
    print message
    if error == errno.ENOENT:
        print "no such file"
    elif error == errno.EPERM:
        print "permission denied"
    else:
        print message