#coding=UTF-8
import md5
import string
import base64
hash = md5.new()
hash.update("spam, spam, and eggs")
value = hash.digest()
print hash.hexdigest()
# before 2.0, the above can be written as
# 在 2.0 前, 以上应该写做:
# print string.join(map(lambda v: "%02x" % ord(v), value), "")
print base64.encodestring(value)
