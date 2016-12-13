import zipfile
import glob, os
# open the zip file for writing, and write stuff to it
file = zipfile.ZipFile("test.zip", "w")
for name in glob.glob("samples/*"):
    file.write(name, os.path.basename(name), zipfile.ZIP_DEFLATED)
file.close()
# open the file again, to see what's in it
file = zipfile.ZipFile("test.zip", "r")
for info in file.infolist():
    print info.filename, info.date_time, info.file_size, info.compress_size
