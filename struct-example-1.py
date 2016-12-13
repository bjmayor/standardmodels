import struct
# native byteorder
buffer = struct.pack("ihb", 1, 2, 3)
print repr(buffer)
print struct.unpack("ihb", buffer)
# data from a sequence, network byteorder
data = [1, 2, 3]
buffer = apply(struct.pack, ("!ihb",) + tuple(data))
print repr(buffer)
print struct.unpack("!ihb", buffer)
# in 2.0, the apply statement can also be written as:
# buffer = struct.pack("!ihb", *data)