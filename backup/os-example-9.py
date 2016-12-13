import os
import sys
try:
    sys.exit(1)
except SystemExit, value:
    print "caught exit(%s)" % value
try:
    os._exit(2)
except SystemExit, value:
    print "caught exit(%s)" % value
print "bye!"
