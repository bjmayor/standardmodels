import array
def little_endian():
    return ord(array.array("i",[1]).tostring()[0])
if little_endian():
    print "little-endian platform (intel, alpha)"
else:
    print "big-endian platform (motorola, sparc)"

