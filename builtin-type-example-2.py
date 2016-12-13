def load(file):
    if isinstance(file, type("")):
        file = open(file, "rb")
    return file.read()
print len(load("hello.py")), "bytes"
print len(load(open("hello.py", "rb"))), "bytes"