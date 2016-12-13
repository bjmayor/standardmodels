class A:
    def a(self):
        pass

    def b(self):
        pass


class B(A):
    def c(self):
        pass

    def d(self):
        pass

def getmembers(klass, members=None):
    if members is None:
        members = []
    for k in klass.__bases__:
        getmembers(k, members)
    for m in dir(klass):
        if m not in members:
            members.append(m)
    return members
print (getmembers(A))
print getmembers(B)
print getmembers(IOError)