import ftplib
import os
def upload(ftp, file):
    ext = os.path.splitext(file)[1]
    if ext in (".txt", ".htm", ".html"):
        ftp.storlines("STOR " + file, open(file))
    else:
        ftp.storbinary("STOR " + file, open(file, "rb"), 1024)
ftp = ftplib.FTP("123.56.99.154")
ftp.login("test", "go2live.cn")
upload(ftp, "samples/sample.txt")
