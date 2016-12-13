import zlib
encoder = zlib.compressobj()
data = encoder.compress("life")
data = data + encoder.compress(" of ")
data = data + encoder.compress("brian")
data = data + encoder.flush()
print repr(data)
print repr(zlib.decompress(data))