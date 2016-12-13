class A:
    pass
class B:
    pass
class C(A):
    pass
class D(A, B):
    pass
def dump(object):
    print object, "=>",
    if issubclass(object, A):
        print "A",
    if issubclass(object, B):
        print "B",
    if issubclass(object, C):
        print "C",
    if issubclass(object, D):
        print "D",
    print
dump(A)
dump(B)
dump(C)
dump(D)
dump(0)
dump("string")