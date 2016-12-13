import zipfile
import glob, os, time
file = zipfile.ZipFile("test.zip", "w")
now = time.localtime(time.time())[:6]
for name in ("life", "of", "brian"):
    info = zipfile.ZipInfo(name)
    info.date_time = now
    info.compress_type = zipfile.ZIP_DEFLATED
    file.writestr(info, name*1000)
file.close()
# open the file again, to see what's in it
file = zipfile.ZipFile("test.zip", "r")
for info in file.infolist():
    print info.filename, info.date_time, info.file_size, info.compress_size