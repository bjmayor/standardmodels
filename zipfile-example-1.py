import zipfile
file = zipfile.ZipFile("samples/sample.zip", "r")
# list filenames
for name in file.namelist():
    print name,
print
# list file information
for info in file.infolist():
    print info.filename, info.date_time, info.file_size