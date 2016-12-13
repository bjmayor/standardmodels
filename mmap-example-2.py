import mmap
import os, string, re
def mapfile(filename):
    file = open(filename, "r+")
    size = os.path.getsize(filename)
    return mmap.mmap(file.fileno(), size)
data = mapfile("samples/sample.txt")
# search
index = data.find("small")
print index, repr(data[index-5:index+15])
# regular expressions work too!
m = re.search("small", data)
print m.start(), m.group()