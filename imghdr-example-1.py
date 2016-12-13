#coding=UTF-8
import imghdr
result = imghdr.what("samples/sample.png")
if result:
    print "file format:", result
else:
    print "cannot identify file"


#需要安装PIL,在维护的版本是Pillow
import Image
im = Image.open("samples/sample.png")
print im.format, im.mode, im.size
