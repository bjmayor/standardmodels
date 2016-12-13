execfile("hello.py")
def EXECFILE(filename, locals=None, globals=None):
    exec compile(open(filename).read(), filename, "exec") in locals, globals
EXECFILE("hello.py")