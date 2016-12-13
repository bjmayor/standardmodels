import ftplib
ftp = ftplib.FTP("123.56.99.154")
ftp.login("anonymous", "ftplib-example-1")
print ftp.dir()
ftp.quit()