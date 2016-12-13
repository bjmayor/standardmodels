import sha
hash = sha.new()
hash.update("spam, spam, and eggs")
print repr(hash.digest())

print hash.hexdigest()