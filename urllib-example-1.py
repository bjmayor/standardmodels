import urllib
#这个网站设置了ua限制.直接这样抓取的数据其实是错的.
fp = urllib.urlopen("http://go2live.cn")
op = open("out.html", "wb")
n= 0
while 1:
    s = fp.read(8192)
    if not s:
        break
    op.write(s)
    n = n + len(s)
fp.close()
op.close()
for k, v in fp.headers.items():
    print k, "=", v
print "copied", n, "bytes from", fp.url