def dump(function):
    if callable(function):
        print function, "is callable"
    else:
        print function, "is *not* callable"
class A:
    def method(self, value):
        return value

class B(A):
    def __call__ (self, value):
        return value

a = A()
b = B()
dump(0) # simple objects
dump("string")
dump(callable)
dump(dump) # function
dump(A) # classes
dump(B)
dump(B.method)
dump(a) # instances
dump(b)
dump(b.method)