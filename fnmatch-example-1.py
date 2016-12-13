import fnmatch
import os
for file in os.listdir("samples"):
    if fnmatch.fnmatch(file, "*.jpg"):
        print file