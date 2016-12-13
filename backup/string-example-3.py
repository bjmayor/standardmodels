import string
print int("4711"),
print string.atoi("4711"),
print string.atoi("11147", 8),
print string.atoi("1267", 16),
print string.atoi("3mv", 36) # whatever...
print string.atoi("4711", 0),
print string.atoi("04711", 0),
print string.atoi("0x4711", 0)
print float("4711"),
print string.atof("1"),
print string.atof("1.23e5")