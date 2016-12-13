import ftplib
import sys
def gettext(ftp, filename, outfile=None):
    # fetch a text file
    if outfile is None:
        outfile = sys.stdout
    # use a lambda to add newlines to the lines read from the server
    ftp.retrlines("RETR " + filename, lambda s, w=outfile.write: w(s+"\n"))
def getbinary(ftp, filename, outfile=None):
# fetch a binary file
    if outfile is None:
        outfile = sys.stdout
    ftp.retrbinary("RETR " + filename, outfile.write)
ftp = ftplib.FTP("123.56.99.154")
ftp.login("anonymous", "ftplib-example-2")
gettext(ftp, "hello.txt")
