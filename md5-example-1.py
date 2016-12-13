import md5
hash = md5.new()
hash.update("spam, spam, and eggs")

print repr(hash.digest())