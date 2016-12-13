import atexit
def exit(*args):
    print "exit", args
# register two exit handler
atexit.register(exit)
atexit.register(exit, 1)
atexit.register(exit, "hello", "world")