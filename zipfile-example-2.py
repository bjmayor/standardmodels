import zipfile
file = zipfile.ZipFile("samples/sample.zip", "r")
for name in file.namelist():
    data = file.read(name)
    print name, len(data), repr(data[:10])