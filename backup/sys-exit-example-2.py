import sys
print "hello"
try:
    sys.exit(1)
except SystemExit:
    pass
print "there"