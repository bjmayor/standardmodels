import tabnanny
FILE = "samples/badtabs.py"
file = open(FILE)
for line in file.readlines():
    print repr(line)
# let tabnanny look at it
tabnanny.check(FILE)