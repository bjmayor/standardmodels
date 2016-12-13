import zlib
MESSAGE = "life of brian"
compressed_message = zlib.compress(MESSAGE)
decompressed_message = zlib.decompress(compressed_message)
print "original:", repr(MESSAGE)
print "compressed message:", repr(compressed_message)
print "decompressed message:", repr(decompressed_message)