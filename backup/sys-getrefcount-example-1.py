import sys
variable = 1234
print sys.getrefcount(0)
print sys.getrefcount(variable)
print sys.getrefcount(None)