import fnmatch
import os, re
pattern = fnmatch.translate("*.jpg")
for file in os.listdir("samples"):
    if re.match(pattern, file):
        print file
print "(pattern was %s)" % pattern