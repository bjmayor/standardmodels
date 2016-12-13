import xdrlib

#
# create a packer and add some data to it
p = xdrlib.Packer()
p.pack_uint(1)
p.pack_string("spam")
data = p.get_buffer()
print "packed:", repr(data)
#
# create an unpacker and use it to decode the data
u = xdrlib.Unpacker(data)
print "unpacked:", u.unpack_uint(), repr(u.unpack_string())
u.done()