# coding=UTF-8
import mmap
import os
filename = "samples/sample.txt"
file = open(filename, "r+")
size = os.path.getsize(filename)
data = mmap.mmap(file.fileno(), size)
# basics
print data

print len(data), size
# use slicing to read from the file
# 使用切片操作读取文件
print repr(data[:10]), repr(data[:10])
# or use the standard file interface
# 或使用标准的文件接口
print repr(data.read(10)), repr(data.read(10))